"""Generar números aleatorios. (random)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Genera un entero con ``n`` bits aleatorios. (getrandbits)

Example: ``random.getrandbits(1)``

:param n: (n) Un valor entre 1 - 30 (inclusive)."""
    ...

def seed(n: int) -> None:
    """Inicializa el generador de números aleatorios. (seed)

Example: ``random.seed(0)``

:param n: (n) La semilla como un número entero

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Elige un entero aleatorio entre ``a`` y ``b`` inclusive. (randint)

Example: ``random.randint(0, 9)``

:param a: (a) Valor inicial para el rango (inclusive)
:param b: (b) Valor final para el rango (inclusive)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Elige un entero seleccionado aleatoriamente desde cero hasta (pero sin incluir) ``stop``. (randrange)

Example: ``random.randrange(10)``

:param stop: (stop) Valor final para el rango (exclusivo)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Elige un elemento seleccionado aleatoriamente de ``range(start, stop, step)``. (randrange)

Example: ``random.randrange(0, 10)``

:param start: (comenzar) El inicio del rango (inclusive)
:param stop: (stop) El final del rango (exclusivo)
:param step: (step) El paso."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Elige un elemento aleatorio de la secuencia no vacía ``seq``. (choice)

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: (seq) Una secuencia.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Genera un número de coma flotante aleatorio en el rango [0.0, 1.0). (random)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Devuelve un número de coma flotante aleatorio entre ``a`` y ``b`` inclusive. (uniform)

Example: ``random.uniform(0, 9)``

:param a: (a) Valor inicial para el rango (inclusive)
:param b: (b) Valor final para el rango (inclusive)"""
    ...