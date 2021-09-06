from microbit import *

while True:
    sleep(2000)
    display.show(Image('00000:'
                       '00000:'
                       '00900:'
                       '00000:'
                       '00000'))
    sleep(500)
    display.show(Image.DIAMOND_SMALL)
    sleep(500)
    display.show(Image.DIAMOND)
    sleep(2000)
    display.show(Image.DIAMOND_SMALL)
    sleep(500)
    display.show(Image('00000:'
                       '00000:'
                       '00900:'
                       '00000:'
                       '00000'))

