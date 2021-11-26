from microbit import *


while True:
    if pin_logo.is_touched():
        display.show(Image.HAPPY)