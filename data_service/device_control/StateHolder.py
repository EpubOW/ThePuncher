import serial

class StateHolder:
    
    instance = None
    __SENSOR_TIMEOUT = 1
    def __init__(self):
        self.serial = serial.Serial('COM18', 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                           bytesize=serial.EIGHTBITS, timeout=self.__SENSOR_TIMEOUT)
    
    @classmethod
    def get_instance(cls):
        if cls.instance == None:
            cls.instance = StateHolder()
        return cls.instance
    
    