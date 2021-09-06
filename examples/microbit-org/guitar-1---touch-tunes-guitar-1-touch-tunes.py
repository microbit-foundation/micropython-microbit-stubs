from microbit import *
import music

while True:
    if pin1.is_touched():
        music.play(music.ODE)
    if pin2.is_touched():
        music.play(music.BLUES)
