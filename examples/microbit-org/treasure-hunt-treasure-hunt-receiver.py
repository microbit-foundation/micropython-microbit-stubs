from microbit import *
import radio
radio.config(group=1)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.show(message)
        sleep(200)
        display.clear()
