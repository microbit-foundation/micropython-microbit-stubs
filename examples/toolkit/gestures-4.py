from microbit import *


while True:
    if accelerometer.was_gesture('right'):
        display.show(Image.ARROW_E)