import pyautogui
import time

# Add appropriate sleep times between events

# Move the mouse to a specific position (x, y)
pyautogui.moveTo(100, 200, duration=1)
time.sleep(1)

# Click the mouse at the current position
pyautogui.click()
time.sleep(1)

# Move the mouse to another position (x, y)
pyautogui.moveTo(300, 400, duration=1)
time.sleep(1)

# Right-click at the current position
pyautogui.rightClick()
time.sleep(1)

# Double-click at the current position
pyautogui.doubleClick()
time.sleep(1)

# Move the mouse to a new position (x, y)
pyautogui.moveTo(500, 600, duration=1)
time.sleep(1)

# Type a message using the keyboard
pyautogui.write('Hello, this is a test message.', interval=0.1)
time.sleep(1)

# Press the Enter key
pyautogui.press('enter')
time.sleep(1)

# Press the 'ctrl' + 'c' keys to copy
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# Press the 'ctrl' + 'v' keys to paste
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Press the 'esc' key
pyautogui.press('esc')
time.sleep(1)