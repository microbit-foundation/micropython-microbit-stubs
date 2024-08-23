"""crwdns328832:0crwdne328832:0 (crwdns328830:0crwdne328830:0)"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """crwdns328836:0crwdne328836:0 (crwdns328834:0crwdne328834:0)

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """crwdns328840:0crwdne328840:0 (crwdns328838:0crwdne328838:0)

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """crwdns328844:0crwdne328844:0 (crwdns328842:0crwdne328842:0)

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """crwdns328848:0crwdne328848:0 (crwdns328846:0crwdne328846:0)

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """crwdns328852:0crwdne328852:0 (crwdns328850:0crwdne328850:0)

Example: ``machine.enable_irq(interrupt_state)``

:param state: (crwdns328854:0crwdne328854:0) crwdns328856:0``disable_irq``crwdne328856:0"""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """crwdns328860:0crwdne328860:0 (crwdns328858:0crwdne328858:0)

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: (crwdns328862:0crwdne328862:0) crwdns328864:0crwdne328864:0
:param pulse_level: (crwdns328866:0crwdne328866:0) crwdns328868:0crwdne328868:0
:param timeout_us: (crwdns328870:0crwdne328870:0) crwdns328872:0crwdne328872:0
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """crwdns328876:0``mem8``crwdnd328876:0``mem16``crwdnd328876:0``mem32``crwdne328876:0 (crwdns328874:0crwdne328874:0)"""

    def __getitem__(self, address: int) -> int:
        """crwdns328880:0crwdne328880:0 (crwdns328878:0crwdne328878:0)

:param address: (crwdns328882:0crwdne328882:0) crwdns328884:0crwdne328884:0
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """crwdns328888:0crwdne328888:0 (crwdns328886:0crwdne328886:0)

:param address: (crwdns328890:0crwdne328890:0) crwdns328892:0crwdne328892:0
:param value: (crwdns328894:0crwdne328894:0) crwdns328896:0crwdne328896:0"""
        ...
mem8: mem
"""crwdns328900:0crwdne328900:0 (crwdns328898:0crwdne328898:0)"""
mem16: mem
"""crwdns328904:0crwdne328904:0 (crwdns328902:0crwdne328902:0)"""
mem32: mem
"""crwdns328908:0crwdne328908:0 (crwdns328906:0crwdne328906:0)"""