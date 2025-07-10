# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:56:29 2020

@author: Schmelzer
"""

from configparser import ConfigParser
import os
import logging
import sys

sys.path.append(".")

from ConsoleColors import ConsoleColors as cc

class Config(ConfigParser):
    """Extended configuration parser that can be used to load configuration 
    files from a path and save configuration objects
    
    ...
    
    Attributes
    ----------
    config_path : string
        Path from which the configuration file will be loaded and saved
    
    Methods
    -------
    load_config(cfg_filename)
        Loads config file from specified path to config parser object
    save_config()
        Saves config parser object to configfile at config_path
    """
    def __init__(self):
        super().__init__()
        self.optionxform = str        
        
    def load_config(self, cfg_filename):
        """Loads config file from specified path to config parser object"""
        path_current_directory = os.path.dirname(__file__)
        self.config_path = os.path.join(path_current_directory, \
                                        cfg_filename)
        
        try:
            #print("Config Path = ", self.config_path)
            self.read(self.config_path)
            logging.info(cc.INFO + 'Reading config file: ' + cfg_filename + cc.END)
            
        except IOError:
            logging.error('Config file' + cfg_filename + 'not found!')
            return False
        
    def save_config(self):
        """Saves config parser object to configfile at config_path"""
        with open(self.config_path, 'w') as configfile:
            self.write(configfile)
                

        
            

# #---------------------------------Test-Cases------------------------------#       
# config = Config()
# config.loadConfig('config_saw.ini')
# print(config.sections())
# #print(config.items('DEFAULT'))
# #print(config.items('Reader Settings'))
# print('Keys from items')
# for (key, val) in config.items('Reader Settings'):
#     print(key)
# print('\n')
# print('Keys from direct call')
# for key in config['Reader Settings'].keys():
#     print(key)
# input('')
# #-------------------------------------------------------------------------#