from time import sleep

import pyautogui

from autoclick.modules.bombcrypto.hero import Hero
from autoclick.modules.bombcrypto.chest import Chest

while True:

    chest = Chest().open()

    sleep(1.5)

    chest.get_bcoin_value()

    sleep(1.5)

    chest.close()

    sleep(1)

    hero = Hero().open()

    sleep(4)

    if hero.has_full_hero():
        hero.set_all_to_work()
        sleep(2)

    hero.close()

    sleep(50)

    for iteration in range(9):
        print(iteration+1, "minutes waited")
        pyautogui.moveTo(600, 210, duration=1)
        pyautogui.click()
        sleep(59)