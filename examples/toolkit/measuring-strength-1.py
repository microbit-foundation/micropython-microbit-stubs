from microbit import *

y_strength = accelerometer.get_y()
display.scroll(y_strength)