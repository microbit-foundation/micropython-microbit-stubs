from microbit import *
import music

while True:
    direction = compass.heading()
    if direction < 5 or direction > 355:
        display.show('N')
        music.play("C4:1")
    elif button_a.is_pressed():
        display.scroll(direction)
    else:
        display.clear()
        music.stop()
