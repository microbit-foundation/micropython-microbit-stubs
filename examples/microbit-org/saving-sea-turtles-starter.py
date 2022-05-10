from microbit import *

while True:
    if display.read_light_level() < 100:
        display.show(Image(
        "00000:"
        "09900:"
        "99999:"
        "99999:"
        "90090"))
    else:
        display.clear()
    sleep(2000)