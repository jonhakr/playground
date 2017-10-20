#!/usr/bin/env python3
import cv2
from PIL import Image
import zbarlight
import time
import serial
import re


def printHelp():
    print('######')
    print('# matchMac.py')
    print('# - Match MAC address from QR code and via Embedded Manager CLI')
    print('> h \t - Show this help')
    print('> s \t - Scan MAC address from QR Code')
    print('> r \t - Read MAC address via EM CLI')
    print('> q \t - Quit')
    print('######')


def compareMAC(mac1, mac2):
    if mac1 and mac2:
        if mac1 == mac2:
            print("MATCH: %s" % mac1)
        else:
            print("NO-MATCH: %s =! %s" % (mac1, mac2))


em_cli = serial.Serial(
    port='/dev/ttyUSB2',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5
    )
if not em_cli.isOpen(): # Should replace with try/catch
    print("Failed to open EM CLI on %s" % em_cli.name)
    quit()
print("Opened EM CLI on %s" % em_cli.name)

cv2.namedWindow('QR Camera')
cap = cv2.VideoCapture(0) # first indexed webcam
if not cap.isOpened():
    print("Failed to open camera index 0")
    quit()

macFind = re.compile('([0-9a-f]{2}(?:-[0-9a-f]{2}){7})', re.IGNORECASE)
scanCode = False
code_scanned = ""
code_read = ""

printHelp()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display frame
    cv2.imshow('QR Camera', frame)

    if scanCode:
        # Scan frame for QR code until one is decoded
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        image = Image.fromarray(gray)
        qrcode = zbarlight.scan_codes('qrcode', image)
        if qrcode:
            scanCode = False
            code_scanned = qrcode[0].decode('utf-8').replace(' ', ':')
            print("Scanned QR Code: %s" % code_scanned)
            compareMAC(code_scanned, code_read)

    keyPress = cv2.waitKey(10) & 0xFF
    if keyPress == ord('q'):
        # Exit
        break
    elif keyPress == ord('h'):
        printHelp()
    elif keyPress == ord('s'):
        # Scan code
        scanCode = True
    elif keyPress == ord('r'):
        # Read MAC address
        em_cli.write(b'login user\r\n')
        time.sleep(0.2)
        em_cli.flushInput() # Flush 2 empty lines received after login
        em_cli.write(b'show mote 2r\n')
        time.sleep(1) # Wait to receive whole message
        while em_cli.in_waiting > 0:
            readStr = em_cli.readline().decode('utf-8')
            if 'mac' in readStr:
                macStr = re.findall(macFind, readStr)
                code_read = macStr[0].replace('-', ':')
                print("Read MAC address: %s" % code_read)
                compareMAC(code_scanned, code_read)

                # Flush the remaining lines in buffer
                em_cli.flushInput()
                break

cap.release()
cv2.destroyAllWindows()
