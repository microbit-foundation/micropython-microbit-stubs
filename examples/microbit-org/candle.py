from microbit import *
import random

lit = True

while True:
    if microphone.was_event(SoundEvent.LOUD):
        lit = not lit
        sleep(500)
    if lit:
        display.show(Image(
        "00900:"
        "09990:"
        "09990:"
        "09990:"
        "09990"))
        sleep(150)
        flicker = random.randint(1, 3)
        if flicker != 2:
            display.set_pixel(2,0,0)
            display.set_pixel(flicker,0,9)
        sleep(150)
    else:
        display.clear()