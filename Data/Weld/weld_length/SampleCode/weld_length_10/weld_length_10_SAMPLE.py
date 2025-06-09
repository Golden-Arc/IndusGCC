import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(1)  # Give time to switch to target application

pyautogui.click(x=1627, y=315)
time.sleep(0.217)
pyautogui.click(x=1061, y=658)
time.sleep(0.133)
pyautogui.click(x=965, y=567)