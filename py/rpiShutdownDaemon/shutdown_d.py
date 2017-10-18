#!/usr/bin/env python3
import RPi.GPIO as GPIO
import subprocess
import time

LONG_PRESS_S = 3.0
GPIO.setmode(GPIO.BOARD) # Use pin numbering
WAKE_UP_CH = 5 # Pin 05 (GPIO 03)
GPIO.setup(WAKE_UP_CH, GPIO.IN) 
# Configuring pullup is redundant, as Pin 05 has HW pullup.

# Shutdown/reboot system when wake up pin is shorted to GND
GPIO.wait_for_edge(WAKE_UP_CH, GPIO.FALLING)
start = time.time()
longPress = True
while (time.time() - start) < LONG_PRESS_S:
    if GPIO.input(WAKE_UP_CH) == GPIO.HIGH:
        longPress = False
        break
    time.sleep(0.1)
if longPress:
    cmd = "sudo reboot"
else:
    cmd = "sudo shutdown -h now"

subprocess.call(cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

# Redundant before shutdown, but considered good practice
GPIO.cleanup()

