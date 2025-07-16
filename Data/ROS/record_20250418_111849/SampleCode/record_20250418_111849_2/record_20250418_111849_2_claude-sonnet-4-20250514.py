import pyautogui
import time

# Disable pyautogui failsafe (optional, but recommended for automation)
pyautogui.FAILSAFE = True

# First mouse click at position (737, 120)
pyautogui.click(737, 120)

# Wait for 3.2 seconds
time.sleep(3.2)

# Second mouse click at position (1256, 597)
pyautogui.click(1256, 597)