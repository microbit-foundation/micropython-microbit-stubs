from microbit import *


x = 0b11110000
y = 0b00011111
display.scroll(bin(x ^ y))