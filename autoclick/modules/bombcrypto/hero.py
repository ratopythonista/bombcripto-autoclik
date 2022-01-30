from time import sleep

import pyautogui

class Hero:
    def __init__(self) -> None:
        self.hero_coordinates = (634, 892)
        self.close_chest_button = (705, 313)
        self.all_to_work_button = (531, 371)

    def open(self):
        pyautogui.moveTo(*self.hero_coordinates)
        pyautogui.click()
        pyautogui.click()
        return self

    def close(self):
        pyautogui.moveTo(*self.close_chest_button)
        pyautogui.click()
        sleep(1)
        pyautogui.click()

    def has_full_hero(self):
        return pyautogui.locateCenterOnScreen("./autoclick/files/full.png")

    def set_all_to_work(self):
        pyautogui.moveTo(*self.all_to_work_button)
        pyautogui.click()