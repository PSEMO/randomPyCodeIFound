import time
import keyboard
import win32api, win32con
from functools import partial

time.sleep(0.5)

#--------------------------------------------

def click(x,y):
    time.sleep(0.005)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.005)

#--------------------------------------------

clickCount = 0

Pos = [[80, 183], [80, 266], [80, 348], [80, 432], [80, 515],
       [80, 598], [80, 680], [80, 765], [80, 850], [80, 933],
       [80, 1016]]

SecondPos = [1400, 400]

while keyboard.is_pressed('q') != True:

    clickCount = clickCount + 1

    for pos in Pos:
        time.sleep(0.01)
        click(pos[0] + 1920, pos[1])

    print(str(clickCount))

    if clickCount > 500:
        clickCount = 0
        for x in range(6):
            click(SecondPos[0] + 1920, SecondPos[1])

#--------------------------------------------
