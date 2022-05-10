from microbit import *
import radio
radio.config(group=99)
radio.on()

while True:
    message = radio.receive()
    sleep(20)
    print(message)
