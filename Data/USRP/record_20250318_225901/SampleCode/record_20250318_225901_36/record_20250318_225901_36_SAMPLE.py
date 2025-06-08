import pyautogui
import time

pyautogui.FAILSAFE = True

# Move and click sequence
pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.click()
time.sleep(0.5)

pyautogui.moveTo(200, 200, duration=0.5)
pyautogui.doubleClick()
time.sleep(0.5)

pyautogui.moveTo(300, 300, duration=0.5)
pyautogui.rightClick()
time.sleep(0.5)

# Typing sequence
pyautogui.write('Hello, world!')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

# Special key combination
pyautogui.keyDown('shift')
pyautogui.press('a')
pyautogui.keyUp('shift')
time.sleep(0.5)

pyautogui.press('space')
time.sleep(0.5)

# Final click
pyautogui.moveTo(500, 500, duration=0.5)
pyautogui.click()