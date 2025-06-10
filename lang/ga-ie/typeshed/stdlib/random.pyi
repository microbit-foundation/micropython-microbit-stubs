"""Gin uimhreacha randamacha. (randamach)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Gin slánuimhir le ``n`` giotán randamach.

Example: ``random.getrandbits(1)``

:param n: Luach idir 1-30 (san áireamh)."""
    ...

def seed(n: int) -> None:
    """Túsaigh an gineadóir uimhreacha randamacha. (síol)

Example: ``random.seed(0)``

:param n: An síol slánuimhir

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Roghnaigh slánuimhir randamach idir ``a`` agus ``b`` san áireamh.

Example: ``random.randint(0, 9)``

:param a: Luach tosaigh don raon (san áireamh)
:param b: Luach deiridh don raon (san áireamh)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Roghnaigh slánuimhir a roghnaíodh go randamach idir nialas agus suas le (ach ní
lena n-áirítear) ``stop``.

Example: ``random.randrange(10)``

:param stop: (stad) Luach deiridh don raon (eisiach)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Roghnaigh eilimint a roghnaíodh go randamach ó ``range(start, stop, step)``.

Example: ``random.randrange(0, 10)``

:param start: (tús) Tús an raoin (san áireamh)
:param stop: (stad) Deireadh an raoin (eisiach)
:param step: (céim) An chéim."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Roghnaigh eilimint randamach ón seicheamh neamhfholamh ``seq``. (rogha)

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: Seicheamh.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Gin uimhir randamach snámhphointe sa raon [0.0, 1.0). (randamach)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Seol uimhir randamach snámhphointe ar ais idir ``a`` agus ``b`` san áireamh. (éide)

Example: ``random.uniform(0, 9)``

:param a: Luach tosaigh don raon (san áireamh)
:param b: Luach deiridh don raon (san áireamh)"""
    ...