#!/usr/bin/env python3
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BOARD) # Use pin numbering
WAKE_UP_CH = 5 # Pin 05 (GPIO 03)
GPIO.setup(WAKE_UP_CH, GPIO.IN) 
# Configuring pullup is redundant, as Pin 05 has HW pullup.

# Shutdown system when wake up pin is shorted to GND
GPIO.wait_for_edge(WAKE_UP_CH, GPIO.FALLING)
subprocess.call("sudo shutdown -h now",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)

# Redundant before shutdown, but considered good practice
GPIO.cleanup()

