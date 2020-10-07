import pyautogui

import time
time.sleep(5)
for word in open('C:\\Users\compu\Desktop\ss.txt', "r"):
    time.sleep(1)
    pyautogui.typewrite(word)
    pyautogui.press("enter")
