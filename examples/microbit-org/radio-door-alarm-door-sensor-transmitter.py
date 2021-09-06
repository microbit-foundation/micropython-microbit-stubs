from microbit import *
import radio
radio.config(group=17)
compass.calibrate()
radio.on()

while True:
    if button_a.was_pressed():
        display.scroll(compass.get_field_strength())
    if compass.get_field_strength() < 100000:
        display.show(Image.DIAMOND_SMALL)
        radio.send('door open')
    else:
        display.clear()
        radio.send('door closed')
    sleep(2000)
