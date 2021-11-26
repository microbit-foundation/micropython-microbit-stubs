from microbit import *
import log


log.add({
  "temperature": temperature(),
  "sound": microphone.sound_level(),
  "light": display.read_light_level()
})