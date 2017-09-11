#!/usr/bin/env python3
import cv2
from PIL import Image
import zbarlight
import time
import serial
import re


def compareMAC(mac1, mac2):
    if mac1 and mac2:
        if mac1 == mac2:
            print("MATCH: %s" % mac1)
        else:
            print("NO-MATCH: %s =! %s" % (mac1, mac2))


macFind = re.compile('([0-9a-f]{2}(?:-[0-9a-f]{2}){7})', re.IGNORECASE)

em_cli = serial.Serial(
    port='/dev/ttyUSB2',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5
    )
em_cli.isOpen()
print(em_cli.name)

cv2.namedWindow('QR Camera')
cap = cv2.VideoCapture(0) # first indexed webcam
scanCode = False
code_scanned = ""
code_read = ""

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display frame
    cv2.imshow('QR Camera', frame)

    if scanCode:
        # Create grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Build image and scan for QR code
        image = Image.fromarray(gray)
        qrcode = zbarlight.scan_codes('qrcode', image)

        # Display resulting frame and print any QR code
        if qrcode:
            scanCode = False
            code_scanned = qrcode[0].decode('utf-8').replace(' ', ':')
            print("Scanned QR Code: %s" % code_scanned)
            compareMAC(code_scanned, code_read)

    keyPress = cv2.waitKey(10) & 0xFF
    if keyPress == ord('q'):
        # Exit
        break
    elif keyPress == ord('s'):
        # Scan code
        scanCode = True
    elif keyPress == ord('r'):
        # Read MAC address
        em_cli.write(b'login user\r\n')
        time.sleep(0.2)
        em_cli.flushInput()
        em_cli.write(b'show mote 2r\n')
        time.sleep(1)
        while em_cli.in_waiting > 0:
            readStr = em_cli.readline().decode('utf-8')
            if 'mac' in readStr:
                macStr = re.findall(macFind, readStr)
                code_read = macStr[0].replace('-', ':')
                print("Read MAC address: %s" % code_read)
                compareMAC(code_scanned, code_read)

cap.release()
cv2.destroyAllWindows()
