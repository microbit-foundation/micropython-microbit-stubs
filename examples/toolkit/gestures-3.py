from microbit import *


while True:
    if accelerometer.was_gesture('left'):
        display.show(Image.ARROW_W)