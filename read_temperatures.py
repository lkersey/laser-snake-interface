import serial
import re

ser = serial.Serial('/dev/ttyUSB0', 9600)

# Expected format to extract from the serial port
expected = r"temperature;[0-9];[0-9,.,-]{2,8}" 

while ser.isOpen():
    line = ser.readline()
    found = re.match(expected, line)
    if (found != None):
        data = line.split(';')
        print data

