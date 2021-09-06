from microbit import *
import radio
radio.config(group=23)
radio.on()

while True:
    radio.send(str(temperature()))
    sleep(5000)
