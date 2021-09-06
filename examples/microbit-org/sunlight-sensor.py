from microbit import *

while True:
    if display.read_light_level() > 100:
        display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
    else:
        display.clear()