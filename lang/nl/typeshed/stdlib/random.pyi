"""Willekeurige getallen genereren. (willekeurig)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Genereer een geheel getal met ``n`` willekeurige bits.

Example: ``random.getrandbits(1)``

:param n: Een waarde tussen 1-30 (inclusief)."""
    ...

def seed(n: int) -> None:
    """Initialiseer de willekeurige getalgenerator.

Example: ``random.seed(0)``

:param n: De integer seed

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Kies een willekeurig geheel getal tussen ``a`` en ``b`` inclusief.

Example: ``random.randint(0, 9)``

:param a: Beginwaarde voor het bereik (inclusief)
:param b: Eindwaarde voor het bereik (inclusief)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Kies een willekeurig geselecteerd geheel getal tussen nul en tot (maar niet
inclusief) ``stop``.

Example: ``random.randrange(10)``

:param stop: Eindwaarde voor het bereik (exclusief)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Kies een willekeurig geselecteerd element uit ``range(start, stop, step)``.

Example: ``random.randrange(0, 10)``

:param start: Het begin van het bereik (inclusief)
:param stop: Einde van het bereik (exclusief)
:param step: (stap) De stap."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Kies een willekeurig element uit de niet-lege reeks ``seq``. (keuze)

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: Een volgorde.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Genereer een willekeurig zwevend puntnummer in het bereik [0.0, 1.0). (willekeurig)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Geeft een willekeurig zwevend punt nummer tussen ``a`` en ``b`` inclusief.

Example: ``random.uniform(0, 9)``

:param a: Beginwaarde voor het bereik (inclusief)
:param b: Eindwaarde voor het bereik (inclusief)"""
    ...