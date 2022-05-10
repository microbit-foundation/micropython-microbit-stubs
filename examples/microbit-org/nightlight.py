from microbit import *

while True:
    if display.read_light_level() < 100:
        display.show(Image(
        "99999:"
        "99999:"
        "99999:"
        "99999:"
        "99999"))
    else:
        display.clear()
    sleep(2000)
