from microbit import *


while True:
    if button_a.was_pressed():
        display.show('A')
    elif button_b.was_pressed():
        display.show('B')
    if accelerometer.was_gesture('shake'):
        break
display.scroll('Game over')