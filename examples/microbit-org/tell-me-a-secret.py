from microbit import *
import radio
radio.config(group=7)
radio.on()

while True:
    message = radio.receive()
    if message:
        if message == 'yes':
            display.show(Image.YES)
            sleep(500)
            display.clear()
        elif message == 'no':
            display.show(Image.NO)
            sleep(500)
            display.clear()
    if button_a.was_pressed():
        radio.send('yes')
        display.show(Image.YES)
        sleep(500)
        display.clear()
    if button_b.was_pressed():
        radio.send('no')
        display.show(Image.NO)
        sleep(500)
        display.clear()
