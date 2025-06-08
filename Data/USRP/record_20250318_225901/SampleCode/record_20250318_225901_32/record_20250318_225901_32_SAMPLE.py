import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(2)  # Give the user a moment to switch to the correct window
pyautogui.click(1073, 859)