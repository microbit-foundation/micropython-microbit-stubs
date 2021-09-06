from microbit import *
import radio
radio.config(group=5)
radio.on()

while True:
    if button_a.was_pressed():
        display.scroll(display.read_light_level())
    if display.read_light_level() > 50:
        radio.send('lights on')
    else:
        radio.send('lights off')
    sleep(10000)
