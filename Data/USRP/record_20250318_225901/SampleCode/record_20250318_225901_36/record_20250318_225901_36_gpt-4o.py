import pyautogui
import time

# Move the mouse to position (100, 200) over 1 second
pyautogui.moveTo(100, 200, duration=1)
time.sleep(1)

# Click the mouse at the current position
pyautogui.click()
time.sleep(1)

# Type the text "Hello, World!" with a 0.1 second interval between each character
pyautogui.write('Hello, World!', interval=0.1)
time.sleep(1)

# Press the 'enter' key
pyautogui.press('enter')
time.sleep(1)

# Move the mouse to position (300, 400) over 1 second
pyautogui.moveTo(300, 400, duration=1)
time.sleep(1)

# Double-click the mouse at the current position
pyautogui.doubleClick()
time.sleep(1)

# Scroll down 500 units
pyautogui.scroll(-500)
time.sleep(1)

# Press the 'ctrl' and 's' keys simultaneously
pyautogui.hotkey('ctrl', 's')
time.sleep(1)