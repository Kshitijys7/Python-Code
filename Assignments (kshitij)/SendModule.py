# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:46:05 2020


@author: Schmelzer
"""

import logging
import serial
from CommandLibrary import CmdLibrary

class Interface():
    
#--------------------------- Common Methods -----------------------------------
    
    def __init__(self, UARTDevName, baudrate):
        #stuff to get connection ready
        self._UARTDevName = UARTDevName     #'/dev/ttyAMA0'
        self._baudrate = baudrate           # 115200
        self._command_library = CmdLibrary()
        
        #setting for logging 
        logging.basicConfig(format='%(levelname)s:%(message)s', \
                            level=logging.INFO)
        
        try:
            self._serInFace = serial.Serial(self._UARTDevName, self._baudrate,\
                                            timeout=5)
            self._serInFace.reset_input_buffer()
            self._serInFace.reset_output_buffer()
            logging.info('CONNECTING TO SERIAL DEVICE {DeviceName}' \
                         .format(DeviceName = self._UARTDevName))
        except serial.serialutil.SerialException:
            logging.error('SERIAL DEVICE {DeviceName} NOT AVAILABLE' \
                          .format(DeviceName = self._UARTDevName))
                
    def read_headline(self, Device):
        """Read the header of a data package. The header length differs 
        with the reader type:
        
        FMCW header (5 bytes)
        ------
        Länge 
        Dies Das
        
        SDM header (6 bytes)
        --------------------
        Noch mehr stuff
        Und das noch
        """
        if Device == 'FMCW':
            return self._serInFace.read_until('', size = 5)
        else:
            return self._serInFace.read_until('', size = 6)
        
    def read_length(self, data_len):
        """Read until the size is exceeded.
        
        Returns
        -------
        bytearray
            Bytearray with size data_len
        """
        return self._serInFace.read_until('', size = data_len)
    
    def read_test(self):
        return self._serInFace.read_until('\r')
    
    def sendCommand(self, cmd, readACK=True):
        """ Send command to UART Device.
        
        A '<CR>' (carriage return) is added to the command.
        
        Parameters
        ----------
        cmd : str, int
            command to send to the UART device
            
        Returns
        -------
        bool : True if ACK was sent from UART device
               False if NACK was sent from UART device   
        """
        try:
            self._serInFace.write(bytes(str(cmd).encode()) + b'\r')
            if readACK == True:
                commandReturn = self._serInFace.read()
                if commandReturn == b'\x06':
                    logging.info('COMMAND {cmd} ACK'.format(cmd = cmd))
                    return True
                elif commandReturn == b'\x15':
                    logging.info('COMMAND {cmd} NACK'.format(cmd = cmd))
                    return False
            else:
                return True
        except serial.SerialException:
            logging.error('SERIAL CONNECTION TIMEOUT')
            
    def readByte(self):
        """Read one byte from the UART interface
        
        Returns
        -------
        byte
            Byte from the UART interface
        """
        return self._serInFace.read()
            
    def readUntilCR(self, MaxEmptyCharLimit=20):
        """ Read bytes from the UART interface until ``\\r`` character.

        Parameters
        ----------
        MaxEmptyCharLimit : int
            Max character count to read, for non-blocking the interface 
            if no ``\\r`` was received, default is 20.
        
        Returns
        -------
        out : str
            Characters read, including ``\\r``. Returns empty `str` if no 
            character was read.
        
        """
        idxTimeout = 0
        out = ''
        while True:
            readStr = self._serInFace.read()
            
            if '\r' in readStr.decode(errors='ignore'):
                return out
            
            if readStr == b'':
                idxTimeout += 1
            else:
                out = out + readStr.decode(errors='ignore')
                
            if idxTimeout > MaxEmptyCharLimit:
                logging.error('serial interface error: READ_TIMEOUT')
                return ''
    
#------------------------ Configuration Methods -------------------------------            
    
    def set_DataInterface(self, interface=3, Device='SDM', module=None, readACK=True):
        """ Selects the data interface ('Ic<CR>').

        Parameters
        ----------
        Interface : int
        
            ============ ==========================
            interface    description
            ============ ==========================
            0            UART
            1            DEBUG_UART
            3            SPI
            ============ ==========================
            
            default is 3.
            
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.

        Returns
        -------
        bool : True if output interface was successfully selected.
        
        """        
        try:
            interface = int(interface)
        except ValueError:
            logging.error('value error')
            return False
        
        if interface == 0: # UART
            self.DataInterface = interface
            return self.sendCommand("I0", readACK=readACK)
        
        elif interface == 1: # DEBUG_UART
            self.DataInterface = interface
            return self.sendCommand("I1", readACK=readACK)
        
        elif interface == 3: # SPI
            self.DataInterface = interface
            return self.sendCommand("I3", readACK=readACK)

        else:
            return False
        
    def set_RF_frontend(self, RF_Frontend=0, Device='SDM', module=None, readACK=True):
        """ Switch RF front-end on ('1d<CR>').

        Parameters
        ----------
        RF_on : str
            With 1, switch RF front-end on.
            With 0, switch RF front-end off, default is 0 (off).
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the 'ACK' or 'NAK' reply after 'value' was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        RF_min = self._command_library.cmd_lib[Device]['RF Frontend']['min']
        RF_max = self._command_library.cmd_lib[Device]['RF Frontend']['max']
        
        try:
            RF_Frontend = int(RF_Frontend)
        except ValueError:
            logging.error('value error')
            return False
        
        if RF_Frontend == 1:
            self.RF_Frontend = RF_Frontend
            return self.sendCommand('11', readACK=readACK)
        elif RF_Frontend == 0:
            self.RF_Frontend = RF_Frontend
            return self.sendCommand('10', readACK=readACK)
        return False
    
    def set_Sweeps(self, swp=10, Device='SDM', module=None, readACK=True):
        """ Set number of sweeps (``2dddd<CR>``).

        Parameters
        ----------
        swp : int
            Number of sweeps in the range or 1 to 2047, default is 10.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
        
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        Sweeps_min = self._command_library.cmd_lib[Device]['Sweeps']['min']
        Sweeps_max = self._command_library.cmd_lib[Device]['Sweeps']['max']
        
        try:
            swp = int(swp)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if swp < Sweeps_min or swp > Sweeps_max:
                logging.error('setting Sweeps to ' + \
                              str(swp) + ' not possible: out of range')
                return False
        
        self.Sweeps = swp
        return self.sendCommand("2" + str(swp), readACK=readACK)   
        
    def set_ADCSamples(self, ADCsamp=36, Device='SDM', module=None, readACK=True):
        """ Set number of ADC samples per frequency point (``t1ddd<CR>``).

        Parameters
        ----------
        ADCsamp : int
            Number of ADC samples in the range of 1 to 127, default is 36.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.

        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        ADCsamp_cmd = self._command_library.cmd_lib[Device]['ADCsamples']['cmd']
        ADCsamp_min = self._command_library.cmd_lib[Device]['ADCsamples']['min']
        ADCsamp_max = self._command_library.cmd_lib[Device]['ADCsamples']['max']
        
        try:
            ADCsamp = int(ADCsamp)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if ADCsamp < ADCsamp_min or ADCsamp > ADCsamp_max:
                logging.error('setting Samples (ADC) to ' + \
                              str(ADCsamp) + ' not possible: out of range')
                return False
        self.ADCsamples = ADCsamp
        return self.sendCommand(ADCsamp_cmd + str(ADCsamp), readACK=readACK)
        
    def set_FrequencyPoints(self, n=230, Device='SDM', module=None, readACK=True):
        """ Set number of measured frequency points (``3dddd<CR>``).

        Parameters
        ----------
        n : int
            Number of measured frequency points in the range of 1 to 2047, \
            default is 230.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
        
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        FreqP_cmd = self._command_library.cmd_lib[Device]['FreqPoints']['cmd']
        FreqP_min = self._command_library.cmd_lib[Device]['FreqPoints']['min']
        FreqP_max = self._command_library.cmd_lib[Device]['FreqPoints']['max']
        
        try:
            n = int(n)
        except ValueError:
            return False
        else:
            if n < FreqP_min or n > FreqP_max:
                logging.error('setting Frequency Points to ' + \
                              str(n) + ' not possible: out of range')
                return False
        self.FrequencyPoints = n        
        return self.sendCommand(str(FreqP_cmd) + str(n), readACK=readACK)
        
    def set_StartFrequency(self, f=2405, Device='SDM', module=None, readACK=True):
        """ Set start frequency (``4dddd<CR>``).

        Start frequency of the sweep in MHz. If a value > 2418MHz is given it \
        is limited to 2418MHz.

        Parameters
        ----------
        f : int
            Start frequency in the range of 2404 to 2418, default is 2405.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        StartFreq_cmd = self._command_library.cmd_lib[Device]['FreqStart']['cmd']
        StartFreq_min = self._command_library.cmd_lib[Device]['FreqStart']['min']
        StartFreq_max = self._command_library.cmd_lib[Device]['FreqStart']['max']
        
        try:
            f = int(f)
        except ValueError:
            logging.error("Value Error")
            return False
        else:
            if f < StartFreq_min or f > StartFreq_max:
                logging.error('setting Start Frequency to ' + \
                              str(f) + ' not possible: out of range')
                return False
        self.StartFrequency = f
        return self.sendCommand(str(StartFreq_cmd) + str(f), readACK=readACK)

    def set_StepSize(self, ss=330, Device='SDM', module=None, readACK=True):
        """ Set frequency step size in kHz (``5dddd<CR>``).

        Parameters
        ----------
        ss : int
            Step size in the range of 1 to 1000, default is 330.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        StepSize_cmd = self._command_library.cmd_lib[Device]['FreqStep']['cmd']
        StepSize_min = self._command_library.cmd_lib[Device]['FreqStep']['min']
        StepSize_max = self._command_library.cmd_lib[Device]['FreqStep']['max']
        
        try:
            ss = int(ss)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if ss < StepSize_min or ss > StepSize_max:
                logging.error("setting \"Step Size\" to " + \
                              str(ss) + " not possible: out of range")
                return False
        self.StepSize = ss
        return self.sendCommand(str(StepSize_cmd) + str(ss), readACK=readACK)
        
    def set_RxDelay(self, rxD=27, Device='SDM', module=None, readACK=True):
        """ Set Rx delay (``t2ddd<CR>``).
        
        Rx delay in 22.73 ns steps.

        Parameters
        ----------
        rxD : int
            Rx delay in ms in the range or 0 to 255, default is 27.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        RxDelay_min = self._command_library.cmd_lib[Device]['Rx Delay']['min']
        RxDelay_max = self._command_library.cmd_lib[Device]['Rx Delay']['max']
        
        try:
            rxD = int(rxD)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if rxD < RxDelay_min or rxD > RxDelay_max:
                logging.error('setting "Rx Delay" to ' + \
                              str(rxD) + ' not possible: out of range')
                return False
        self.RxDelay = rxD
        return self.sendCommand("t2" + str(rxD), readACK=readACK)
        
    def set_TxLevel(self, txL=40, Device='SDM', module=None, readACK=True):
        """ Set Tx output level (``g1ddd<CR>``).

        Parameters
        ----------
        txL : int
            Tx level in the range or 0 to 63, default is 40.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        TxLevel_cmd = self._command_library.cmd_lib[Device]['Power']['cmd']
        TxLevel_min = self._command_library.cmd_lib[Device]['Power']['min']
        TxLevel_max = self._command_library.cmd_lib[Device]['Power']['max']
        
        try:
            txL = int(txL)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if txL < TxLevel_min or txL > TxLevel_max:
                logging.error("setting \"Tx Level\" to " + \
                              str(txL) + " not possible: out of range")
                return False
        self.TxLevel = txL
        return self.sendCommand(TxLevel_cmd + str(txL), readACK=readACK)
    
    def set_OutputSelect(self, outputSelect=0, Device='SDM', module=None, readACK=True):
        """ Set the data output type (``Bxxx<CR>``).

        Select the datatype(s) to be transferred. The coding is defined \
        bit-wise in hexadecimal representation. If several bits are set, the \
        transmission takes place in several data packets.
        
        On the UART interface, the 24 bit datatype is transmitted by 3 bytes \
        and must be mapped accordingly. On the SPI interface the width is \
        always 32 bit, i.e. 4 bytes. 

        Parameters
        ----------
        outputSelect : int
            OutputSelect in bit-wise coding:
            
            ====== ================================================ ==============
            Bit    description                                      datatype
            ====== ================================================ ==============
            5      Imaginary part raw samples                       24 bit int
            6      Real part raw samples                            24 bit int
            7      Imaginary part raw samples, high-pass filtered   24 bit int
            8      Real part raw samples, high-pass filtered        24 bit int
            9      Real part FFT                                    32 bit int
            10     Imaginary part FFT                               32 bit int
            11     Magnitude FFT                                    32 bit int
            ====== ================================================ ==============

            default is 0.
            
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.

        Returns
        -------
        bool : True if parameter was successfully set.
            
        """  
        
        outputSelect_cmd = self._command_library.cmd_lib[Device]['Output Select']['cmd']
        
        try:
            outputSelect = int(eval(str(outputSelect)))
        except ValueError:
            logging.error('value error')
            return False
        else:
            if Device =='SDM':
                if ((0b1100111111100000 & outputSelect) == 0 \
                    and (outputSelect == 0) == False):
                    logging.error('setting "OutputSelect" to ' + \
                                  str(outputSelect) + ' not possible')
                    return False
            
            elif Device == 'FMCW':
                 if ((0b00011111 & outputSelect) == 0 \
                    and (outputSelect == 0) == False):
                    logging.error('setting "OutputSelect" to ' + \
                                  str(outputSelect) + ' not possible')
                
        self.outputSelect = outputSelect
        return self.sendCommand(str(outputSelect_cmd) + str(hex(outputSelect)[2:]), readACK=readACK)
        
    def set_AntennaMode(self, antennaMode=2, Device='SDM', module=None, readACK=True):
        """ Set antenna switch within the SDM Tx module (``addd<CR>``).

        This command selects the antenna ANT1 or/and ANT2. 

        Parameters
        ----------
        antennaCode : int
            The following antenna codes are defined:
            
            =========== =======================================================
            antennaCode description
            =========== =======================================================
            2           Bi-static (ANT1 is transmitting, ANT2 is receiving)
            5           Bi-static (ANT2 is transmitting, ANT1 is receiving)
            12          ANT 1 (mono-static)
            13          ANT 2 (mono-static)
            =========== =======================================================
            
            default is 2.
        
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set. 
        
        """
        
        antMode_valid_list = self._command_library.cmd_lib[Device]['Antenna Mode']['valid list']
        antMode_cmd = self._command_library.cmd_lib[Device]['Antenna Mode']['cmd']
        
        try:
            antenna = int(antennaMode)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if antenna not in antMode_valid_list:
                logging.error("setting \"Antenna Mode\" to " + str(antenna) + \
                              " not possible: out of range")
                return False
        self.Antenna = antenna
        return self.sendCommand(str(antMode_cmd) + str(antenna), readACK=readACK)
        
    def set_SweepMode(self, swm=0, Device='FMCW', module=None, readACK=True):
        """ Set sweep mode (``xd<CR>``).
        
        ======================================================================
                                        SDM                                            
        ======================================================================
        Parameters
        ----------
        swm : int
            0 is off,
            1 is continuous,
            2 is single-shot,
            default is 0.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if sweep mode was successfully set.
        
        ======================================================================
                                        FMCW                                            
        ======================================================================
        Parameters
        ----------
        swm : int
            0 is off, 
            1 is continuous, 
            2 is single-shot, triggered on falling edge, 
            3 is single-shot, triggered on rising edge,
            4 is query as long as trigger is low,
            5 is Query as long as trigger is high,
            6 is single-shot, untriggerd,
            default is 0.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if sweep mode was successfully set.
        
        """
        try:
            swm = int(swm)
        except ValueError:
            logging.error('value error')
            return False

        if Device == 'SDM':
            sweep_modi_sdm = {
                0: 'x0',
                1: 'x1',
                2: 'x2',
            }
            swm = sweep_modi_sdm.get(swm)
            self.SweepMode = swm
            return self.sendCommand(swm, readACK=readACK)
        
        elif Device == 'FMCW':
            sweep_modi_fmcw = {
                0: 'x0',
                1: 'x1',
                2: 'x2',
                3: 'x3',
                4: 'x4',
                5: 'x5',
                6: 'x6'
            }
            swm = sweep_modi_fmcw.get(swm)
            #print(swm)
            self.SweepMode = swm
            return self.sendCommand(swm, readACK=readACK)
        
        else:
            return False
  
    def set_TxExcite(self, txExcite=115, Device='SDM', module=None, readACK=True):
        """ Set Tx excitation time (``t0ddd<CR>``).
        
        Tx excitation time in 22.73 ns steps. Must be greater than the \
        acoustic length of the TAG.

        Parameters
        ----------
        txExciteTime : int
            set Tx Excitation time in the range or 0 to 511, default is 115.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
        
        Returns
        -------
        bool : True if parameter was successfully set. 
        
        """
        
        TxExcite_min = self._command_library.cmd_lib[Device]['Tx Time']['min']
        TxExcite_max = self._command_library.cmd_lib[Device]['Tx Time']['max']
        
        try:
            txExcite = int(txExcite)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if txExcite < TxExcite_min or txExcite > TxExcite_max:
                logging.error('setting "Tx excitation time" to ' + \
                              str(txExcite) + ' not possible: out of range')
                return False
        self.TxExcite = txExcite
        return self.sendCommand('t0' +  str(txExcite), readACK=readACK)
        

    def set_StartSamplePoint(self, startSP=0, Device='SDM', module=None, readACK=True):
        """ Set start sample point for time domain data (``7dddd<CR>``).

        Parameters
        ----------
        startSP : int
            start point in time domain for FFT-based output, \
            in the range of 0 to 1022, default is 0.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        startSP_cmd = self._command_library.cmd_lib[Device]['DataStart']['cmd']
        startSP_min = self._command_library.cmd_lib[Device]['DataStart']['min']
        startSP_max = self._command_library.cmd_lib[Device]['DataStart']['max']
        
        try:
            startSP = int(startSP)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if startSP < startSP_min or startSP > startSP_max:
                logging.error("setting \"Start frequency point\" to " + 
                              str(startSP) + " not possible: out of range")
                return False
        self.StartFreqPoint = startSP
        return self.sendCommand(str(startSP_cmd) + str(startSP), readACK=readACK)
    
    def set_StopSamplePoint(self, stopSP=1022, Device='SDM', module=None, readACK=True):
        """ Set stop sample point for time domain data (``8dddd<CR>``).

        Parameters
        ----------
        stopSP : int
            stop point in time domain for FFT-based output, \
            in the range of 0 to 1022, default is 1022.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        stopSP_cmd = self._command_library.cmd_lib[Device]['DataStop']['cmd']
        stopSP_min = self._command_library.cmd_lib[Device]['DataStop']['min']
        stopSP_max = self._command_library.cmd_lib[Device]['DataStop']['max']
        
        try:
            stopSP = int(stopSP)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if stopSP < stopSP_min or stopSP > stopSP_max:
                logging.error('setting "Stop frequency point" to ' + 
                              str(stopSP) + " not possible: out of range")
                return False
        self.StopFreqPoint = stopSP
        return self.sendCommand(str(stopSP_cmd) + str(stopSP), readACK=readACK)
    
    def set_IDdecoder(self, IDdecoder_mode=0, Device='SDM', module=None, readACK=True):
        """ Set ID decoder and ID related modes (``ixx<CR>``).

        With setting the ID decoder mode, the TAG ID code and optionally some \
        additional information are send in an ASCII format. The format of \
        this information is variable, depending on the parameter settings.

        Parameters
        ----------
        IDdecoder_mode : 
            IDdecoder_mode in bit-wise coding, sent as two digit hex value.
            
            =================== ================================================
            Bit 1-4, decimal    description                                                   
            =================== ================================================
            0                   ID decoder off (default)
            1                   SCD20 TAG decoder
            2                   SCD16 TAG decoder
            3                   SCD32 TAG decoder
            4                   AVG24 TAG decoder
            5                   SCD50 TAG decoder
            =================== ================================================
            
            Additional information can be read by setting the following bits:
            
            =================== ================================================
            Bit, binary         description                                                   
            =================== ================================================
            6                   Return timestamp
            7                   Temperature output              
            =================== ================================================
            
            example to start the SCD16 decoder with timestamp and temperature \
            readout:
            
                >>> SDMmoduleOBJ = SDMmodule()
                >>> SDMmoduleOBJ.set_IDdecoder( 2 + 0b1000000 + 0b10000000 )
            
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        try:
            IDdecoder_mode_x = hex(eval(str(IDdecoder_mode))).split("x")[1]
        except ValueError:
            logging.error('value error')
            return False
        else:
            if len(IDdecoder_mode_x) < 1 or len(IDdecoder_mode_x) > 2:
                logging.error('setting "IDdecoder_mode" to ' + 
                              str(IDdecoder_mode_x) + " not possible: out of range")
                return False
        self.IDdecoder_mode = eval(str(IDdecoder_mode))
        return self.sendCommand('i' + str(IDdecoder_mode_x), readACK=readACK)
    
#--------------------------- FMCW only methods --------------------------------
    
    def set_Delay(self, Del=27, Device='SDM', module=None, readACK=True):
        
        Delay_cmd = self._command_library.cmd_lib['FMCW']['Delay']['cmd']
        Delay_min = self._command_library.cmd_lib['FMCW']['Delay']['min']
        Delay_max = self._command_library.cmd_lib['FMCW']['Delay']['max']
        
        try:
            Del = int(Del)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if Del < Delay_min or Del > Delay_max:
                logging.error('setting "Delay" to ' + \
                              str(Del) + ' not possible: out of range')
                return False
        self.Delay = Del
        return self.sendCommand(str(Delay_cmd) + str(Del), readACK=readACK)
    
    def set_Gain(self, Gain=2, Device='SDM', module=None, readACK=True):
        
        Gain_cmd = self._command_library.cmd_lib['FMCW']['Gain']['cmd']
        Gain_min = self._command_library.cmd_lib['FMCW']['Gain']['min']
        Gain_max = self._command_library.cmd_lib['FMCW']['Gain']['max']
        
        try:
            Gain = int(Gain)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if Gain < Gain_min or Gain > Gain_max:
                logging.error('setting "Gain" to ' + \
                              str(Gain) + ' not possible: out of range')
                return False
        self.Gain = Gain
        return self.sendCommand(str(Gain_cmd) + str(Gain), readACK=readACK)
    
    def set_ADC(self, ADCsamples=2, Device='SDM', module=None, readACK=True):
        
        ADCsamples_cmd = self._command_library.cmd_lib['FMCW']['ADC']['cmd']
        ADCsamples_min = self._command_library.cmd_lib['FMCW']['ADC']['min']
        ADCsamples_max = self._command_library.cmd_lib['FMCW']['ADC']['max']
        
        try:
            ADCsamples = int(ADCsamples)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if ADCsamples < ADCsamples_min or ADCsamples > ADCsamples_max:
                logging.error('setting "ADC" to ' + \
                              str(ADCsamples) + ' not possible: out of range')
                return False
        self.ADC = ADCsamples
        return self.sendCommand(str(ADCsamples_cmd) + str(ADCsamples), readACK=readACK)
    
    def set_Trigger(self, trigger=10, Device='SDM', module=None, readACK=True):
        """ Set Trigger (``Cddddd<CR>``).
        
        Activates the switching output for ddddd ms.

        Parameters
        ----------
        trigger : int
           activates the switching output in the range of 0 to 29999, default is 10.
        module : optional
            Used in module multiplexing mode, default is None.
        readACK : bool, optional
            When True, receive the `ACK` or `NAK` reply after `value` was sent.
            
        Returns
        -------
        bool : True if parameter was successfully set.
        
        """
        
        trigger_cmd = self._command_library.cmd_lib['FMCW']['Trigger']['cmd']
        trigger_min = self._command_library.cmd_lib['FMCW']['Trigger']['min']
        trigger_max = self._command_library.cmd_lib['FMCW']['Trigger']['max']
        
        try:
            trigger = int(trigger)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if trigger < trigger_min or trigger > trigger_max:
                logging.error('setting "Trigger" to ' + \
                              str(trigger) + ' not possible: out of range')
                return False
        self.Trigger = trigger
        return self.sendCommand(str(trigger_cmd) + str(trigger), readACK=readACK)
    
    def set_IDsnr(self, IDsnr=5, Device='SDM', module=None, readACK=True):
        
        IDsnr_cmd = self._command_library.cmd_lib['FMCW']['IDsnr']['cmd']
        IDsnr_min = self._command_library.cmd_lib['FMCW']['IDsnr']['min']
        IDsnr_max = self._command_library.cmd_lib['FMCW']['IDsnr']['max']
        
        try:
            IDsnr = int(IDsnr)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if IDsnr < IDsnr_min or IDsnr > IDsnr_max:
                logging.error('setting "ID.SNR" to ' + \
                              str(IDsnr) + ' not possible: out of range')
                return False
        self.ID_SNR = IDsnr
        return self.sendCommand(str(IDsnr_cmd) + str(IDsnr), readACK=readACK)
    
    
    def set_FFTlength(self, FFTlen=1, Device='SDM', module=None, readACK=True):
        
        FFTlen_cmd = self._command_library.cmd_lib['FMCW']['FFTlength']['cmd']
        FFTlen_min = self._command_library.cmd_lib['FMCW']['FFTlength']['min']
        FFTlen_max = self._command_library.cmd_lib['FMCW']['FFTlength']['max']
        
        try:
            FFTlen = int(FFTlen)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if FFTlen < FFTlen_min or FFTlen > FFTlen_max:
                logging.error('setting "FFT.length" to ' + \
                              str(FFTlen) + ' not possible: out of range')
                return False
        self.FFT_Length = FFTlen
        return self.sendCommand(str(FFTlen_cmd) + str(FFTlen), readACK=readACK)
    
    
    def set_FFTwindow(self, FFTwin=0, Device='SDM', module=None, readACK=True):
        
        FFTwin_cmd = self._command_library.cmd_lib['FMCW']['FFTwindow']['cmd']
        FFTwin_min = self._command_library.cmd_lib['FMCW']['FFTwindow']['min']
        FFTwin_max = self._command_library.cmd_lib['FMCW']['FFTwindow']['max']
        
        try:
            FFTwin = int(FFTwin)
        except ValueError:
            logging.error('value error')
            return False
        else:
            if FFTwin < FFTwin_min or FFTwin > FFTwin_max:
                logging.error('setting "FFT.window" to ' + \
                              str(FFTwin) + ' not possible: out of range')
                return False
        self.FFT_Window = FFTwin
        return self.sendCommand(str(FFTwin_cmd) + str(FFTwin), readACK=readACK)
 
    def deactivate(self):
        self._serInFace.reset_input_buffer()
        self._serInFace.reset_output_buffer()
        self.set_SweepMode(0)
        self.set_RF_frontend(0)
        
    def activate(self):
        self._serInFace.reset_input_buffer()
        self._serInFace.reset_output_buffer()
        self.set_RF_frontend(1)
 
    def close(self):
        self._serInFace.reset_input_buffer()
        self._serInFace.reset_output_buffer()
        self.set_SweepMode(0)
        self.set_RF_frontend(0)
        self._serInFace.close()
        
        