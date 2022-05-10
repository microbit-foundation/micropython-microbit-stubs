from microbit import *

currentTemp = temperature()
max = currentTemp
min = currentTemp

while True:
    display.show('.')
    currentTemp = temperature()
    if currentTemp < min:
        min = currentTemp
    if currentTemp > max:
        max = currentTemp
    if button_a.was_pressed():
        display.scroll(min)
    if button_b.was_pressed():
        display.scroll(max)
    sleep(1000)
    display.clear()
    sleep(1000)
