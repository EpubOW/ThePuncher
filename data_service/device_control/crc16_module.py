def modbus_crc(msg: bytes) -> int:
    crc = 0xFFFF
    for n in range(len(msg)):
        crc ^= msg[n]
        for i in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

def swap_crc(crc: int) -> int:
    return int.from_bytes(crc.to_bytes(2)[::-1])


def check_crc(answer: bytes, mode=None):
    crc = modbus_crc(answer[0:-2])
    if mode == 'MODBUS': crc = swap_crc(crc)
    try:
        equals_values = answer[-2:] == crc.to_bytes(2)
    except Exception as e:
        equals_values = answer[-2:] == crc.to_bytes(2, byteorder='big')
    if not equals_values: print(f'assertFunc: {answer[-2:]}, {crc.to_bytes(2)}')
    
    return equals_values


def add_crc(request: bytes, mode=None):
    crc = modbus_crc(request)
    if mode == 'MODBUS': crc = swap_crc(crc)
    # print(f'crc: {nice_hex(crc.to_bytes(2))}')
    try:
        final_req = request + crc.to_bytes(2)
    except Exception as e:
        final_req = request + crc.to_bytes(2, byteorder='big')
    return final_req

def nice_hex(msg: bytes):
    if len(msg) > 0:
        return ' '.join(f'{b:02X}' for b in msg)
    else: return ''

