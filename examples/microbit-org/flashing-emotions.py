from microbit import *

while True:
    if button_a.is_pressed():
        for x in range(4):
            display.show(Image.HAPPY)
            sleep(200)
            display.clear()
            sleep(200)
    if button_b.is_pressed():
        for x in range(4):
            display.show(Image.SAD)
            sleep(200)
            display.clear()
            sleep(200)