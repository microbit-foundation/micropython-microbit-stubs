"""Générer des nombres aléatoires."""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Générer un entier avec ``n`` bits aléatoires.

Example: ``random.getrandbits(1)``

:param n: Une valeur comprise entre 1-30 (inclus)."""
    ...

def seed(n: int) -> None:
    """Initialiser le générateur de nombres aléatoires.

Example: ``random.seed(0)``

:param n: La graine aléatoire

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Choisir un entier aléatoire entre ``a`` et ``b`` inclus.

Example: ``random.randint(0, 9)``

:param a: Valeur de départ pour l'intervalle (inclus)
:param b: Valeur de fin pour l'intervalle (inclus)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Choisir un entier aléatoirement entre zéro et ``stop`` (mais sans inclure ce dernier).

Example: ``random.randrange(10)``

:param stop: Valeur de fin pour l'intervalle (exclusif)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Choisir un élément sélectionné aléatoirement dans ``range(start, stop, step)``.

Example: ``random.randrange(0, 10)``

:param start: Le début de la plage (inclus)
:param stop: La fin de l'intervalle (exclusif)
:param step: L'incrément."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Choisir un élément aléatoire dans la séquence non vide ``seq``.

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: Une séquence.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Générer un nombre aléatoire à virgule flottante [0.0, 1.0).

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Renvoie un nombre aléatoire à virgule flottante entre ``a`` et ``b`` inclus.

Example: ``random.uniform(0, 9)``

:param a: Valeur de départ pour l'intervalle (inclus)
:param b: Valeur de fin pour l'intervalle (inclus)"""
    ...