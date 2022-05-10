from microbit import *

display.show('M')
reading = display.read_light_level()
sleep(100)

while True:
    if button_a.was_pressed():
        # take a light measurement and store it
        reading = display.read_light_level()
        display.show(Image.DIAMOND_SMALL)
        sleep(400)
        display.show(Image.DIAMOND)
        sleep(400+500)
        display.show('M')

    elif button_b.was_pressed():
        # display the stored light measurement
        display.clear()
        display.scroll(reading)
        sleep(500)
        display.show('M')