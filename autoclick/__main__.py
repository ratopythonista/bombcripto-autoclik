
from time import sleep
from random import randint
from datetime import datetime, timedelta



import pyautogui
from tqdm import tqdm

# from autoclick.modules.gshow.vote import vote
from autoclick.modules.linux.page import page_focus
from autoclick.modules.bombcrypto.hero import Hero
from autoclick.modules.bombcrypto.chest import Chest

hero = Hero()
chest = Chest()
last_workout = datetime.now() - timedelta(hours=2)


while True:

    if  datetime.now() - last_workout >= timedelta(hours=2): 

        page_focus("Bombcrypto")

        sleep(3)

        pyautogui.press('f5') 
        sleep(15)

        # Move To
        pyautogui.moveTo(1280, 670)
        
        sleep(1)

        pyautogui.click()

        sleep(5)
        
        pyautogui.moveTo(2460, 630)

        sleep(1)

        pyautogui.click()

        sleep(20)

        pyautogui.moveTo(1300, 490)

        sleep(1)

        pyautogui.click()


        hero.open()

        sleep(2)
        
        hero.set_all_to_work()

        sleep(2)

        hero.close()

        sleep(2)

        last_workout = datetime.now()



