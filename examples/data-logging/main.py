from microbit import *
import log


# Creates a new "log" file with the given "headers", timestamp added by default
log.set_labels("temperature", "brightness")

# Configuring a different time unit for the timestamp
log.set_labels("temperature", "brightness", timestamp=log.SECONDS)

# Enables the serial mirroring
log.set_mirroring(True)

# A decorator might be a bit "magical" as we have never used them before in micro:bit
@run_every(h=1, min=20, s=30, ms=50)
def log_periodically():
    """
    Records the temperature & brightness every 00:01:20:30:50 (dd:hh:mm:ss:ms).
    """
    log.add({"temperature": temperature(), "brightness": display.read_light_level()})
    # Or
    log.add(temperature=temperature(), brightness=display.read_light_level())


def main():
    # Or schedule using a callback
    run_every(log_periodically, h=4, min=30, s=20, ms=10)

    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            log.delete(full=True)
        elif button_a.is_pressed():
            # On Button B add another entry to the log
            # this shows the function with the decorator can still be called
            log_periodically()
            display.show(Image.HAPPY)
            sleep(500)
        elif button_b.is_pressed():
            log.delete()
            sleep(500)
        else:
            display.show(Image.CONFUSED)


if __name__ == "__main__":
    main()
