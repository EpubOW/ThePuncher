import serial.serialutil
from device_control.StateHolder import StateHolder
from device_control import requests_to_devices
import serial
from device_control import crc16_module

class MainController():
    correct_len = 15

    def __init__():
        pass

    @classmethod
    def send_request(cls, request, mode=None):
        response = 'potential error'
        try:
            print('\ntry to request')
            client = StateHolder.get_instance().serial
            
            response = requests_to_devices.request_to_serial_sensor(
                request,
                client,
                cls.correct_len,
                mode=mode)
            print(f'get response \n{response}')

            # if type(response) is bytes:
            #     volt, temp = cls.check_temp(response, route)
            # else:
            #     print(response)
        except AssertionError:
            print('\nERROR ANSWER: response not assert')
            print('clear_buffer', client.read_all()) 
        except serial.serialutil.SerialException as e:
            print(f'serial Exception: {e}')
        except Exception as e:
            print(e)
        return response


    @classmethod
    def getData(cls, route, mode=None):
        '''
        mode: влияет на расстановку байт в CRC: None - обычная, 'MODBUS' - обратная
        '''
        request = '010380000005'
        pos, volt, temp, inputs = None, None, None, None
        response = cls.send_request(request, mode=mode)
        if type(response) is bytes:
            print(crc16_module.nice_hex(response))
            pos = (response[3] << 24) + (response[4] << 16) + (response[5] << 8) + response[6]
            if pos >= 2**31: pos -= 2**32
            volt = ((response[7] << 8) + response[8]) / 1000
            temp = (response[9] << 8) + response[10]
            inputs = (response[11] << 8) + response[12]
            print(f'pos: {pos} импульсов/{pos / 19.98:.2f} мм, volt: {volt}, temp: {temp}, inputs: {inputs}')
        
    @classmethod
    def cylinderMovementUp(cls, route, mode=None):
        request='010600080000'
        response = cls.send_request(request, mode=mode)
        if type(response) is bytes:
            if response[1].to_bytes(1) == b'\x86': print('incorrect request')
            else: print(crc16_module.nice_hex(response))
    
    @classmethod
    def cylinderMovementDown(cls, route, mode=None):
        request='010600080001'
        response = cls.send_request(request, mode=mode)
        if type(response) is bytes:
            if response[1].to_bytes(1) == b'\x86': print('incorrect request')
            else: print(crc16_module.nice_hex(response))

    @classmethod
    def clearPosition(cls, route, mode=None):
        request='010600070001'
        response = cls.send_request(request, mode=mode)
        if type(response) is bytes:
            if response[1].to_bytes(1) == b'\x86': print('incorrect request')
            else: print(crc16_module.nice_hex(response))
            
    @classmethod
    def reboot(cls, route, mode=None):
        request='010600070002'
        response = cls.send_request(request, mode=mode)
        if type(response) is bytes:
            if response[1].to_bytes(1) == b'\x86': print('incorrect request')
            else: print(crc16_module.nice_hex(response))