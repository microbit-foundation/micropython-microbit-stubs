"""Generate random numbers. ()"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Generate an integer with ``n`` random bits. (getrandbits)

Example: ``urandom.getrandbits(1)``

:param n: (n) A value between 1-30 (inclusive)."""
    ...

def seed(n: int) -> None:
    """Initialize the random number generator.

Example: ``urandom.seed(0)``

:param n: (n) The integer seed

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Choose a random integer between ``a`` and ``b`` inclusive. (randint)

Example: ``urandom.randint(0, 9)``

:param a: Start value for the range (inclusive)
:param b: End value for the range (inclusive)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Choose a randomly selected integer between zero and up to (but not
including) ``stop``. (randrange)

Example: ``urandom.randrange(10)``

:param stop: End value for the range (exclusive)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Choose a randomly selected element from ``range(start, stop, step)``. (randrange)

Example: ``urandom.randrange(0, 10)``

:param start: The start of the range (inclusive)
:param stop: The end of the range (exclusive)
:param step: (step) The step."""
    ...
_T = TypeVar("""_T""")

def choice(seq: Sequence[_T]) -> _T:
    """Choose a random element from the non-empty sequence ``seq``.

Example: ``urandom.choice([Image.HAPPY, Image.SAD])``

:param seq: (seq) A sequence.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Generate a random floating point number in the range [0.0, 1.0).

Example: ``urandom.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Return a random floating point number between ``a`` and ``b`` inclusive. (uniform)

Example: ``urandom.uniform(0, 9)``

:param a: Start value for the range (inclusive)
:param b: End value for the range (inclusive)"""
    ...