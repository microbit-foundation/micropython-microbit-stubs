from microbit import *


while True:
    if pin1.read_digital():
        display.show(1)
    else:
        display.show(0)