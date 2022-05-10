from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        number = random.randint(1, 3)
        if number == 3:
            display.show(Image.YES)
        elif number == 2:
            display.show(Image.NO)
        else:
            display.show(Image.MEH)