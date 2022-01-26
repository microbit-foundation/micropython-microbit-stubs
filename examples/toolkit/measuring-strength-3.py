from microbit import *

magnet_strength_x = compass.get_x()
display.scroll(magnet_strength_x)