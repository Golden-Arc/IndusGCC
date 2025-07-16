import pyautogui
import time

# Enable fail-safe (move mouse to top-left corner to stop)
pyautogui.FAILSAFE = True

# Set a small pause between PyAutoGUI calls for stability
pyautogui.PAUSE = 0.1

# Reproduce the mouse click sequence
pyautogui.click(304, 175)
time.sleep(1.883)

pyautogui.click(402, 175)
time.sleep(1.700)

pyautogui.click(524, 180)
time.sleep(0.983)

pyautogui.click(543, 181)