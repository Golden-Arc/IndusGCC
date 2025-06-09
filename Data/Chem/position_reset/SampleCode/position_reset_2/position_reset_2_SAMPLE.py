import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(1)  # Initial delay to switch to target application

pyautogui.click(x=669, y=1060)
time.sleep(3.967)
pyautogui.click(x=1038, y=58)
time.sleep(0.183)
pyautogui.click(x=1078, y=652)