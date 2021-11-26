from microbit import *


while True:
    if button_a.is_pressed():
        if button_b.is_pressed():
            display.show('C')
        else:
            display.show('A')
    elif button_b.is_pressed():
        display.show('B')