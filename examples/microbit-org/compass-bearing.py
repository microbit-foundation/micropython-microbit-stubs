from microbit import *
compass.calibrate()

while True:
    if button_a.was_pressed():
        display.scroll(str(compass.heading()))