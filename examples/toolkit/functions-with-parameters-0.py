from microbit import *

def image_wait(myImage):
    display.show(myImage)
    sleep(1000)

image_wait(Image.HEART)
image_wait(Image.HEART_SMALL)