from microbit import *
import audio

timer = 0
display.show(Image(
    "00000:"
    "09090:"
    "00000:"
    "09990:"
    "00000"))
audio.play(Sound.HELLO)

while True:
    if pin_logo.is_touched():
        timer = 0
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
    elif accelerometer.was_gesture('shake'):
        timer = 0
        display.show(Image.SURPRISED)
        audio.play(Sound.GIGGLE)
    else:
        sleep(500)
        timer += 0.5
        # sleep for half a second only to make it react more quickly to logo touch & shake
        
    if timer == 20:
        display.show(Image.SAD)
        audio.play(Sound.SAD)
    elif timer == 30:
        display.show(Image.ASLEEP)
        audio.play(Sound.YAWN)
    elif timer == 40:
        display.show(Image.SKULL)
        audio.play(Sound.MYSTERIOUS)
        break
    