"""Generate random numbers.
"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Generate an integer with ``n`` random bits.

    :param n: A value between 1-30 (inclusive).
    """
    ...

def seed(n: int) -> None:
    """Initialize the random number generator.

    :param n: The integer seed

    This will give you reproducibly deterministic randomness from a given starting
    state (``n``).
    """
    ...

def randint(a: int, b: int) -> int:
    """Choose a random integer between ``a`` and ``b`` inclusive.

    :param a: Start value for the range (inclusive)
    :param b: End value for the range (inclusive)

    Alias for ``randrange(a, b + 1)``.
    """
    ...

@overload
def randrange(stop: int) -> int:
    """Choose a randomly selected integer between zero and up to (but not
    including) ``stop``.

    :param stop: End value for the range (exclusive)
    """
    ...

@overload
def randrange(start: int, stop: int, step: int = 1) -> int:
    """
    Choose a randomly selected element from ``range(start, stop, step)``.

    :param start: The start of the range (inclusive)
    :param stop: The end of the range (exclusive)
    :param step: The step.
    """
    ...

_T = TypeVar("_T")

def choice(seq: Sequence[_T]) -> _T:
    """Choose a random element from the non-empty sequence ``seq``.

    :param seq: A sequence.

    If ``seq`` is  empty, raises ``IndexError``.
    """
    ...

def random() -> float:
    """Generate a random floating point number in the range [0.0, 1.0).

    :return: The random floating point number
    """
    ...

def uniform(a: float, b: float) -> float:
    """
    Return a random floating point number between ``a`` and ``b`` inclusive.
    """
    ...
