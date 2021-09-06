from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        tool = random.randint(0,2)
        if tool == 0:
            display.show(Image.SQUARE_SMALL)
        elif tool == 1:
            display.show(Image.SQUARE)
        else:
            display.show(Image.SWORD)