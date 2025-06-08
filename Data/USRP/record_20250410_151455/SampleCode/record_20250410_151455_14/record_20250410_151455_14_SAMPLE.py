import pyautogui
import time

# Initial delay to allow user to switch to target window
time.sleep(1)

# First sequence of actions
pyautogui.moveTo(100, 200)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.write("Hello, World!")
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

# Second sequence of actions
pyautogui.moveTo(300, 400)
time.sleep(0.5)
pyautogui.doubleClick()
time.sleep(0.5)
pyautogui.write("Python Automation")
time.sleep(0.5)
pyautogui.press('tab')
time.sleep(0.5)

# Third sequence of actions
pyautogui.moveTo(500, 600)
time.sleep(0.5)
pyautogui.rightClick()
time.sleep(0.5)
pyautogui.press('esc')
time.sleep(0.5)

# Additional actions from second script
pyautogui.scroll(10)
time.sleep(0.5)
pyautogui.moveTo(200, 200)
time.sleep(0.5)
pyautogui.dragTo(300, 300, duration=0.5)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
pyautogui.moveTo(400, 400)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)
pyautogui.write("World")
time.sleep(0.5)
pyautogui.press('space')
time.sleep(0.5)
pyautogui.hotkey('alt', 'tab')