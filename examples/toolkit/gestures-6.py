from microbit import *


while True:
    if accelerometer.was_gesture('6g'):
        display.show(6)