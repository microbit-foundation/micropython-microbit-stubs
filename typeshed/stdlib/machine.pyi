"""Low-level utilities.
"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Get a byte string with a unique identifier of a board.

    :return: An identifier that varies from one board instance to another.
    """
    ...

def reset() -> None:
    """Reset the device in a manner similar to pushing the external RESET button."""
    ...

def freq() -> int:
    """Get the CPU frequency in hertz.

    :return: The CPU frequency.
    """
    ...

def disable_irq() -> Any:
    """Disable interrupt requests.

    :return: the previous IRQ state which should be considered an opaque value

    The return value should be passed to the ``enable_irq`` function to restore
    interrupts to their original state.
    """
    ...

def enable_irq(state: Any) -> None:
    """Re-enable interrupt requests.

    :param state: The value that was returned from the most recent call to the ``disable_irq`` function.
    """
    ...

def time_pulse_us(
    pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int = 1000000
) -> int:
    """Time a pulse on a pin.

    If the current input value of the pin is different to ``pulse_level``, the
    function first waits until the pin input becomes equal to
    ``pulse_level``, then times the duration that the pin is equal to
    ``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
    starts straight away.

    :param pin: The pin to use
    :param pulse_level: 0 to time a low pulse or 1 to time a high pulse
    :param timeout_us: A microsecond timeout
    :return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end
    """
    ...
