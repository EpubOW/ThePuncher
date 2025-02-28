import os

def read_env(
    env_value_name:str, 
    default:str|int|float,
):
    val = os.getenv(env_value_name)
    if val is None:
        return default
    return type(default)(val)


# api config
API_HOST  = read_env('API_HOST',  default='0.0.0.0')
API_PORT  = read_env('API_PORT',  default=8000)
API_DEBUG = read_env('API_DEBUG', default=True)

# device config
SERIAL_NAME     = read_env('SERIAL_NAME',     default='COM18')
SERIAL_BAUDRATE = read_env('SERIAL_BAUDRATE', default=115200)
SERIAL_PARITY   = read_env('SERIAL_PARITY',   default='N')
SERIAL_STOPBITS = read_env('SERIAL_STOPBITS', default=1)
SERIAL_BYTESIZE = read_env('SERIAL_BYTESIZE', default=8)
SERIAL_TIMEOUT  = read_env('SERIAL_TIMEOUT',  default=1)

print(API_HOST, API_PORT, API_DEBUG)