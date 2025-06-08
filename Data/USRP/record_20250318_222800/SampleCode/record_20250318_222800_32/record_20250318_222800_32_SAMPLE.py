import pyautogui
import time

# Initial delay
time.sleep(2)

# Mouse movement and click
pyautogui.moveTo(100, 100)
time.sleep(1)
pyautogui.click()
time.sleep(1)

# Typing text
pyautogui.write("Hello, World!")
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# Mouse movement and double click
pyautogui.moveTo(200, 200)
time.sleep(1)
pyautogui.doubleClick()
time.sleep(1)

# Keyboard shortcuts
pyautogui.keyDown('ctrl')
time.sleep(0.5)
pyautogui.press('a')
time.sleep(0.5)
pyautogui.keyUp('ctrl')
time.sleep(1)

# Additional typing
pyautogui.write('This is the second line.')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

# Special keys
pyautogui.press('esc')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)