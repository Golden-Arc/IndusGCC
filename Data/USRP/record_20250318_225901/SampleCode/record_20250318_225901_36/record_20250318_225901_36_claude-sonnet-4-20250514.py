import pyautogui
import time

# Move the mouse to position (100, 100)
pyautogui.moveTo(100, 100)
time.sleep(1)

# Click the mouse at the current position
pyautogui.click()
time.sleep(1)

# Move the mouse to position (200, 200)
pyautogui.moveTo(200, 200)
time.sleep(1)

# Double-click the mouse at the current position
pyautogui.doubleClick()
time.sleep(1)

# Move the mouse to position (300, 300)
pyautogui.moveTo(300, 300)
time.sleep(1)

# Right-click the mouse at the current position
pyautogui.rightClick()
time.sleep(1)

# Type some text (e.g., "Hello, world!")
pyautogui.write('Hello, world!')
time.sleep(1)

# Press the Enter key
pyautogui.press('enter')
time.sleep(1)

# Press and hold the Shift key, then press 'a' (for uppercase 'A')
pyautogui.keyDown('shift')
pyautogui.press('a')
pyautogui.keyUp('shift')
time.sleep(1)

# Press the spacebar
pyautogui.press('space')
time.sleep(1)

# Move the mouse to position (500, 500) and click
pyautogui.moveTo(500, 500)
pyautogui.click()