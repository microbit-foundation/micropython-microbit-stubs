from microbit import *

count = 0
display.show(count)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        count = 0
        display.scroll(count)
    elif button_b.is_pressed():
        count += 1
        display.scroll(count)
    elif button_a.is_pressed():
        display.scroll(count)
    sleep(100)