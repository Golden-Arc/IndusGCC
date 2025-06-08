import pyautogui
import time

pyautogui.FAILSAFE = False

pyautogui.click(100, 100)
time.sleep(0.5)
pyautogui.click(200, 200)
time.sleep(0.7)
pyautogui.write('hello')
time.sleep(0.8)
pyautogui.press('enter')
time.sleep(0.5)
pyautogui.doubleClick(300, 300)
time.sleep(0.5)
pyautogui.write('world')
time.sleep(0.8)
pyautogui.press('esc')
time.sleep(0.7)
pyautogui.rightClick(400, 400)