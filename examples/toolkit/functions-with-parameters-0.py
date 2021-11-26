from microbit import *


def count(n):
    for x in range(n):
        display.show(x)
        sleep(1000)

count(5)
count(9)