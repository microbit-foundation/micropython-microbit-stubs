from microbit import *
import music
import radio
radio.config(group=17)
radio.on()

while True:
    message = radio.receive()
    if message:
        if message == 'door open':
            display.show(Image.NO)
            music.play(["C4:4"])
        if message == 'door closed':
            display.show(Image.YES)
