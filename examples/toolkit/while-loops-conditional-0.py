from microbit import *


number = 0
while number < 10:
    display.show(number)
    number = number + 1
    sleep(1000)