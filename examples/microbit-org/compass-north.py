from microbit import *
compass.calibrate()

while True:
    bearing = compass.heading()
    if bearing < 45 or bearing > 315:
        display.show('N')
    else:
        display.show(' ')
