"""Zufallszahlen generieren."""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Eine Ganzzahl mit ``n`` zufälligen Bits generieren.

Example: ``random.getrandbits(1)``

:param n: Ein Wert zwischen 1-30 (einschließlich)."""
    ...

def seed(n: int) -> None:
    """Initialisiert den Zufallszahlengenerator.

Example: ``random.seed(0)``

:param n: Der Integer-Seed

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Wählt eine zufällige Ganzzahl zwischen ``a`` und ``b`` (einschließlich) aus.

Example: ``random.randint(0, 9)``

:param a: Anfangswert für den Bereich (inklusiv)
:param b: Endwert für den Bereich (inklusiv)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Wählt eine zufällige Ganzzahl zwischen Null und ``stop`` (exklusiv) aus.

Example: ``random.randrange(10)``

:param stop: Endwert für den Bereich (exklusiv)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Wählt ein zufälliges Element aus ``range(start, stop, step)``.

Example: ``random.randrange(0, 10)``

:param start: Anfang des Bereichs (inklusiv)
:param stop: Das Ende des Bereichs (exklusiv)
:param step: Schrittweite"""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Wählt ein zufälliges Element aus der nicht leeren Sequenz ``seq``.

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: Eine Sequenz.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Erzeugt eine zufällige Fließkommazahl im Bereich [0.0, 1.0).

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Gibt eine zufällige Fließkommazahl zwischen ``a`` und ``b`` inklusiv aus.

Example: ``random.uniform(0, 9)``

:param a: Anfangswert für den Bereich (inklusiv)
:param b: Endwert für den Bereich (inklusiv)"""
    ...