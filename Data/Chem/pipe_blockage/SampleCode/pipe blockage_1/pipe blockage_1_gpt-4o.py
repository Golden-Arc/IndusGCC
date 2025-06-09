import pyautogui
import time

# Move the mouse to position (100, 200)
pyautogui.moveTo(100, 200)
time.sleep(1)

# Click the mouse at the current position
pyautogui.click()
time.sleep(1)

# Type the text "Hello, World!"
pyautogui.typewrite("Hello, World!")
time.sleep(1)

# Press the Enter key
pyautogui.press('enter')
time.sleep(1)

# Move the mouse to position (300, 400)
pyautogui.moveTo(300, 400)
time.sleep(1)

# Right-click the mouse at the current position
pyautogui.rightClick()
time.sleep(1)

# Scroll up by 10 units
pyautogui.scroll(10)
time.sleep(1)

# Press the 'ctrl' and 's' keys simultaneously
pyautogui.hotkey('ctrl', 's')
time.sleep(1)