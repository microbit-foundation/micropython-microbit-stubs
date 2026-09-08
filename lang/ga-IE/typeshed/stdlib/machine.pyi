"""Fóntais leibhéal íseal. (meaisín)"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Faigh beart teaghrán le haitheantóir uathúil cláir. (id uathúil)

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Athshocraigh an gléas ar bhealach cosúil le brúigh an cnaipe ATHSHOCRAITHE seachtrach. (athshocrú)

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Faigh an minicíocht LAP i hertz. (minicíocht)

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Díchumasaigh iarratais idirbhriste. (díchumasaigh irq)

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Athchumasaigh iarratais idirbhriste. (cumasaigh irq)

Example: ``machine.enable_irq(interrupt_state)``

:param state: (stát) An luach a cuireadh ar ais ón nglao is déanaí chuig an bhfeidhm ``disable_irq``."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Am buille ar bhioráin. (cuisle ama us)

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: (bioráin) An biorán le húsáid
:param pulse_level: (leibhéal cuisle) 0 go ham cuisle íseal nó 1 go ham cuisle ard
:param timeout_us: (am istigh linn) Teorainn ama micrea soicind
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """An rang le haghaidh radharcanna cuimhne ``mem8``, ``mem16`` agus ``mem32``. (cuimhne)"""

    def __getitem__(self, address: int) -> int:
        """Faigh luach ó chuimhne. (faigh-mír)

:param address: (seoladh) An seoladh cuimhne.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Socraigh luach ag an seoladh a thugtar. (socraigh-mír)

:param address: (seoladh) An seoladh cuimhne.
:param value: (luach) An luach slánuimhir a shocrú."""
        ...
mem8: mem
"""Amharc 8-giotán (beart) ar chuimhne. (cuimhne8)"""
mem16: mem
"""Radharc 16-giotán ar chuimhne. (cuimhne16)"""
mem32: mem
"""Amharc 32-giotán ar chuimhne. (cuimhne32)"""