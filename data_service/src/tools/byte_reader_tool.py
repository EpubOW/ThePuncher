import serial
from time import time

class SerialSizeException(Exception):
    pass

def byte_reader(
    ser: serial.Serial, 
    size = 9
):
    buf = b''
    while True:
        res = ser.read()
        if res:
            buf += res
            if len(buf) > 72:
                ser.close()
                ser.open()
                return len(buf), buf
            continue
        break 
    return len(buf), buf

