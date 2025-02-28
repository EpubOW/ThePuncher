from .static_holder import StaticHolder
from src.device_clients.puncher_client import PuncherClient

class MeasurementService:
    def __init__(
            self,
            puncer_client:PuncherClient,
            static_holder:StaticHolder
        ):
        pass

    def on_startup_init(self):
        pass

    def make_measurements(self):
        pass