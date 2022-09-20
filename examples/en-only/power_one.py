from microbit import *
import power


@run_every(s=20)
def silly_face():
    display.show(Image.SILLY)
    sleep(500)


while True:
    if button_a.is_pressed():
        display.scroll("Off")
        # In this mode the micro:bit can only wake up via the reset button
        power.off()
        # This line of code will never be executed, as waking up from this
        # mode starts the programme from the beginning
        display.show(Image.SURPRISED)
    elif button_b.is_pressed():
        display.scroll("Sleep")
        # Go into Deep Sleep with multiple wake up sources
        power.deep_sleep(
            wake_on=(pin0, pin1, button_a),
            ms=5 * 60 * 1000,  # In 5 minutes it wakes up anyway
            run_every=False,  # Blocks run_every from waking up the board
        )
        # When the micro:bit wakes up will it continue running from here
        display.show(Image.ASLEEP)
        sleep(1000)
    display.show(Image.HAPPY)
    sleep(200)
