import pyautogui
import time

time.sleep(1)
pyautogui.moveTo(100, 100)
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