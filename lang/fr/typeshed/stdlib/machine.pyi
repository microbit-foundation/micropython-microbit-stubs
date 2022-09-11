"""Utilitaires bas niveau"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Récupère une chaîne d'octets représentant un identifiant unique d'une carte.

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Réinitialise l'appareil d'une manière similaire à la pression sur le bouton RESET externe.

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Récupère la fréquence du CPU en hertz.

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Désactiver les demandes d'interruption.

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Réactiver les demandes d'interruption.

Example: ``machine.enable_irq(interrupt_state)``

:param state: La valeur qui a été renvoyée par l'appel le plus récent à la fonction ``disable_irq``."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Chronométrer une impulsion sur une broche.

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: (broche) La broche à utiliser
:param pulse_level: 0 pour chronométrer une impulsion basse ou 1 pour chronométrer une impulsion haute.
:param timeout_us: Un délai d'attente en microseconde
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """La classe pour les vues mémoire ``mem8``, ``mem16`` et ``mem32``."""

    def __getitem__(self, address: int) -> int:
        """Accéder à une valeur dans la mémoire.

:param address: L'adresse en mémoire.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Écrire une valeur à une adresse donnée.

:param address: L'adresse en mémoire.
:param value: La valeur entière à écrire."""
        ...
mem8: mem
"""Vue de la mémoire au format 8-bit (octet)."""
mem16: mem
"""Vue de la mémoire au format 16-bit."""
mem32: mem
"""Vue de la mémoire au format 32-bit."""