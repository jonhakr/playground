#!/usr/bin/env python3
import sys
import traceback
import time
import serial
from serial.threaded import LineReader
from serial.threaded import ReaderThread

class PrintLines(LineReader):
    def connection_made(self, transport):
        super(PrintLines, self).connection_made(transport)
        print('port opened')

    def handle_line(self, data):
        print('> %s' % data)

    def connection_lost(self, exc):
        if exc:
            traceback.print_exc(exc)
        sys.stdout.write('port closed\n')


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

with ReaderThread(em_cli, PrintLines) as protocol:
    protocol.write_line('login user')
    time.sleep(0.2)
    protocol.write_line('sm')
    time.sleep(0.2)
    protocol.write_line('show mote 2')
    time.sleep(1)

em_cli.close()
