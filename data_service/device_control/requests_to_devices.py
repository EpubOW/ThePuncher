import serial
from device_control import crc16_module


def request_to_serial_sensor(request: str, client: serial.Serial, response_len, mode=None, *args):
    """
    request: should be in format '01%02X0105' where %02X for paste arguments
    args: arguments for request, for example s_id:int for check_temp()
    """
    try:
        request = bytes.fromhex(request % args)
    except Exception as e:
        print(e)
        return e
    command = crc16_module.add_crc(request, mode=mode)
    # print('command', command)
    client.write(command)
    # response = client.readall()
    response = client.read(response_len)
    # print(f'response {response}')
    if response:
        assert crc16_module.check_crc(response, mode=mode)
    else:
        client.reset_input_buffer()
        client.reset_output_buffer()
        response = 'EMPTY ANSWER FROM SENSOR'
    return response
