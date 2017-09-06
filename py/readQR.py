#!/usr/bin/env python3
from PIL import Image
import zbarlight

filePath = './qrcode.png'
with open(filePath, 'rb') as imageFile:
    image = Image.open(imageFile)
    image.load()

qrCode = zbarlight.scan_codes('qrcode', image)
print('QR code: %s' % qrCode)
