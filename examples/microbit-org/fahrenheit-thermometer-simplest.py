from microbit import *

def convertCtoF(C):
    return C * 1.8 + 32

while True:
    if button_a.was_pressed():
        display.scroll(temperature())
    if button_b.was_pressed():
        display.scroll(convertCtoF(temperature()))