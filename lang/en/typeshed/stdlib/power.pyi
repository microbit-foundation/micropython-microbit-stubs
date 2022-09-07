"""Manage the power modes of the micro:bit (V2 only).
"""

from microbit import MicroBitDigitalPin, Button
from typing import Optional, Tuple, Union

def off() -> None:
    """Power down the board to the lowest possible power mode.

    Example: ``power.off()``

    This is the equivalent to pressing the reset button for a few seconds,
    to set the board in "Off mode".

    The micro:bit will only wake up if the reset button is pressed or,
    if on battery power, when a USB cable is connected.

    When the board wakes up it will start for a reset state, so your program
    will start running from the beginning.
    """
    ...

def deep_sleep(
    ms: Optional[int] = None,
    wake_on: Optional[
        Union[MicroBitDigitalPin, Button] | Tuple[MicroBitDigitalPin | Button, ...]
    ] = None,
    run_every: bool = False,
) -> None:
    """Set the micro:bit into a low power mode where it can wake up and continue operation.

    Example: ``power.deep_sleep(wake_on=(button_a, button_b))``

    The program state is preserved and when it wakes up it will resume operation where it left off.

    Deep Sleep mode will consume more battery power than Off mode.

    The wake up sources are configured via arguments.

    If no wake up sources have been configured it will sleep until the reset button is pressed (which resets the Target MCU) or, in battery power, when the USB cable is inserted.

    :param ms: A time in milliseconds to wait before it wakes up.
    :param wake_on: A single instance or a tuple of pins and/or buttons to wake up the board, e.g. ``deep_sleep(wake_on=button_a)`` or ``deep_sleep(wake_on=(pin0, pin2, button_b))``.
    :param run_every: Set to ``True`` to wake up with each ``microbit.run_every`` scheduled run.
    """
    ...
