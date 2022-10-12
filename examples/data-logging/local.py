import log
from microbit import *

entry = {
  'temperature': temperature(),
  'light': display.read_light_level()
}
log.add(entry)