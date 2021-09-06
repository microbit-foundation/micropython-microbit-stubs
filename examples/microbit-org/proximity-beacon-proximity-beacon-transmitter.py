from microbit import *
import radio
radio.config(group=1, power=1)
radio.on()

while True:
    radio.send('1')
    sleep(200)
