from microbit import *
import radio
radio.config(group=7)
radio.on()

while True:
    radio.send(str(accelerometer.get_y()))
    message = radio.receive()
    if message:
        display.scroll(message)
    sleep(2000)