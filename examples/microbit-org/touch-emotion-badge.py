from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)
    if pin_logo.is_touched():
        display.show(Image.SURPRISED)