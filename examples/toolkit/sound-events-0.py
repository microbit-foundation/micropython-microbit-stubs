from microbit import *


while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.HAPPY)
    elif microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.ASLEEP)