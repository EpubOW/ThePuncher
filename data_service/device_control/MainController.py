import serial.serialutil
from device_control.StateHolder import StateHolder
from device_control import requests_to_devices
import serial
from .crc16_module import *

class MainController():
    correct_len = 15

    def __init__():
        pass

    @classmethod
    def send_request(cls, request, mode=None):
        response = 'potential error'
        try:
            # print('\ntry to request')
            client = StateHolder.get_instance().serial
            
            response = requests_to_devices.request_to_serial_sensor(
                request,
                client,
                cls.correct_len,
                mode=mode)
            # print(f'get response \n{response}')

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
        
    