from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll('A')
    elif button_b.was_pressed():
        display.scroll('B')
    sleep(100) 