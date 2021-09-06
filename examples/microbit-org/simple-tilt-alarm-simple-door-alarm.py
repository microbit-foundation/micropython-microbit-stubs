from microbit import *
import music

while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.ANGRY)
        music.play(["G4:4", "A4", "B4", "B4", "B4", "A4", "G4", "F4"])
        