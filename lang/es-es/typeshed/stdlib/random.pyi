"""Generar números aleatorios. (aleatorio)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Genera un entero con ``n`` bits aleatorios.

Example: ``random.getrandbits(1)``

:param n: Un valor entre 1 - 30 (inclusive)."""
    ...

def seed(n: int) -> None:
    """Inicializa el generador de números aleatorios. (semilla)

Example: ``random.seed(0)``

:param n: La semilla como un número entero

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Elige un entero aleatorio entre ``a`` y ``b`` inclusive. (entero aleatorio)

Example: ``random.randint(0, 9)``

:param a: Valor inicial para el rango (inclusive)
:param b: Valor final para el rango (inclusive)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Elige un entero seleccionado aleatoriamente desde cero hasta (pero sin incluir) ``stop``. (rango aleatorio)

Example: ``random.randrange(10)``

:param stop: (detener) Valor final para el rango (exclusivo)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Elige un elemento seleccionado aleatoriamente de ``range(start, stop, step)``. (rango aleatorio)

Example: ``random.randrange(0, 10)``

:param start: (comenzar) El inicio del rango (inclusive)
:param stop: (detener) El final del rango (exclusivo)
:param step: (paso) El paso."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Elige un elemento aleatorio de la secuencia no vacía ``seq``. (elección)

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: (sec) Una secuencia.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Genera un número de coma flotante aleatorio en el rango [0.0, 1.0). (aleatorio)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Devuelve un número de coma flotante aleatorio entre ``a`` y ``b`` inclusive. (uniforme)

Example: ``random.uniform(0, 9)``

:param a: Valor inicial para el rango (inclusive)
:param b: Valor final para el rango (inclusive)"""
    ...