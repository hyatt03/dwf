#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
   DWF Python Example 2

   Modified by: MURAMATSU Atsushi <amura@tomato.sakura.ne.jp>   
   Revised: 2016-04-21
   Original Author:  Digilent, Inc.
   Original Revision: 10/17/2013

   Requires:                       
       Python 2.7, 3.3 or later
"""

import dwf
import time
import sys

#declare constants
CHANNEL = 0

#print DWF version
print("DWF Version: " + dwf.FDwfGetVersion())

#open device
print("Opening first device...")
dwf_ao = dwf.DwfAnalogOut()

print("Generating sine wave...")
dwf_ao.nodeEnableSet(CHANNEL, dwf_ao.NODE.CARRIER, True)
dwf_ao.nodeFunctionSet(CHANNEL, dwf_ao.NODE.CARRIER, dwf_ao.FUNC.SINE)
dwf_ao.nodeFrequencySet(CHANNEL, dwf_ao.NODE.CARRIER, 10e3)
dwf_ao.nodeAmplitudeSet(CHANNEL, dwf_ao.NODE.CARRIER, 1.41)
dwf_ao.nodeOffsetSet(CHANNEL, dwf_ao.NODE.CARRIER, 1.41)

print("Generating sine wave for 10 seconds...")
dwf_ao.configure(CHANNEL, True)
time.sleep(10)
print("done.")

dwf_ao.close()
