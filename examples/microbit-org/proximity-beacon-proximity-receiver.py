from microbit import *
import radio
radio.config(group=1)
radio.on()
light = Image(5,5) # create an empty image

# function to map signal stength to LED brightness
def map(value, fromMin, fromMax, toMin, toMax):
    fromRange = fromMax - fromMin
    toRange = toMax - toMin
    valueScaled = float(value - fromMin) / float(fromRange)
    return toMin + (valueScaled * toRange)

while True:
    message = radio.receive_full()
    if message:
        signal = message[1]
        brightness = map(signal, -98, -44, 0, 9)
        light.fill(round(brightness))
        display.show(light)
