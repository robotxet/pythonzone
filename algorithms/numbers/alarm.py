"""
Alarm clock:
simple timer that plays sound after a particular time
"""

import os
import time

def beep():
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.5, 1000))

delay = raw_input("Enter timer in seconds: ")
time.sleep(int(delay))
for i in range(3):
    beep()
