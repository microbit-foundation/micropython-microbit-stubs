from microbit import *


on = False
while True:
    if button_a.was_pressed():
        on = not on
    if on:
        display.show(1)
    else:
        display.show(0)