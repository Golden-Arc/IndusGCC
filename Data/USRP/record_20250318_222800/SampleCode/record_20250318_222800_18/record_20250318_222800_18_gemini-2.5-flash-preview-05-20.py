import pyautogui
import time

time.sleep(3) # Give a 3-second delay to switch to the target application

pyautogui.click(x=1082, y=855, button='left')
time.sleep(1.333)
pyautogui.click(x=1502, y=501, button='left')
time.sleep(0.200)
pyautogui.click(x=1502, y=501, button='left')