from microbit import *
import music

# Uses accelerometer readings in the x and y axis 
# and also allows the micro:bit to be slightly off-level
# to make it work better in practice
while True:
    if accelerometer.get_x() > -10 and accelerometer.get_x() < 10 and accelerometer.get_y() > -10 and accelerometer.get_y() < 10:
        display.show(Image.YES)
        music.play('C5:1')
        sleep(200)
    else:
        display.show(Image.NO)
