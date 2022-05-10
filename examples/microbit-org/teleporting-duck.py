from microbit import *
import radio
radio.config(group=23)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.show(Image.DUCK)
    if accelerometer.was_gesture('shake'):
        display.clear()
        radio.send('duck')
