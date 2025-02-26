from src.tools.serial_protocol_tools import *
from src.tools.crc16module import *
from src.tools.byte_reader_tool import *

class SerialManagerService:
    
    def __init__(
        self,
        ser:serial.Serial
    ):
        self.__serial = ser
    
    
    __WRITE_COMMAND = b'\x06'
    __READ_COMMAND  = b'\x03'

    def send_modbus_write_command(
        self,
        dev_address:bytes,
        data_address:bytes,
        data:bytes,
        responce_size:int
    ):
        msg = data_address + data
        answer_size, answer = send_message(
            self.__serial,
            dev_address,
            self.__WRITE_COMMAND,
            msg,
            responce_size
        )
        
        check_answer(
            size            = answer_size, 
            answer          = answer, 
            max_answer_size = responce_size
        )
        return answer

    def send_modbus_read_command(
        self,
        dev_address:bytes,
        data_address:bytes,
        data_size:bytes,
        responce_size:int
    ):
        msg = data_address + data_size
        answer_size, answer = send_message(
            self.__serial,
            dev_address,
            self.__READ_COMMAND,
            msg,
            responce_size
        )

        check_answer(
            size            = answer_size, 
            answer          = answer, 
            max_answer_size = responce_size
        )
        return answer
    
        

__all__ = ['SerialManagerService']