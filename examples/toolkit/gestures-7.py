from microbit import *


while True:
    if accelerometer.was_gesture('freefall'):
        display.show('F')