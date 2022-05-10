from microbit import *

lights = Image("11111:"
              "11111:"
              "11111:"
              "11111:"
              "11111")

while True:
    display.show(lights * microphone.sound_level())