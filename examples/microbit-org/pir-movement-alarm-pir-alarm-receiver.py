from microbit import *
import music
import radio
radio.config(group=73)
radio.on()

while True:
    message = radio.receive()
    if message:
        if message == 'moving':
            display.show(Image.STICKFIGURE)
            music.play(["C4:4"])
        if message == 'still':
            display.clear()
