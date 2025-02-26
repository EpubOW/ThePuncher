from flask import Flask
from collections.abc import Callable

class PuncherApp:
    
    def __init__(
        self,
        flask_app:Flask,
        on_startup_init:Callable,
        host:str,
        port:str,
        api_debug_mode:bool        = False
        
    ):
        self.__flask_app = flask_app
        
        self.__on_startup_init = on_startup_init
        self.__host            = host
        self.__port            = port
        self.api_debug_mode    = api_debug_mode
        
    def start_app(self):
        self.__on_startup_init()
        with self.__flask_app.app_context():
            self.__flask_app.run(
                host  = self.__host,
                port  = self.__port,
                debug = self.api_debug_mode
            )
        
        
        