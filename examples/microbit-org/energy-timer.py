from microbit import *

display.show('T')
timing = False
total_time = 0
start_time = 0

while True:
    if button_a.was_pressed():
        # start or stop the timer
        if not timing:
            # start the timer
            start_time = running_time()
            timing = True
        else:
            # stop the timer
            timing = False
            end_time = running_time()
            total_time += (end_time - start_time)
            display.show('T')
        
    elif button_b.was_pressed():
        # display the cumulative time
        if not timing:
            display.clear()
            display.scroll(round(total_time/1000))
            sleep(500)
            display.show('T')
    
    elif timing:
        # Animate screen so we know it is timing
        display.show(Image.DIAMOND_SMALL)
        sleep(400)
        display.show(Image.DIAMOND)
        sleep(400)
        