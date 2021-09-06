from microbit import *
steps=0

while True:
    if accelerometer.get_y() > 1500:
        steps += 1
        display.scroll(steps)
