from microbit import *
import radio


while True:
    message = radio.receive()
    if message:
        display.scroll(message)