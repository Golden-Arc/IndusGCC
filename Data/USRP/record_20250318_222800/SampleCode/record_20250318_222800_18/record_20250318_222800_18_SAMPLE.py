import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(3)  # Initial delay to switch to target application

pyautogui.click(x=1082, y=855)
time.sleep(1.333)
pyautogui.click(x=1502, y=501)
time.sleep(0.200)
pyautogui.click(x=1502, y=501)