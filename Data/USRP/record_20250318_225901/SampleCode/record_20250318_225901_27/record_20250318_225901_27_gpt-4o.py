import pyautogui
import time

# Move the mouse to position (100, 200) and click
pyautogui.moveTo(100, 200)
pyautogui.click()
time.sleep(1)

# Type 'Hello, World!' with a delay between each character
pyautogui.write('Hello, World!', interval=0.1)
time.sleep(1)

# Press the 'enter' key
pyautogui.press('enter')
time.sleep(1)

# Move the mouse to position (300, 400) and double click
pyautogui.moveTo(300, 400)
pyautogui.doubleClick()
time.sleep(1)

# Move the mouse to position (500, 600) and right click
pyautogui.moveTo(500, 600)
pyautogui.rightClick()
time.sleep(1)

# Scroll up 500 units
pyautogui.scroll(500)
time.sleep(1)

# Press 'ctrl' + 's' to save
pyautogui.hotkey('ctrl', 's')
time.sleep(1)