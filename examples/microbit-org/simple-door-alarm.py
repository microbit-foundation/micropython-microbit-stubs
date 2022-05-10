# Python uses nanoteslas to measure magnetism.
# Experiment with different numbers depending on the
# strength of your magnet, which you can read by 
# pressing button A.

from microbit import *

while True:
    if button_a.was_pressed():
        display.scroll(compass.get_field_strength())
    if compass.get_field_strength() < 200000:
        display.show(Image.ANGRY)