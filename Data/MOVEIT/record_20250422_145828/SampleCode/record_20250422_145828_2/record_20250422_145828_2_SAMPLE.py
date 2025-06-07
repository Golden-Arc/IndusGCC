import pyautogui
import time

# Initial mouse movement and click
pyautogui.moveTo(100, 100, duration=0.5)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)

# Typing actions
pyautogui.typewrite('Hello, World!', interval=0.1)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

# Mouse movement and right click
pyautogui.moveTo(200, 200, duration=0.5)
time.sleep(0.5)
pyautogui.rightClick()
time.sleep(0.5)

# Scrolling actions
pyautogui.scroll(300)
time.sleep(0.5)
pyautogui.scroll(-300)
time.sleep(0.5)

# Circular mouse motion
pyautogui.moveTo(300, 300, duration=0.5)
time.sleep(0.5)
pyautogui.dragRel(100, 0, duration=0.5)
time.sleep(0.5)
pyautogui.dragRel(0, 100, duration=0.5)
time.sleep(0.5)
pyautogui.dragRel(-100, 0, duration=0.5)
time.sleep(0.5)
pyautogui.dragRel(0, -100, duration=0.5)
time.sleep(0.5)

# Keyboard shortcuts
pyautogui.keyDown('alt')
time.sleep(0.2)
pyautogui.press('tab')
time.sleep(0.2)
pyautogui.keyUp('alt')
time.sleep(0.5)