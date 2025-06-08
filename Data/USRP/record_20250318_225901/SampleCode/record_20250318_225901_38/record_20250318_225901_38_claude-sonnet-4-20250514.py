import pyautogui
import time

# First action: Move the mouse to a specific position (e.g., 500, 500)
pyautogui.moveTo(500, 500)
time.sleep(1)

# Second action: Click at the current mouse position
pyautogui.click()
time.sleep(1)

# Third action: Type some text
pyautogui.write('Hello, world!')
time.sleep(1)

# Fourth action: Press the 'enter' key
pyautogui.press('enter')
time.sleep(1)

# Fifth action: Move the mouse to another position (e.g., 800, 800)
pyautogui.moveTo(800, 800)
time.sleep(1)

# Sixth action: Right-click at the current mouse position
pyautogui.rightClick()
time.sleep(1)

# Seventh action: Scroll down
pyautogui.scroll(-500)
time.sleep(1)

# Eighth action: Press the 'esc' key to cancel
pyautogui.press('esc')
time.sleep(1)