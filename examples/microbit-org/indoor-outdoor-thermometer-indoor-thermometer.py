from microbit import *
import radio
radio.config(group=23)
radio.on()
outdoorTemp = '-'

while True:
    message = radio.receive()
    if message:
        outdoorTemp = message
    if button_a.was_pressed():
        display.scroll(str(temperature()))
    if button_b.was_pressed():
        display.scroll(outdoorTemp)
        