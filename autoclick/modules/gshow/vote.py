import imp
import pyautogui
from time import sleep


def vote():
    dg_pos = (1830, 580)

    pyautogui.moveTo(*dg_pos)
    pyautogui.click()
    sleep(3)

    human_pos = (1814, 730)
    pyautogui.moveTo(*human_pos)
    pyautogui.click()
    sleep(3)

    again = (1900, 400)
    pyautogui.moveTo(*again)
    pyautogui.click()
    sleep(3)

    pyautogui.press('f5') 
    sleep(4)
