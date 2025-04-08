"""Low-Level-Utilities. (maschine)"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Liefert eine Byte-Zeichenkette mit einem eindeutigen Bezeichner für ein Board. (Eindeutige ID)

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Setzt das Gerät zurück, als würde man die externe RESET-Taste drückt. (zurücksetzen)

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Ermittelt die Taktfrequenz der CPU in Hertz.

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Deaktiviere Interrupt-Anforderungen. (IRQ deaktivieren)

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Interrupt-Anfragen wieder aktivieren. (IRQ aktivieren)

Example: ``machine.enable_irq(interrupt_state)``

:param state: Der Wert, der beim letzten Aufruf der Funktion ``disable_irq`` zurückgegeben wurde."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Gibt die Dauer eines Impulses an einem Pin zurück. (impulsdauer_messen)

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: Der zu verwendende Pin
:param pulse_level: (Impulsstufe) 0, um einen Low-Impuls oder 1, um einen High-Impuls zu messen
:param timeout_us: Eine Verzögerung in Mikrosekunden
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """Die Klasse für die ``mem8``, ``mem16`` und ``mem32`` Speicheranzeigen."""

    def __getitem__(self, address: int) -> int:
        """Greife auf einen Wert im Speicher zu.

:param address: (adresse) Die Speicheradresse.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Setzt einen Wert an der angegebenen Adresse.

:param address: (adresse) Die Speicheradresse.
:param value: (wert) Der zu setzende Integer-Wert."""
        ...
mem8: mem
"""8-Bit (Byte) Ansicht des Speichers."""
mem16: mem
"""16-Bit (Byte) Ansicht des Speichers."""
mem32: mem
"""32-Bit (Byte) Ansicht des Speichers."""