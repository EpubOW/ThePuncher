from device_control.MainController import MainController
# from device_control.crc16_module import print_nice_hex

class MainProcessing():
    mode = 'MODBUS'
    route = ''

    def __init__():
        pass
    
    @classmethod
    def printTest(cls):
        # MainController.getData(cls.route, mode=cls.mode)
        # MainController.clearPosition(cls.route, mode=cls.mode)
        # MainController.getData(cls.route, mode=cls.mode)

        MainController.cylinderMovementUp(cls.route, mode=cls.mode)
        # MainController.getData(cls.route, mode=cls.mode)