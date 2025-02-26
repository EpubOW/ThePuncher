from device_control.MainController import MainController
from device_control import crc16_module
import time
from datetime import datetime
# from device_control.crc16_module import print_nice_hex

class MainProcessing():
    mode = 'MODBUS'
    route = ''

    def __init__():
        pass
    
    @classmethod
    def printTest(cls):
        # lastTemp = None
        # lastDatetime = datetime.now()
        # while True:
        #     _, _, tempNow, _, datetimeNow  = cls.getData()
        #     if tempNow != lastTemp:
        #         lastTemp = tempNow
        #         lastDatetime = datetimeNow
        #     elif (datetimeNow - lastDatetime).total_seconds() > 5:
        #         print('STOP', lastTemp)
        #         break
        #     time.sleep(0.01)
        cls.cylinderMovementUp()

    @classmethod
    def getData(cls):
        '''
        mode: влияет на расстановку байт в CRC: None - обычная, 'MODBUS' - обратная
        '''
        request = '010380000005'
        pos, volt, temp, inputs = None, None, None, None
        response = MainController.send_request(request, mode=cls.mode)
        if type(response) is bytes:
            # print(crc16_module.nice_hex(response))
            pos = (response[3] << 24) + (response[4] << 16) + (response[5] << 8) + response[6]
            if pos >= 2**31: pos -= 2**32
            volt = ((response[7] << 8) + response[8]) / 1000
            temp = (response[9] << 8) + response[10]
            inputs = (response[11] << 8) + response[12]
            print(f'pos: {pos} импульсов/{pos / 19.98:.2f} мм, volt: {volt}, temp: {temp}, inputs: {inputs}')
        return [pos, volt, temp, inputs, datetime.now()]

    @classmethod
    def cylinderMovementUp(cls):
        request='010600080004'
        response = MainController.send_request(request, mode=cls.mode)
        if type(response) is bytes:
            if response[1].to_bytes(1) == b'\x86': print('incorrect request')
            else: print(crc16_module.nice_hex(response))
    
    @classmethod
    def cylinderMovementDown(cls):
        request='010600080001'
        response = MainController.send_request(request, mode=cls.mode)
        if type(response) is bytes:
            if response[1].to_bytes(1) == b'\x86': print('incorrect request')
            else: print(crc16_module.nice_hex(response))

    @classmethod
    def clearPosition(cls):
        request='010600070001'
        response = MainController.send_request(request, mode=cls.mode)
        if type(response) is bytes:
            if response[1].to_bytes(1) == b'\x86': print('incorrect request')
            else: print(crc16_module.nice_hex(response))
            
    @classmethod
    def reboot(cls):
        request='010600070002'
        response = MainController.send_request(request, mode=cls.mode)
        if type(response) is bytes:
            if response[1].to_bytes(1) == b'\x86': print('incorrect request')
            else: print(crc16_module.nice_hex(response))