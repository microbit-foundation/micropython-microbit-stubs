from microbit import *


while True:
    if pin0.is_touched():
        display.show(0)