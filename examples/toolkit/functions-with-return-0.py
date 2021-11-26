from microbit import *


def convertCtoF(c):
    return c * 1.8 + 32

display.scroll(convertCtoF(temperature()))