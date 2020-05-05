#!/usr/bin/env python
import pyautogui as p
from time import sleep
from os import system


if __name__ == '__main__':
    system('killall unclutter')
    system('killall xscreensaver')
    sleep(1)

    for i in range(5, 0, -1):
        print(i)
        sleep(1)

    while True:
        try:
            p.mouseDown(button='right')
        except KeyboardInterrupt:
            break
    p.mouseUp(button='right')

    system('unclutter -idle 2 -jitter 2 -root & disown')
    system('exec xscreensaver -nosplash & disown')
