"""Narzędzia niskiego poziomu."""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Pobierz ciąg bajtów z unikatowym identyfikatorem płytki.

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Zresetuj urządzenie w sposób podobny do naciśnięcia zewnętrznego przycisku RESET.

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Uzyskaj częstotliwość procesora w hercach

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Wyłącz żądania przerwań.

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Ponownie włącz żądania przerwań.

Example: ``machine.enable_irq(interrupt_state)``

:param state: Wartość, która została zwrócona z ostatniego wywołania funkcji ``disable_irq``."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Czas pulsowania na pinie.

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: Pin do użycia
:param pulse_level: 0 do czasu niskiego pulsu lub 1 do czasu wysokiego pulsu
:param timeout_us: Mikrosekundowy limit czasu
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """Klasa dla widoków pamięci ``mem8``, ``mem16`` i ``mem32``."""

    def __getitem__(self, address: int) -> int:
        """Uzyskaj dostęp do wartości z pamięci.

:param address: Adres pamięci.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Ustaw wartość dla podanego adresu.

:param address: Adres pamięci.
:param value: Wartość całkowita do ustawiania."""
        ...
mem8: mem
"""8-bitowy widok pamięci."""
mem16: mem
"""16-bitowy widok pamięci."""
mem32: mem
"""32-bitowy widok pamięci."""