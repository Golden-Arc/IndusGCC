import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(1)  # Initial delay to switch to target application

pyautogui.click(x=156, y=1027)
time.sleep(1.250)
pyautogui.click(x=877, y=279)
time.sleep(0.867)
pyautogui.click(x=1192, y=812)