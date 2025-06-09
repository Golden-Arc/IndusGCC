import pyautogui
import time

# Move and click sequence
pyautogui.moveTo(100, 200)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)

# Typing and pressing enter
pyautogui.typewrite("Hello, World!")
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

# Move and right click
pyautogui.moveTo(300, 400)
time.sleep(0.5)
pyautogui.rightClick()
time.sleep(0.5)

# Scrolling
pyautogui.scroll(10)
time.sleep(0.5)

# Hotkey combination
pyautogui.hotkey('ctrl', 's')
time.sleep(0.5)

# Additional actions from script 2
pyautogui.moveTo(200, 200)
time.sleep(0.5)
pyautogui.doubleClick()
time.sleep(0.5)

# Alt+tab switching
pyautogui.keyDown('alt')
time.sleep(0.1)
pyautogui.press('tab')
time.sleep(0.1)
pyautogui.keyUp('alt')
time.sleep(0.5)

# Additional scrolling
pyautogui.scroll(100)
time.sleep(0.5)
pyautogui.scroll(-50)