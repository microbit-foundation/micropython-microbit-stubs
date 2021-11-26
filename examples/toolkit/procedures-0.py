from microbit import *


def countdown():
    for x in range(9,0,-1):
        display.show(x)
        sleep(1000)

countdown()