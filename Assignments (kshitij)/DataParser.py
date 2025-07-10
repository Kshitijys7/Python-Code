# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:34:16 2021

@author: Schmelzer
"""
import logging


class DataParser():
    """ Class for parsing the data response of the FMCW Radar. """
    
    def __init__(self, config, dev_name):
        self._config = config
        self._dev_name = dev_name
        self.reset_values()
        
        # Translator of Outputmodi
        self.bit_translater = {
            1    : 'Bit0',      # Bit 0: Realteil FFT
            2    : 'Bit1',      # Bit 1: Imaginärteil FFT
            4    : 'Bit2',      # Bit 2: Raw Samples
            8    : 'Bit3',      # Bit 3: Betrag FFT
            16   : 'Bit4',      # Bit 4: Phase FFT
            32   : 'Bit5',      # Bit 5: Imaginary data Raw Samples
            64   : 'Bit6',      # Bit 6: Real data Raw Samples
            128  : 'Bit7',      # Bit 7: Imaginary data Raw Samples, high-pass filtered
            256  : 'Bit8',      # Bit 8: Real data Raw Samples, high-pass filtered
            512  : 'Bit9',      # Bit 9: Real data (after FFT)
            1024 : 'Bit10',     # Bit 10: Imaginary data (after FFT)
            2048 : 'Bit11'}     # Bit 11: Magnitude (after FFT)
            
        # Config variables
        self._mode_from_config = eval(self._config.get('Reader Settings', 
                                                       'OutputSelect'))
        
    def reset_values(self):
        """Reset data parser attributes"""
        self.data_out = {}                  # dict for output data
        self.data_out['data packet'] = {}   # dict for data packet
        self.data_len = None                # data length of data packet
        self._datagram = 0x00               # contains bitmask of send data set
        self._resp_num = -1                 # counter for number of data sets


    @property
    def datagram(self):
        return self._datagram


    @property
    def mode_from_config(self):
        return self._mode_from_config          

    
    def sort_head(self, byte_arr):
        """A data header has the following structure:
            D<Port><Mode><Number Bytes>
        
        - D: start symbol of fmcw data packet
        - Port: Antenna port at which the measurement was made
        - Mode: Character, the type of data contained is coded bit by bit. The coding corresponds to the "Output
            select “command.
        - Number Bytes: Word, number of the following data bytes 
            (order: LowByte, HighByte)

        Parameters
        ----------
        byte_arr : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        print('BYTE ARR ', byte_arr)
        # start symbol
        if byte_arr[0] == 68:
            self._resp_num += 1
            self.data_out['data packet'][self._resp_num] = {}
            logging.info('Data Start Symbol found')
        
        curr_port = int(byte_arr[1])
        logging.info('Port {} found'.format(curr_port))
        data_mode = int(byte_arr[2])
        self._datagram |= data_mode
        logging.info('Output Mode {} found'.format(data_mode))
        self.data_len = int(byte_arr[3] + 256 * byte_arr[4])
        
        self.data_out['data packet'][self._resp_num]['port'] = curr_port
        self.data_out['data packet'][self._resp_num]['mode'] = data_mode
        self.data_out['data packet'][self._resp_num]['size'] = self.data_len
        self.data_out['data packet'][self._resp_num]['data'] = []
        
        
    def sort_sdm_head(self, byte_arr):
        """
        To be continued

        Parameters
        ----------
        byte_arr : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        if (byte_arr[0] == 0 or 100):
            self._resp_num += 1
            self.data_out['data packet'][self._resp_num] = {}
            logging.info('Data Start Symbol found')
        
        bit_mode = byte_arr[0] + 256 * byte_arr[1]
        self.data_len = byte_arr[2] + 256 * byte_arr[3]
        curr_port = int(byte_arr[8])
        self.chksum = byte_arr[9]
        self._datagram |= bit_mode
        
        self.data_out['data packet'][self._resp_num]['port'] = curr_port
        self.data_out['data packet'][self._resp_num]['mode'] = bit_mode
        self.data_out['data packet'][self._resp_num]['size'] = self.data_len
        self.data_out['data packet'][self._resp_num]['data'] = []
        
    def sort_ident_string(self, ident_str):
        """
        To be continued

        Parameters
        ----------
        ident_str : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if not 'ident' in self.data_out: self.data_out['ident'] = {}
        
        try:      
            curr_port = int(ident_str[1])
            curr_id = ident_str[2:-6]
            signal = -int(ident_str[-6:-4])
            snr = int(ident_str[-4:-2])
            chksum = int(ident_str[-2:],16)
            asciisum = sum(ident_str[0:-2].encode('ascii'))
            checksum_status = not bool((asciisum - chksum)%256)
        
            if checksum_status:
                self.data_out['ident']['port'] = curr_port
                self.data_out['ident']['id'] = curr_id
                self.data_out['ident']['signal'] = signal
                self.data_out['ident']['snr'] = snr
                
            else: 
                self.data_out['ident'] = None
        
        except:
            self.data_out['ident'] = None

            
    def sort_data(self, data_response):
        """Appends data of data packets to the output data""" 
        data = list(data_response)
        self.data_out['data packet'][self._resp_num]['data'] = data

    def get_data_length(self):
        """Returns the length of a data package.
        
        Returns
        -------
        data length : byte 
            
        """
        return self.data_len
    
    def get_checksum(self):
        return self.chksum


    def get_output_data(self):
        """Returns the output data as dict::
            
            output_data (dict)
              |
              |--[key] data packet (str) : [val] (dict)
              |    |
              |    |--[key] X (int with X = consecutive number) : [val] (dict)
              |         |
              |         |--[key] port (str) : [val] Antenna port (int)
              |         |--[key] mode (str) : [val] type of data (str)
              |         |--[key] data (str) : [val] data (list)
              |
              |--[key] ident : [val] (dict)
                   |
                   |--[key] port (str)   : [val] Antenna port (int)
                   |--[key] id (str)     : [val] Ident-String (str)
                   |--[key] signal (str) : [val] Signal [dB] (int)
                   |--[key] snr (str)    : [val] Signal-To-Noise-Ratio (int)


        Returns
        -------
        output data : dict
            Dictionary containing data information
        """
        return self.data_out