from flask_cors import CORS
from flask import Flask
import serial

from .app.puncher_app import PuncherApp
from .config import *
from .services.serial_manager_service import SerialManagerService
from .device_clients.puncher_client import PuncherClient
#flask
flask_app = Flask(
    __name__
)

# cors
flask_app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(
    flask_app, 
    supports_credentials=True, 
    resources={r"*": {"origins": "*"}}
)

# serial
serial_port = serial.Serial( # TODO: move to class with on startup init
    port     = SERIAL_NAME, 
    baudrate = SERIAL_BAUDRATE, 
    parity   = SERIAL_PARITY, 
    stopbits = SERIAL_STOPBITS,
    bytesize = SERIAL_BYTESIZE, 
    timeout  = SERIAL_TIMEOUT
    )

serial_manager = SerialManagerService(
    ser=serial_port
)

# devices
puncher_client = PuncherClient(
    dev_address=b'\x01',
    serial_manager=serial_manager
)

def on_startup_init():
    pass

app = PuncherApp(
    flask_app       = flask_app,
    on_startup_init = on_startup_init,
    host            = API_HOST,
    port            = API_PORT,
    api_debug_mode  = API_DEBUG
)