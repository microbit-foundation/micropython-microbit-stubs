from microbit import *
import music

while True:
    if button_a.was_pressed():
        music.play(music.ODE)
    if button_b.was_pressed():
        music.play(music.BLUES)
