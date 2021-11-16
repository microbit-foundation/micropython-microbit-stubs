from microbit import *
import log


@run_every(min=5)
def log_temp():
    """Records the temperature every 5 minutes."""
    log.add(temperature=temperature())
