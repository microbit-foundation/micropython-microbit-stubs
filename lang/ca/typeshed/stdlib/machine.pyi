"""Utilitats de baix nivell. (màquina)"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Obté una cadena de bytes amb un identificador únic d'una placa.

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Reinicia el dispositiu d'una manera semblant a la de prémer el botó extern de REINICI. (reiniciar)

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Obté la freqüència en Hertz de la CPU

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Desactiva les sol·licituds d'interrupció. (desabilita irq)

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Torna a habilitar les sol·licituds d'interrupció. (habilita irq)

Example: ``machine.enable_irq(interrupt_state)``

:param state: (estat) El valor retornat per la crida més recent a la funció ``disable_irq``."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Cronometra una pulsació en un pin. (mesura la durada d'una pulsació en un pin)

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: El pin a utilitzar
:param pulse_level: (nivell de pulsació) 0 per cronometrar la durada de l'estat baix o 1 per cronometrar la durada de l'estat alt
:param timeout_us: (temps d'espera a la resposta excedit en microsegons) Temps d'espera d'un microsegon
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """La classe per a les vistes de la memòria ``mem8``, ``mem16`` i ``mem32``."""

    def __getitem__(self, address: int) -> int:
        """Accedeix a un valor de la memòria

:param address: (adreça) L'adreça de la memòria
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Assigna un valor a l'adreça donada

:param address: (adreça) L'adreça de la memòria
:param value: (valor) El valor enter que cal assignar."""
        ...
mem8: mem
"""vista de la memòria 8-bit (byte)"""
mem16: mem
"""vista de la memòria 16-bit"""
mem32: mem
"""vista de la memòria 32-bit"""