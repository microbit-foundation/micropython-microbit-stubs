from microbit import *
import random

while True:
    gameStarted = False
    sleep(random.randint(1000, 5000))
    gameStarted = True
    display.show(Image.HEART)
    while gameStarted:
        if pin1.is_touched():
            display.show('A')
            gameStarted = False
        elif pin2.is_touched():
            display.show('B')
            gameStarted = False
    sleep(3000)
    display.clear()
