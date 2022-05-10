from microbit import *
lightsOn = False

while True:
    if microphone.was_event(SoundEvent.LOUD):
        lightsOn = not lightsOn
        if lightsOn:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))
        else:
            display.clear()
    sleep(100)