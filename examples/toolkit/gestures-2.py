from microbit import *


while True:
    if accelerometer.was_gesture('down'):
        display.show(Image.ARROW_S)