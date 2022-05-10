from microbit import *
import radio
radio.config(group=73)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.show(Image.HEART)
        sleep(1000)
        display.clear()
