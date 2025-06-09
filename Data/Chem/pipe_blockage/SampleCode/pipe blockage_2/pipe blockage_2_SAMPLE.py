import pyautogui
import time

# Move and click at (100, 200)
pyautogui.moveTo(100, 200)
time.sleep(1)
pyautogui.click()
time.sleep(1)

# Type text and press Enter
pyautogui.typewrite("Hello, World!")
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# Move and double click at (300, 400)
pyautogui.moveTo(300, 400)
time.sleep(1)
pyautogui.doubleClick()
time.sleep(1)

# Select all with Ctrl+A
pyautogui.keyDown('ctrl')
time.sleep(0.5)
pyautogui.press('a')
time.sleep(0.5)
pyautogui.keyUp('ctrl')
time.sleep(1)

# Additional actions from script 2
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.typewrite("World")
time.sleep(0.5)
pyautogui.press('space')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Right click at (500, 600) and press Esc
pyautogui.moveTo(500, 600)
time.sleep(0.5)
pyautogui.rightClick()
time.sleep(0.5)
pyautogui.press('esc')