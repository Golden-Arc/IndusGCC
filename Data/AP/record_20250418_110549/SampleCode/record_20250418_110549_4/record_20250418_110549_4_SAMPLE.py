import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(1)  # Initial delay before starting actions

pyautogui.click(x=100, y=349, button='left')