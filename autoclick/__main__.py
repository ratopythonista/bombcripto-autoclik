from time import sleep
from datetime import datetime

import pyautogui
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
bcoin_log_file = open("bcoin_log_file.csv", "a+")

bau = pyautogui.locateCenterOnScreen("./autoclick/files/bau.png")
pyautogui.moveTo(*bau, duration=1)
pyautogui.click() 

sleep(1.5)

pyautogui.screenshot("./autoclick/files/screen.png")
screenshot = Image.open("./autoclick/files/screen.png")
bcoin = screenshot.crop((385, 635, 549, 685))
bcoin_string = pytesseract.image_to_string(bcoin)
bcoin = float(bcoin_string.replace(",", "."))
time = datetime.now().timestamp()
bcoin_log_file.write(f"{time};{bcoin}\n")

sleep(1.5)

pyautogui.moveRel(-130, 100, duration=1)
pyautogui.click()

sleep(3)

pyautogui.moveTo(*bau, duration=1)
pyautogui.moveRel(-450, 700, duration=1)

pyautogui.click()
pyautogui.click()

sleep(5)

fechar = pyautogui.locateCenterOnScreen("./autoclick/files/fechar.png")

# TODO Check if energy is full
# TODO Set all to work

pyautogui.moveTo(*fechar, duration=1)
pyautogui.click()
sleep(1)
pyautogui.click()