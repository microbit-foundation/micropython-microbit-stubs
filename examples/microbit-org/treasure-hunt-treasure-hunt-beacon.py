from microbit import *
import radio
radio.config(group=1, power=1)
radio.on()
id = '1' # change this number for each beacon
display.show(id)
sleep(2000)
display.clear()

while True:
    radio.send(id)
    sleep(200)
