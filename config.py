# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:57:15 2021

@author: Administrator
"""

class Config:
    def __init__(self,):
        self.hop=192               #hop size (window size = 6*hop)
        self.sr=16000              #sampling rate
        self.min_level_db=-100     #reference values to normalize data
        self.ref_level_db=20
        self.shape=24              #length of time axis of split specrograms to feed to generator            
        self.vec_len=128           #length of vector generated by siamese vector
        self.bs = 8                #batch size
        self.delta = 2.            #constant for siamese loss