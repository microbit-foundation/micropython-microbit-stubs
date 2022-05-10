from microbit import *
import radio
import music
radio.config(group=1)
radio.on()

def alarm():
    display.show(Image.ANGRY)
    music.play(music.BADDY)
    
while True:
    message = radio.receive()
    if message:
        alarm()
    if accelerometer.was_gesture('shake'):
        radio.send('thief!')
        alarm()
