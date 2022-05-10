from microbit import *
import audio

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)
        audio.play(Sound.SAD)
    if pin_logo.is_touched():
        display.show(Image.SURPRISED)
        audio.play(Sound.SPRING)