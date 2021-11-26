from microbit import *


while True:
    if display.read_light_level() < 50:
        display.show(Image.HEART)
    elif display.read_light_level() < 150:
        display.show(Image.HEART_SMALL)
    else:
        display.clear()