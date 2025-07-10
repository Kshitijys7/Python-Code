# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:54:52 2020

@author: Schmelzer
"""

class CmdLibrary:
    def __init__(self):
        self.cmd_lib = {
            'FMCW':{
                'RF Frontend': {
                    'cmd': '1',
                    'min': 0,
                    'max': 1,
                    'default': 0},
                'Sweeps': {
                    'cmd': '2',
                    'min': 1,
                    'max': 255,
                    'default': 20},
                'FreqPoints': {
                    'cmd': '3',
                    'min': 1,
                    'max': 511,
                    'default': 240},
                'FreqStart': {
                    'cmd': '4',
                    'min': 2400,
                    'max': 2483,
                    'default': 2420},
                'FreqStep': {
                    'cmd': '5',
                    'min': 0,
                    'max': 1857,
                    'default': 200},
                'Gain': {
                    'cmd': '6',
                    'min': 0,
                    'max': 8,
                    'default': 2},
                'DataStart': {
                    'cmd': '7',
                    'min': 0,
                    'max': 511,
                    'default': 172},
                'DataStop': {
                    'cmd': '8',
                    'min': 0,
                    'max': 511,
                    'default': 482},
                'Delay': {
                    'cmd': '9',
                    'min': 0,
                    'max': 199,
                    'default': 4},
                'ADC': {
                    'cmd': 'A',
                    'min': 0,
                    'max': 127,
                    'default': 20},
                'Output Select': {
                    'cmd': 'B',
                    'min': 0x00,
                    'max': 0x1F,
                    'default': 0},
                'Antenna Mode': {
                    'cmd': 'a',
                    'valid list': [0,1,255],
                    'default': 0},
                'Trigger': {
                    'cmd': 'C',
                    'min': 0,
                    'max': 29999,},
                'Power': {
                    'cmd': 'w',
                    'min': 0,
                    'max': 99,
                    'default': 75},
                'ID': {
                    'cmd': 'i',
                    'valid list': [0,1,2],
                    'default': 0},
                'FFTwindow': {
                    'cmd': 'm1',
                    'min': 0,
                    'max': 3,
                    'default': 0},
                'IDsnr': {
                    'cmd': 'm2',
                    'min': 0,
                    'max': 9,
                    'default': 5},
                'FFTlength': {
                    'cmd': 'm3',
                    'min': 0,
                    'max': 2,
                    'default': 1},
                },
            'SDM':{
                'RF Frontend': {
                    'cmd': '1',
                    'min': 0,
                    'max': 1,
                    'default': 0},
                'Sweeps': {
                    'cmd': '2',
                    'min': 1,
                    'max': 2047,
                    'default': 10},
                'FreqPoints': {
                    'cmd': '3',
                    'min': 1,
                    'max': 1022,
                    'default': 255},
                'ADCsamples': {
                    'cmd': 't1',
                    'min': 1,
                    'max': 127,
                    'default': 36},
                'FreqStart': {
                    'cmd': '4',
                    'min': 2404,
                    'max': 2418,
                    'default': 2405},
                'FreqStep': {
                    'cmd': '5',
                    'min': 0,
                    'max': 1000,
                    'default': 385},
                'DataStart': {
                    'cmd': '7',
                    'min': 0,
                    'max': 1022,
                    'default': 300},
                'DataStop': {
                    'cmd': '8',
                    'min': 0,
                    'max': 1022,
                    'default': 930},
                'Antenna Mode': {
                    'cmd': 'a',
                    'valid list': [2,5,12,13,16,17,18,19,20],
                    'default': 12},
                'Output Select': {
                    'cmd': 'B',
                    'min': 0,
                    'max': 0xFFFF,
                    'default': 0},
                'Power': {
                    'cmd': 'g1',
                    'min': 0,
                    'max': 63,
                    'default': 50},
                'Tx Time': {
                    'cmd': 't0',
                    'min': 0,
                    'max': 511,
                    'default': 115},
                'Rx Delay': {
                    'cmd': 't2',
                    'min': 0,
                    'max': 255,
                    'default': 27},
                'Tag': {
                    'cmd': 'i',
                    'min': 0,
                    'max': 3,
                    'default': 0},
                'Sweep Mode': {
                    'cmd': 'x',
                    'valid list': [0,1,2],
                    'default': 0},
                'Data Interface': {
                    'cmd': 'I',
                    'valid list': [0,1,3,4],
                    'default': 0},
                }}
        
    def getKey(self, Devicename, Keyname, Value):
        return self.cmd_lib[Devicename][Keyname].get(Value)
    
    def get_keyname(self, device_name, key_name):
        return self.cmd_lib[device_name][key_name]
    
# Lib = CmdLibrary()
# print(Lib.getKey('SDM','Antenna Mode','valid list'))
# input('')