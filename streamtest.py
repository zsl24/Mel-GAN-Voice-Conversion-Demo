# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 15:09:49 2021

@author: Administrator
"""

import argparse
import sys
import sounddevice as sd
import numpy  # Make sure NumPy is loaded before it is used in the callback
from test import voice_conversion

assert numpy  # avoid "imported but unused" message (W0611)


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, outdata, frames, time, status):
    if status:
        print(status) 
    buffer = indata[:]
    buffer = voice_conversion(buffer)
    outdata[:] = buffer

try:
    with sd.Stream(blocksize = 16384,
                   samplerate= 16000, 
                   channels=1, callback=callback):
        print('#' * 80)
        print('press Return to quit')
        print('#' * 80)
        input()
except KeyboardInterrupt:
    sys.exit('\nInterrupted by user')