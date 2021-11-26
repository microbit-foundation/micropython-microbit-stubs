from microbit import *


running = False
while True:
    if button_a.was_pressed():
        running = not running
    if running:
        display.show(1)
    else:
        display.show(0)