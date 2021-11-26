from microbit import *


while True:
    if button_a.is_pressed() and not button_b.is_pressed():
        display.scroll('A not B')
    sleep(200)