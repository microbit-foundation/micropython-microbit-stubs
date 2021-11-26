from microbit import *


while True:
    if accelerometer.was_gesture('3g'):
        display.show(3)