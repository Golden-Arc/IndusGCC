import pyautogui
import time

# Move the mouse to position (100, 200)
pyautogui.moveTo(100, 200)
time.sleep(1)

# Click the mouse
pyautogui.click()
time.sleep(1)

# Type the text "Hello, World!"
pyautogui.typewrite("Hello, World!")
time.sleep(1)

# Press the Enter key
pyautogui.press('enter')
time.sleep(1)

# Move the mouse to position (300, 400)
pyautogui.moveTo(300, 400)
time.sleep(1)

# Double click the mouse
pyautogui.doubleClick()
time.sleep(1)

# Type the text "Goodbye!"
pyautogui.typewrite("Goodbye!")
time.sleep(1)

# Press the Escape key
pyautogui.press('esc')