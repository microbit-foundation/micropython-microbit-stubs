from microbit import *

magnet_strength_y = compass.get_y()
display.scroll(magnet_strength_y)