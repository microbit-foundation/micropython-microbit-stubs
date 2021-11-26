from microbit import *


while True:
    if pin1.is_touched():
        display.show(1)