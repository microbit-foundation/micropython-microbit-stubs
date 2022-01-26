from microbit import *

import log

@run_every(h=1, min=20, s=30, ms=50)
def log_data():
    log.add({
      "temperature": temperature(),
      "sound": microphone.sound_level(),
      "light": display.read_light_level()
    })