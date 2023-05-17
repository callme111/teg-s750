#!/usr/bin/env python3

import os
import serial
import sys

from time import sleep
from xmodem import XMODEM1k


ESC_TO_STOP_AUTOBOOT = "Hit Esc key to stop autoboot: "
PROMPT = "RTL9300#"
YMODEM_READY = "## Ready for binary (ymodem) download to 0x82000000 at 115200 bps..."

ESC = bytes(chr(27), "ascii")
LOADY = "loady 0x82000000\n".encode("ascii")
BOOTM = "bootm 0x82000000\n".encode("ascii")


def read_all(ser):
    to_read = ser.in_waiting
    if to_read > 0:
        print(ser.read(to_read).decode('ascii'), end="")


def write_response(ser, what):
    sleep(0.1)
    for i in range(len(what)):
        b = what[i:i+1]
        read_all(ser)
        ser.write(b)

class MyModem:

    def __init__(self, ser, filename):
        self.ser = ser
        self.size = os.path.getsize(filename)
        self.filename = filename
        self.sent = 0
        self.last_sent = 0

    def getc(self, size, timeout=8):
        gbytes = self.ser.read(size)
        return gbytes or None


    def putc(self, data, timeout=8):
        pbytes = self.ser.write(data)
        self.sent += pbytes
        if self.sent - self.last_sent > 10000:
            self.last_sent = self.sent
            print(f'Sent {self.sent} ({self.sent*100/self.size:5.2f}%)')

        return pbytes or None

    def transfer(self):
        with open(self.filename, "rb") as file:
            modem = XMODEM1k(self.getc, self.putc)
            modem.send(file)


def transfer_and_run(port, baudrate, filename):

    transferred = False
    
    with serial.Serial(port, baudrate=baudrate) as ser:

        print("Ready, power up switch.\n")
        # ser.write(b"\n")

        line = ""
        while True:
            read = ser.read().decode("ascii")
            print(read, end="")
            
            line += read
            if line.endswith("\n"):
                line = ""

            if line.startswith(ESC_TO_STOP_AUTOBOOT):
                line = ""
                write_response(ser, ESC)
            
            elif line.startswith(PROMPT):
                line = ""
                if not transferred:
                    write_response(ser, LOADY)
                else:
                    write_response(ser, BOOTM)

            elif line.startswith(YMODEM_READY):
                line = ""
                ser.read_until()

                m = MyModem(ser, filename)
                m.transfer()
                transferred = True


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} port filename")
        sys.exit(1)
    
    transfer_and_run(sys.argv[1], 115200, sys.argv[2])

