
import pyautogui

from autoclick.modules.bombcrypto.log import bcoin_log_file

class Chest:
    def __init__(self) -> None:
        self.close_chest_button = (968, 313)
        self.open_chest_button = (1094, 210)
        self.bcoin_value_coordinates = (385, 635, 549, 685)

    def open(self):
        pyautogui.moveTo(*self.open_chest_button)
        pyautogui.click()
        return self

    def close(self):
        pyautogui.moveTo(*self.close_chest_button)
        pyautogui.click()