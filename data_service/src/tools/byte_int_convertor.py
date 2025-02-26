import binascii

def byte16_to_int(
    byte_value:bytes
):
    return int(binascii.b2a_hex(byte_value), 16)


def int_to_byte16(
    int_value:int
):
    hex_str_value = "{0:x}".format(int(int_value))
    bytes_value = bytes.fromhex(hex_str_value)
    return bytes_value