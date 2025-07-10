# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 13:53:19 2021

@author: Schmelzer
"""
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:22:55 2021


"""
from Config import Config
from SendModule import Interface
from DataParser import DataParser

import numpy as np
import time


class RUST():
    def __init__(self):
        self._data_memory = {}
        self.config = Config()
        self.config.load_config('serial_com_ID20.ini')
        self.device = FMCW(self.config)
        
    def startup(self):
        self.device.open_interface()
        self.device.update_device()
        
    def run(self):
        """Starts a continous measurement task"""
        self.device.set_continous_swp_mode()
        time.sleep(0.1)
        while True:
            self._data_memory = self.device.read()
            print(self._data_memory)
             
    def snapshot(self):
        """Starts a single measurement task"""
        self.device.set_single_swp_mode()
        time.sleep(0.1)
        self._data_memory = self.device.read()
        print(self._data_memory)
        input()
        
    def firmware(self):
        firmware = self.device.get_firmware()
        print(firmware)
        input()
        
    def disconnect(self):
        """Closes the interface to the RF-Frontend"""
        self.device._interface.close()


class Device():
    
    def __init__(self, config):
        self.config = config
        
    def get_dev_name(self):
        """Returns the device name
        
        Return
        ------
        device_name : string
        """
        return self.device_name
    
    def get_firmware(self):
        """ Read the firmware string of the module via UART.

        Returns
        -------
        firmware_out : list
            firmware string form the 'F' command.
        """
        self._interface.sendCommand(self._firmware_command, readACK=False) 
        # vv output does not send an ACK
        firmware_out = []
        for n in range(self._firmware_length):
            firmware_out.append(self._interface.readUntilCR())
        
        return firmware_out
    
    def update_device(self):
        """ Send config values to the Reader """
        self.ident_active = self.config.get('Reader Settings', 'ID')
        if 'Reader Settings' in self.config.sections():
            
            for key in self.config["Reader Settings"]:
                func = self.key_names.get(key)
                func(self.config["Reader Settings"][key], self.device_name)
            print('CONFIG UPLOAD COMPLETE')
            
    def set_single_swp_mode(self):
        """Send 'the single sweep mode command' to the RF-Frontend to enable a 
        single measurement task"""
        self._interface._serInFace.reset_input_buffer()
        self._interface.set_SweepMode(self._single_swpm_cmd, self.device_name)
        
    def set_continous_swp_mode(self):
        """Send 'the continous sweep mode command' to the RF-Frontend to 
        enable the continous sweeping mode
        """
        self._interface._serInFace.reset_input_buffer()
        self._interface.set_SweepMode(self._contin_swpm_cmd, self.device_name)
    
    def disable_sweep_mode(self):
        """Send the sweep mode command with 0 as value to the RF-Frontend to
        disable the measurement of the RF-Frontend"""
        self._interface.set_SweepMode(0, self.device_name)


        
class FMCW(Device):
    
    def __init__(self, config):
        super().__init__(config)
        self.device_name = 'FMCW'
        self._firmware_command = 'F'
        self._firmware_length = 2
        self._UARTDevName = '/dev/ttyAMA0'#'/dev/serial0'
        self._baudrate = 115200
        self._single_swpm_cmd = 6
        self._contin_swpm_cmd = 1
        self._fmcw_dtype = np.int16
        self._response = bytearray() 
        self.config = config
        self.deltapi = DataParser(self.config, self.device_name)
        
    def open_interface(self):
        """Initialize the interface to the RF-Frontend"""
        self._interface = Interface(self._UARTDevName, self._baudrate)
        self.key_names = {
            'RFFrontend'      : self._interface.set_RF_frontend,
            'Sweeps'          : self._interface.set_Sweeps,
            'FreqPoints'      : self._interface.set_FrequencyPoints,
            'FreqStart'       : self._interface.set_StartFrequency,
            'FreqStep'        : self._interface.set_StepSize,
            'Gain'            : self._interface.set_Gain,
            'DataStart'       : self._interface.set_StartSamplePoint,
            'DataStop'        : self._interface.set_StopSamplePoint,
            'Delay'           : self._interface.set_Delay,
            'ADC'             : self._interface.set_ADC,
            'OutputSelect'    : self._interface.set_OutputSelect,
            'AntennaMode'     : self._interface.set_AntennaMode,    
            'Trigger'         : self._interface.set_Trigger,
            'Power'           : self._interface.set_TxLevel,
            'ID'              : self._interface.set_IDdecoder,
            'IDsnr'           : self._interface.set_IDsnr,
            'FFTlength'       : self._interface.set_FFTlength,
            'FFTwindow'       : self._interface.set_FFTwindow}
        
    def read(self):
        """
        The read function works with the DataParser class in order to sort the 
        data for further program execution. The data from the RF front end 
        consists of 2 parts. First the header (first 5 data bytes) and second 
        the actual data. The header of the data packet contains information on 
        the port, the output mode and the length of the actual data. 
        If the value for ID in the config is set to 1, the ID string is 
        appended to the data packet, if available.
        
        A data packet has the following structure:
            |######## Header #########|...|########### Data ###########|
            
            D<Port><Mode><Number Bytes>...<Data><Data><Data><Data><Data>...
        
        - Header: see dataparser - sort_head()
        - Data: data words in low-byte, high-byte format

        Returns
        -------
        dict
            Dictionary contains information on the port, mode and length. It
            also contains the converted data. The datatype of the fmcw data is
            'np.int16'

        """
        self.deltapi.reset_values()
        config_mode = self.deltapi.mode_from_config
        data_gram = self.deltapi.datagram
        

        #receive datagram from device and parse data
        while (config_mode != data_gram):
            
            # data head
            fmcw_header = self._interface.read_headline(self.device_name)
            self.deltapi.sort_head(fmcw_header)
            
            # data body
            dat_len = self.deltapi.get_data_length()
            data_buffer = self._interface.read_length(dat_len)
            fmcw_data = np.frombuffer(data_buffer, dtype=self._fmcw_dtype)
            self.deltapi.sort_data(fmcw_data)
            
            # ident 
            if int(self.ident_active) > 0:
                self._interface._serInFace.timeout = 0.2
                ident_data = self._interface.readUntilCR(1)
                self.deltapi.sort_ident_string((ident_data))
            
            data_gram = self.deltapi.datagram
            
        return self.deltapi.get_output_data()


if __name__ == "__main__":
    try:
        software = RUST()
        software.startup()
        software.run()
        
    finally:
        software.disconnect()