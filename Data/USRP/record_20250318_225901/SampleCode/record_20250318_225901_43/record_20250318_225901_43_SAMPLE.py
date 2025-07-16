import pyautogui
import time

# Enable fail-safe and set pause for stability
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1

# Execute click sequence with specified delays
pyautogui.click(304, 175)
time.sleep(1.883)

pyautogui.click(402, 175)
time.sleep(1.700)

pyautogui.click(524, 180)
time.sleep(0.983)

pyautogui.click(543, 181)