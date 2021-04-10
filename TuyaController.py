import credentials
from tuyaha import TuyaApi


class TuyaController:
    def __init__(self, device_name):
        username = credentials.login['username']
        password = credentials.login['password']
        country_code = 'us'
        api = TuyaApi()  # https://github.com/PaulAnnekov/tuyaha
        devices = api.init(username=username, password=password, countryCode=country_code)
        for dev in devices:
            dev_name = dev.obj_name
            if dev_name == device_name:
                self.device = dev

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()
