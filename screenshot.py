import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = f'C:/Users/hp/Documents/PYTHON_PROJECTS/screenshots_data/{name}.png'
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()