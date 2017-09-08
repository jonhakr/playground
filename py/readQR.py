#!/usr/bin/env python3
import cv2
from PIL import Image
import zbarlight


cv2.namedWindow('QR Camera')
cap = cv2.VideoCapture(0) # first indexed webcam

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Create grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Build image and scan for QR code
    image = Image.fromarray(gray)
    qrcode = zbarlight.scan_codes('qrcode', image)

    # Display resulting frame and print any QR code
    cv2.imshow('QR Camera', frame)
    if qrcode:
        print(qrcode)

    # Exit on keypress 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
