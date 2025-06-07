import pyautogui
import time

# Move the mouse to a specific position
pyautogui.moveTo(100, 100, duration=0.5)
time.sleep(1)

# Click the mouse
pyautogui.click()
time.sleep(1)

# Type a message
pyautogui.typewrite('Hello, World!', interval=0.1)
time.sleep(1)

# Press the Enter key
pyautogui.press('enter')
time.sleep(1)

# Move the mouse to another position
pyautogui.moveTo(200, 200, duration=0.5)
time.sleep(1)

# Right-click the mouse
pyautogui.rightClick()
time.sleep(1)

# Scroll up
pyautogui.scroll(300)
time.sleep(1)

# Scroll down
pyautogui.scroll(-300)
time.sleep(1)

# Move the mouse in a circular motion
pyautogui.moveTo(300, 300, duration=0.5)
time.sleep(1)
pyautogui.dragRel(100, 0, duration=0.5)
time.sleep(1)
pyautogui.dragRel(0, 100, duration=0.5)
time.sleep(1)
pyautogui.dragRel(-100, 0, duration=0.5)
time.sleep(1)
pyautogui.dragRel(0, -100, duration=0.5)
time.sleep(1)