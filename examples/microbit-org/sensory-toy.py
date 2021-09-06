from microbit import *
import audio

while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.SURPRISED)
        audio.play(Sound.GIGGLE)
    if accelerometer.was_gesture('up'):
        display.show(Image.HAPPY)
        audio.play(Sound.HELLO)
    if accelerometer.was_gesture('down'):
        display.show(Image.ASLEEP)
        audio.play(Sound.YAWN)
    if accelerometer.was_gesture('left'):
        display.show(Image.ARROW_W)
        audio.play(Sound.SLIDE)
    if accelerometer.was_gesture('right'):
        display.show(Image.ARROW_E)
        audio.play(Sound.SOARING)
