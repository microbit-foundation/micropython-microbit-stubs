from microbit import *

magnet_strength_all = compass.get_field_strength()
display.scroll(magnet_strength_all)