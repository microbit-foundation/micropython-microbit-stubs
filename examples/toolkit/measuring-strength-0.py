from microbit import *

x_strength = accelerometer.get_x()
display.scroll(x_strength)