from microbit import *
display.show('L')

LIGHT = 100  # <<< Enter your 'measured' reading here

HYSTERESIS = 8
LIGHT -= (HYSTERESIS/2)
DARK = LIGHT - HYSTERESIS
ON_IMAGE = Image('99999:99999:99999:99999:99999')
OFF_IMAGE = Image('00000:00000:00900:00000:00000')
timing = False
start_time = 0
total_time = 0
reading = display.read_light_level()
sleep(1000)

def show_number(n):
    # Make number display the same as MakeCode
    if len(str(n)) == 1:
        display.show(n)
    else:
        display.scroll(n)

while True:
    reading = display.read_light_level()
    if reading < DARK:
        if timing:
            # it has just gone dark, update timer for 'on' time
            end_time = running_time()
            total_time += (end_time - start_time)
            timing = False
        
    elif reading >= LIGHT:
        if not timing:
            # it has just gone light, start the timer
            start_time = running_time()
            timing = True
        
    if button_b.was_pressed():
        # calculate and display cumulative time in minutes
        minutes = total_time / 60000
        if timing:
            # adjust live for current ON time
            minutes += (running_time() - start_time) / 60000
        display.clear()
        show_number(round(minutes))  # whole numbers only
        sleep(500)

    # update the display with the ON/OFF state
    if timing:
        display.show(ON_IMAGE)
    else:
        display.show(OFF_IMAGE)
    sleep(1000)

        