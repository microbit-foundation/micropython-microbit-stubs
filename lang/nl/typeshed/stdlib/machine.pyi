"""Hulpprogramma's op laag niveau."""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Krijg een byte string met een uniek id van een bord. (uniek id)

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Reset het apparaat op een manier die lijkt op de externe RESET knop.

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Krijg de CPU frequentie in Hertz. (frequentie)

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Interruptie verzoeken uitschakelen. (irq uitschakelen)

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Zet interruptie verzoeken opnieuw aan. (irq inschakelen)

Example: ``machine.enable_irq(interrupt_state)``

:param state: (staat) De waarde die is teruggestuurd van de meest recente oproep naar de ``disable_irq`` functie."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Time een puls op een pin. (tijd pulse us)

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: De pin om te gebruiken
:param pulse_level: (puls niveau) 0 om een lage puls te tikken of 1 om een hoge puls te tikken
:param timeout_us: Een microseconde time-out
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """De klasse van de ``mem8``, ``mem16`` en ``mem32`` geheugenweergaven."""

    def __getitem__(self, address: int) -> int:
        """Toegang tot een waarde uit het geheugen.

:param address: (adres) Het geheugenadres.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Stel een waarde in op het opgegeven adres.

:param address: (adres) Het geheugen adres.
:param value: (waarde) De integerwaarde die moet worden ingesteld."""
        ...
mem8: mem
"""8-bit (byte) weergave van het geheugen."""
mem16: mem
"""16-bit (byte) weergave van het geheugen."""
mem32: mem
"""32-bit (byte) weergave van het geheugen."""