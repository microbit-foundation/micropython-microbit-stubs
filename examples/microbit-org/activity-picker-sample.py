from microbit import *
import random

while True:
    if button_a.is_pressed():
        random_number = random.randint(1, 6)
        if random_number == 1:
            display.scroll('PE with Joe')
        elif random_number == 2:
            display.scroll('watch a movie')
        elif random_number == 3:
            display.scroll('play a board game')
        elif random_number == 4:
            display.scroll('tidy our rooms')
        elif random_number == 5:
            display.scroll('play a card game')
        else:
            display.scroll('learn a song')