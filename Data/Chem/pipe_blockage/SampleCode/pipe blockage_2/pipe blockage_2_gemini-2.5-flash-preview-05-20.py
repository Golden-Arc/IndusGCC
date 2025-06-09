import pyautogui
import time

time.sleep(1)

pyautogui.click(100, 200)
time.sleep(1.333)

pyautogui.write("Hello")
time.sleep(0.556)

pyautogui.press("enter")
time.sleep(1.767)

pyautogui.doubleClick(300, 400)
time.sleep(0.455)

pyautogui.hotkey("ctrl", "c")
time.sleep(1.444)

pyautogui.write("World")
time.sleep(0.223)

pyautogui.press("space")
time.sleep(0.555)

pyautogui.hotkey("ctrl", "v")
time.sleep(1.334)

pyautogui.rightClick(500, 600)
time.sleep(0.222)

pyautogui.press("esc")