from microbit import *

def image_wait(myImage, delay=1000):
    display.show(myImage)
    sleep(delay)

image_wait(Image.HEART)
image_wait(Image.HEART_SMALL, delay=3000)
display.clear()