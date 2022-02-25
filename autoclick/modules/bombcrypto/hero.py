from time import sleep

import pyautogui

class Hero:
    def __init__(self) -> None:
        self.hero_coordinates = (1280, 770)
        self.close_chest_button = (1330, 320)
        self.all_to_work_button = (1190, 365)

    def open(self):
        pyautogui.moveTo(*self.hero_coordinates)
        pyautogui.click()
        sleep(1)
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