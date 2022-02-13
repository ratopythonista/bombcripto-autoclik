from datetime import datetime, timedelta
from time import sleep
from random import randint

import pyautogui
from tqdm import tqdm

from autoclick.modules.gshow.vote import vote
from autoclick.modules.bombcrypto.hero import Hero
from autoclick.modules.bombcrypto.chest import Chest

hero = Hero()
chest = Chest()
last_workout = datetime.now() - timedelta(hours=2)

print("Prepare windowns...")
sleep(5)

while True:

    chest.open()

    sleep(2)

    chest.get_bcoin_value()
    print(datetime.now() - last_workout)

    sleep(1)

    chest.close()

    sleep(1)

    if  datetime.now() - last_workout >= timedelta(hours=2): 

        hero.open()

        sleep(2)
        
        hero.set_all_to_work()

        sleep(2)

        hero.close()

        sleep(2)

        last_workout = datetime.now()

    for iteration in tqdm(range(250)):
        if iteration%50 == 0:
            pyautogui.moveTo(randint(550, 650), randint(160, 260))
            pyautogui.click()
            # vote()
        sleep(1)

