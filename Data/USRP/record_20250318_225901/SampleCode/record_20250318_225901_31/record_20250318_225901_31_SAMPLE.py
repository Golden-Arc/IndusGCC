import pyautogui
import time

pyautogui.FAILSAFE = True
time.sleep(1)  # Initial delay to switch to the target application

pyautogui.click(x=784, y=696)
time.sleep(0.100)

pyautogui.click(x=784, y=696)
time.sleep(0.933)

pyautogui.click(x=972, y=429)
time.sleep(0.300)

pyautogui.press('1')
time.sleep(0.200)

pyautogui.click(x=969, y=448)
time.sleep(0.167)

pyautogui.press('1')
time.sleep(0.733)

pyautogui.click(x=1052, y=861)
time.sleep(1.083)

pyautogui.click(x=657, y=832)
time.sleep(0.117)

pyautogui.click(x=657, y=831)