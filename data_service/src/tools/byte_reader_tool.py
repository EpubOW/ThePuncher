import serial

class SerialSizeException(Exception):
    pass

def byte_reader(
    ser: serial.Serial, 
    size: int
):
    buf = ser.read(size)
    return len(buf), buf

def byte_reader_without_size(
        ser: serial.Serial
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

