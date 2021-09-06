from microbit import *
import radio
radio.config(group=2)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.show(Image.HAPPY)
    if button_a.is_pressed():
        display.clear()
        radio.send('smile')