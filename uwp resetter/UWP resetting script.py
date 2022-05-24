import pyautogui
import time
screenWidth, screenHeight = pyautogui.size()
pyautogui.click(14,1060, interval = 0.5)
pyautogui.write("Awesome")
time.sleep(1.5)
pyautogui.click(570, 890)
time.sleep(4.8)
pyautogui.moveTo(1920, 1020)
pyautogui.drag(1920,-40, duration = 0.2)
pyautogui.click(1920,1020)
pyautogui.click(85, 450)
time.sleep(0.2)
pyautogui.click(280,380)
time.sleep(10)
pyautogui.click(1910, 20)


