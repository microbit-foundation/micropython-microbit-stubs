"""Générer des nombres aléatoires. (random)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Générer un entier avec ``n`` bits aléatoires. (getrandbits)

Example: ``random.getrandbits(1)``

:param n: (n) Une valeur comprise entre 1-30 (inclus)."""
    ...

def seed(n: int) -> None:
    """Initialiser le générateur de nombres aléatoires. (seed)

Example: ``random.seed(0)``

:param n: (n) La graine aléatoire

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Choisir un entier aléatoire entre ``a`` et ``b`` inclus. (randint)

Example: ``random.randint(0, 9)``

:param a: (a) Valeur de départ pour l'intervalle (inclus)
:param b: (b) Valeur de fin pour l'intervalle (inclus)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Choisir un entier aléatoirement entre zéro et ``stop`` (mais sans inclure ce dernier). (randrange)

Example: ``random.randrange(10)``

:param stop: (stop) Valeur de fin pour l'intervalle (exclusif)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Choisir un élément sélectionné aléatoirement dans ``range(start, stop, step)``. (randrange)

Example: ``random.randrange(0, 10)``

:param start: (start) Le début de la plage (inclus)
:param stop: (stop) La fin de l'intervalle (exclusif)
:param step: (step) L'incrément."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Choisir un élément aléatoire dans la séquence non vide ``seq``. (choice)

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: (seq) Une séquence.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Générer un nombre aléatoire à virgule flottante [0.0, 1.0). (random)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Renvoie un nombre aléatoire à virgule flottante entre ``a`` et ``b`` inclus. (uniform)

Example: ``random.uniform(0, 9)``

:param a: (a) Valeur de départ pour l'intervalle (inclus)
:param b: (b) Valeur de fin pour l'intervalle (inclus)"""
    ...