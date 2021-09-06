from microbit import *
import radio
radio.config(group=73, power=1)
radio.on()

while True:
    radio.send('hello')
    sleep(2000)
