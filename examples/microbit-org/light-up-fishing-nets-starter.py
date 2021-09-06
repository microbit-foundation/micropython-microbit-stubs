from microbit import *
import music

while True:
    if display.read_light_level() < 50:
        display.show(Image(
        "99999:"
        "99999:"
        "99999:"
        "99999:"
        "99999"))
        music.play("A5")
    else:
        display.clear()
    sleep(1000)