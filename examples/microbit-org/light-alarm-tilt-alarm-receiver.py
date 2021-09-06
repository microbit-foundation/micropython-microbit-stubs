from microbit import *
import music
import radio
radio.config(group=5)
radio.on()

while True:
    message = radio.receive()
    if message:
        if message == 'lights off':
            display.clear()
        elif message == 'lights on':
            display.show(Image.ANGRY)
            music.play(music.BADDY)
