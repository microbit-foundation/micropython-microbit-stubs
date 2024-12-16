"""Generuj liczb losowe. (losowy)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Wygeneruj liczbę całkowitą z ``n`` losowymi bitami.

Example: ``random.getrandbits(1)``

:param n: Wartość między 1–30 (włącznie)."""
    ...

def seed(n: int) -> None:
    """Zainicjuj generator liczb losowych.

Example: ``random.seed(0)``

:param n: Całkowity zarodek

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Wybierz losową liczbę całkowitą pomiędzy ``a`` i ``b`` włącznie.

Example: ``random.randint(0, 9)``

:param a: Wartość początkowa dla zakresu (włącznie)
:param b: Wartość końcowa dla zakresu (wyłącznie)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Wybierz losowo wybraną liczbę całkowitą między zero aż do (ale nie
włącznie) ``stop``.

Example: ``random.randrange(10)``

:param stop: Wartość końcowa zakresu (wyłącznie)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Wybierz losowo wybrany element z ``range(start, stop, step)``.

Example: ``random.randrange(0, 10)``

:param start: Początek zakresu (włącznie)
:param stop: Koniec zakresu (wyłącznie)
:param step: Krok"""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Wybierz losowy element z niepustego cigu ``seq``.

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: Cig.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Wygeneruj losową liczbę zmiennopozycyjną w zakresie [0.0, 1.0).

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Zwróć losową liczbę zmiennopozycyjnłą między ``a`` i ``b``.

Example: ``random.uniform(0, 9)``

:param a: Wartość początkowa dla zakresu (włącznie)
:param b: Wartość końcowa dla zakresu (wyłącznie)"""
    ...