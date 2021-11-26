from microbit import *


for x in range(1024):
    pin0.write_analog(x)
    sleep(3)