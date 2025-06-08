import pyautogui
import time

# Initial delay to allow user to switch to target application
time.sleep(1)

# Mouse movement and clicks
pyautogui.moveTo(100, 200, duration=1)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(300, 400, duration=1)
time.sleep(1)
pyautogui.rightClick()
time.sleep(1)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.moveTo(500, 600, duration=1)
time.sleep(1)

# Keyboard typing and commands
pyautogui.write('Hello, this is a test message.', interval=0.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('esc')
time.sleep(1)

# Additional actions from second script
pyautogui.moveTo(100, 100, duration=0.5)
time.sleep(0.5)
pyautogui.click(100, 100)
time.sleep(0.5)
pyautogui.dragTo(200, 200, duration=0.5)
time.sleep(0.5)
pyautogui.press('a')
time.sleep(0.5)
pyautogui.press('b')
time.sleep(0.5)
pyautogui.press('c')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 's')
time.sleep(0.5)
pyautogui.write('Hello World')