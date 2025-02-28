from src.services.serial_manager_service import SerialManagerService
from src.tools.byte_int_convertor import *
from src.tools.byte_print_tool import *

import serial

class PuncherClient:
    
    __MOVE_REG_ADDRESS    = b'\x00\x08'
    __ADDER_REG_ADDRESS   = b'\x00\x07'
    __READ_REG_ADDRESS    = b'\x80\x00'
    
    __READ_REG_BYTE_SIZE  = b'\x00\x05'
    
    __MOVE_ANSWER_SIZE = 8
    __READ_ANSWER_SIZE = 15
    
    __MOVE_UP_COMMAND_DATA        = b'\x00\x00'
    __MOVE_DOWN_COMMAND_DATA      = b'\x00\x01'
    __RESET_MOVEMENT_COMMAND_DATA = b'\x00\x01'
    __RESET_MODULE_COMMAND_DATA   = b'\x00\x02'
    
    
    
    RESERVE_DOWN_INPUT = 0
    RESERVE_UP_INPUT   = 1
    DOWN_INPUT         = 2
    UP_INPUT           = 3
    
    __ENCODER_KOEF = 19.98
        
    def __init__(
        self,
        dev_address:bytes,
        serial_manager:SerialManagerService
        
    ):
        self.__serial_manager = serial_manager
        self.__dev_address = dev_address
        
    
    def read_data(
        self,
    ):
        response = self.__serial_manager.send_modbus_read_command(
            self.__dev_address,
            self.__READ_REG_ADDRESS,
            self.__READ_REG_BYTE_SIZE,
            self.__READ_ANSWER_SIZE
        )
        deepnes      = byte16_to_int(response[3:7]) / self.__ENCODER_KOEF
        voltage      = byte16_to_int(response[7:9]) / 1000
        temperature  = byte16_to_int(response[9:11])
        inputs_value = byte16_to_int(response[11:13])
        return deepnes, voltage, temperature, inputs_value
    
    def cylinder_move_up(
            self,
    ):
        response = self.__serial_manager.send_modbus_write_command(
            self.__dev_address,
            self.__MOVE_REG_ADDRESS,
            self.__MOVE_UP_COMMAND_DATA,
            self.__MOVE_ANSWER_SIZE
        )
        return response
    
    def cylinder_move_down(
            self,
    ):
        response = self.__serial_manager.send_modbus_write_command(
            self.__dev_address,
            self.__MOVE_REG_ADDRESS,
            self.__MOVE_DOWN_COMMAND_DATA,
            self.__MOVE_ANSWER_SIZE
        )
        return response

    def reset_movement(
            self,
    ):
        response = self.__serial_manager.send_modbus_write_command(
            self.__dev_address,
            self.__ADDER_REG_ADDRESS,
            self.__RESET_MOVEMENT_COMMAND_DATA,
            self.__MOVE_ANSWER_SIZE
        )
        return response
    
    def reset_module(
            self,
    ):
        response = self.__serial_manager.send_modbus_write_command(
            self.__dev_address,
            self.__ADDER_REG_ADDRESS,
            self.__RESET_MODULE_COMMAND_DATA,
            self.__MOVE_ANSWER_SIZE
        )
        return response