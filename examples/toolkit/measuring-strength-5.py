from microbit import *

magnet_strength_z = compass.get_z()
display.scroll(magnet_strength_z)