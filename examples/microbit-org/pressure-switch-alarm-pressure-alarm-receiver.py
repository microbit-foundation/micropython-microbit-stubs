from microbit import *
import music
import radio
radio.config(group=34)
radio.on()

while True:
    message = radio.receive()
    if message:
        if message == 'intruder':
            display.show(Image.ANGRY)
            music.play(music.BADDY)
    if button_a.was_pressed():
        display.clear()
