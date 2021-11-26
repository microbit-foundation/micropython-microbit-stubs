from microbit import *


while True:
    if accelerometer.was_gesture('up'):
        display.show(Image.ARROW_N)