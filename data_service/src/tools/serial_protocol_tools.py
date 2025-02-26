import binascii

from .byte_reader_tool import *
from .crc16module import *

from loguru import logger

class ModbusException(Exception):
    pass


    

def send_message(
    ser, 
    address:bytes,
    command:bytes,
    msg:bytes,
    responce_size:int
):
    message = address + command + msg
    message_crc = add_crc(message)
    logger.info(f'send: {message_crc}')
    res = ser.write(message_crc)
    ser.flush()
    size, answer = byte_reader(ser, responce_size)
    logger.info(f'read: {answer}')
    return size, answer
    
def check_answer(
    size, 
    answer, 
    max_answer_size = 10
):
    if size < 3:
        raise SerialSizeException('Слишкий малый размер ответа')
    if size > max_answer_size:
        raise SerialSizeException('Слишкий большой размер ответа')
    
    check_crc(answer)
    
    if answer[1:2] > b'\x80':
        if answer[2:3] == b'\x01':
            raise ModbusException('Принятый код функции не может быть обработан \n    - code: 1')
        if answer[2:3] == b'\x02':
            raise ModbusException('Адрес данных, указанный в запросе, недоступен \n    - code: 2')
        if answer[2:3] == b'\x03':
            raise ModbusException('Значение, содержащееся в поле данных запроса, является недопустимой величиной \n    - code: 3')
        if answer[2:3] == b'\x04':
            raise ModbusException('Невосстанавливаемая ошибка имела место, пока ведомое устройство пыталось выполнить затребованное действие \n    - code: 4')
        if answer[2:3] == b'\x05':
            raise ModbusException('Ведомое устройство приняло запрос и обрабатывает его, но это требует много времени. Этот ответ предохраняет ведущее устройство от генерации ошибки тайм-аута \n    - code: 5')
        if answer[2:3] == b'\x06':
            raise ModbusException('Ведомое устройство занято обработкой команды. Ведущее устройство должно повторить сообщение позже, когда ведомое освободится \n    - code: 6')
        if answer[2:3] == b'\x07':
            raise ModbusException(f'Ведомое устройство не может выполнить программную функцию, заданную в запросе. Этот код возвращается для неуспешного программного запроса, использующего функции с номерами 13 или 14. Ведущее устройство должно запросить диагностическую информацию или информацию об ошибках от ведомого \n    - code: 7')
        if answer[2:3] == b'\x08':
            raise ModbusException(f'Ведомое устройство при чтении расширенной памяти обнаружило ошибку паритета. Ведущее устройство может повторить запрос, но обычно в таких случаях требуется ремонт \n    - code: 8')
        if answer[2:3] == b'\x0A':
            raise ModbusException(f'Шлюз неправильно настроен или перегружен запросами \n    - code: 9')
        if answer[2:3] == b'\x0B':
            raise ModbusException(f'Slave устройства нет в сети или от него нет ответа \n    - code: 10')
        raise ModbusException(f'Неопознанная ошибка: Неизвестный ответ устройства \n    - code: {int(binascii.b2a_hex(answer[2]), 16)}')