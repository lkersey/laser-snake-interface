import re
import serial
import sql
import time 

ser = serial.Serial('/dev/ttyUSB0', 9600)

# Expected format to extract from the serial port
expected = r"temperature;[0-9];[0-9,.,-]{2,8}" 

#print sql.get_temperatures(1, 100)


while ser.isOpen():
    line = ser.readline()
    m = re.match(expected, line)
    if (m != None):
        found = m.group(0)
        data = found.split(';')
        print data
        sql.write_temperature(int(data[1]), float(data[2]), time.time())
        

