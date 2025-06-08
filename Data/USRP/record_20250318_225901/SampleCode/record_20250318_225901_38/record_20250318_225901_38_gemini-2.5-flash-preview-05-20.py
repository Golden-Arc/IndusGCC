import pyautogui
import time

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

# Initial delay to give user time to switch to the target application
time.sleep(3)

# 0.00s: Mouse click at (100, 100)
pyautogui.click(100, 100)

# 0.50s: Type "Hello"
time.sleep(0.50)
pyautogui.write("Hello")

# 1.20s: Press Enter key
time.sleep(0.70)
pyautogui.press("enter")

# 1.70s: Move mouse to (200, 200)
time.sleep(0.50)
pyautogui.moveTo(200, 200)

# 2.00s: Right click
time.sleep(0.30)
pyautogui.rightClick()

# 2.50s: Type "World"
time.sleep(0.50)
pyautogui.write("World")

# 3.00s: Press Escape key
time.sleep(0.50)
pyautogui.press("esc")

# 3.50s: Double click at (300, 300)
time.sleep(0.50)
pyautogui.doubleClick(300, 300)

# 4.00s: Press F5 key
time.sleep(0.50)
pyautogui.press("f5")

# 4.50s: Scroll down by 100 units
time.sleep(0.50)
pyautogui.scroll(-100)

# 5.00s: Scroll up by 50 units
time.sleep(0.50)
pyautogui.scroll(50)

# 5.50s: Press Ctrl+C
time.sleep(0.50)
pyautogui.hotkey("ctrl", "c")

# 6.00s: Press Alt+Tab
time.sleep(0.50)
pyautogui.hotkey("alt", "tab")