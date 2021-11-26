from microbit import *


microphone.set_threshold(SoundEvent.LOUD, 200)
microphone.set_threshold(SoundEvent.QUIET, 1)