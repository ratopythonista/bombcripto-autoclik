from datetime import datetime

import pyautogui

from autoclick.modules.image.ocr import image_to_float
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

    def get_bcoin_value(self):
        croped_image = pyautogui.screenshot().crop(self.bcoin_value_coordinates)
        bcoin = image_to_float(croped_image)
        time = datetime.now().timestamp()
        bcoin_log_file.write(f"{time};{bcoin}\n")
        print(f"{time};{bcoin}")