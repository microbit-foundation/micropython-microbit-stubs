from microbit import *
import random

options = ['PE with Joe', 
           'watch a movie',
           'play a board game',
           'tidy our rooms',
           'learn a song',
           'bake a cake']

while True:
    if button_a.is_pressed():
        choice = random.randint(0, len(options)-1)
        display.scroll(options[choice])