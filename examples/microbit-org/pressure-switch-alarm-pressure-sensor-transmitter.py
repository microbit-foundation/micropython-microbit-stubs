from microbit import *
import radio
radio.config(group=34)
radio.on()

while True:
    if pin0.is_touched():
        radio.send('intruder')
