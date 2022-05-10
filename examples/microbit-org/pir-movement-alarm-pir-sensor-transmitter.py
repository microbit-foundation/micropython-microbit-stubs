from microbit import *
import radio
radio.config(group=73)
radio.on()

while True:
    if pin0.read_digital():
        display.show(Image.DIAMOND_SMALL)
        radio.send('moving')
    else:
        display.clear()
        radio.send('still')
    sleep(1000)
