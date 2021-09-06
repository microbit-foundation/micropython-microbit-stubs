from microbit import *
microphone.set_threshold(SoundEvent.LOUD, 150)
start = 0

while True:
    if microphone.was_event(SoundEvent.LOUD):
        start = running_time()
        display.show(Image.TARGET)

    if microphone.was_event(SoundEvent.QUIET):
        if start > 0:
            time = running_time() - start
            start = 0
            display.clear()
            sleep(100)
            display.scroll(time / 1000)