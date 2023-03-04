"""Genera nombres aleatoris. (aleatori)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Genera un nombre enter amb ``n`` bits aleatoris.

Example: ``random.getrandbits(1)``

:param n: Un valor entre 1-30 (inclusiu)."""
    ...

def seed(n: int) -> None:
    """Inicialitza el generador de nombres aleatoris. (llavor)

Example: ``random.seed(0)``

:param n: The integer seed

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Tria un nombre enter aleatori entre ``a`` i ``b`` inclosos.

Example: ``random.randint(0, 9)``

:param a: Valor inicial de l'interval (inclòs)
:param b: Valor final de l'interval (inclòs)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Tria un nombre enter seleccionat aleatòriament entre zero i fins a (però no
inclòs) ``stop``.

Example: ``random.randrange(10)``

:param stop: (atura) Valor final de l'interval (exclòs)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Tria un element seleccionat aleatòriament de ``range(start, stop, step)``.

Example: ``random.randrange(0, 10)``

:param start: L'inici de l'interval (inclòs)
:param stop: (atura) El final de l'interval (exclusiu)
:param step: El pas."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Tria un element aleatori de la seqüència no buida ``seq``.

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: Una seqüència.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Genera un nombre aleatori de coma flotant en l'interval [0.0, 1.0). (aleatori)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Retorna un nombre de coma flotant aleatori entre ``a`` i ``b`` inclosos. (uniforme)

Example: ``random.uniform(0, 9)``

:param a: Valor inicial de l'interval (inclòs)
:param b: Valor final de l'interval (inclòs)"""
    ...