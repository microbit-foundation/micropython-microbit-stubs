from microbit import *


x = 0b11110000
y = 0b10101010
display.scroll(bin(x & y))