from datetime import datetime
from time import sleep
from winreg import *

from TuyaController import TuyaController


def webcam_loop(controller: TuyaController):
    teams_webcam_status_key = OpenKey(HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam"
                    r"\NonPackaged\C:#Users#douglas.f.silva#AppData#Local#Microsoft#Teams#current#Teams.exe")

    last_state = (QueryValueEx(teams_webcam_status_key, "LastUsedTimeStop"))
    while 1:
        webcam_state = (QueryValueEx(teams_webcam_status_key, "LastUsedTimeStop"))

        if webcam_state != last_state:
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if webcam_state[0] == 0:  # turn on
                print(now_str + " - turned on")
                controller.turn_on()
            else:
                print(now_str + " - turned off")
                controller.turn_off()

            last_state = webcam_state

        sleep(3)


if __name__ == '__main__':
    light_controller = TuyaController(device_name="webcam light")
    webcam_loop(light_controller)
