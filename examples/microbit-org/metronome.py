from microbit import *
import music
tempo = 100

while True:
    music.set_tempo(bpm=tempo)
    music.play(['C4:1', 'r:3']) # play C for 1 tick, rest for 3 ticks
    if button_a.was_pressed():
        tempo -= 5
    if button_b.was_pressed():
        tempo += 5  
    