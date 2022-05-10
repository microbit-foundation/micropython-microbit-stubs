from microbit import *
import music

while True:
    if pin1.is_touched():
        music.play(["F4:4", "A4", "C5"])
    if pin2.is_touched():
        music.play(["A4:4", "C5", "E5"])
