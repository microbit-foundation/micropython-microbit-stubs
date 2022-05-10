from microbit import *
import radio
radio.config(group=99)
radio.on()

while True:
    sleep(20)
    radio.send(str(accelerometer.get_values()))
