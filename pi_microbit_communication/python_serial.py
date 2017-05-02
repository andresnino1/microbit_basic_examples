# This file goes on the pc you are connecting to the microbit.  Only tested on raspberry pi.
import serial
import time

PORT = "/dev/ttyACM0"
BAUD = 115200
s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

while True:
    s.write("hello".encode('UTF-8'))
    time.sleep(5)
