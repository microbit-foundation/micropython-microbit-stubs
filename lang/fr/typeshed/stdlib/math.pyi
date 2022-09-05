"""Fonctions mathématiques. (math)"""
from typing import Tuple

def acos(x: float) -> float:
    """Calculer le cosinus inversé. (acos)

Example: ``math.acos(1)``

:param x: (x) Un nombre
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Calculer le sinus inversé. (asin)

Example: ``math.asin(0)``

:param x: (x) Un nombre
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Calculer la tangente inverse. (atan)

Example: ``math.atan(0)``

:param x: (x) Un nombre
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Calculer la valeur principale de la tangente inverse de ``y/x``. (atan2)

Example: ``math.atan2(0, -1)``

:param y: (x) Un nombre
:param x: (x) Un nombre
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Arrondir un nombre vers l'infini positif. (ceil)

Example: ``math.ceil(0.1)``

:param x: (x) Un nombre
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Calculer ``x`` avec le signe de ``y``. (copysign)

Example: ``math.copysign(1, -1)``

:param x: (x) Un nombre
:param y: (y) La source du signe pour la valeur de retour
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Calculer le cosinus de ``x``. (cos)

Example: ``math.cos(0)``

:param x: (x) Un nombre
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """Convertir les radians en degrés. (degrés)

Example: ``math.degrees(2 * math.pi)``

:param x: (x) Une valeur en radians
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Calculer l'exponentiel de ``x``. (exp)

Example: ``math.exp(1)``

:param x: (x) Un nombre
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Renvoie la valeur absolue de ``x``. (fabs)

Example: ``math.fabs(-0.1)``

:param x: (x) Un nombre
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Arrondir un nombre vers l'infini négatif. (floor)

Example: ``math.floor(0.9)``

:param x: (x) Un nombre
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Calculer le reste de ``x/y``. (fmod)

Example: ``math.fmod(10, 3)``

:param x: (x) Le numérateur
:param y: (y) Le dénominateur"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Décompose un nombre à virgule flottante en sa mantisse et son exposant. (frexp)

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: (x) Un nombre à virgule flottante
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Vérifier si une valeur est finie. (isfinite)

Example: ``math.isfinite(float('inf'))``

:param x: (x) Un nombre.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Vérifie si une valeur est infinie. (isinf)

Example: ``math.isinf(float('-inf'))``

:param x: (x) Un nombre.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """Vérifie si une valeur n'est pas un nombre (NaN). (isnan)

Example: ``math.isnan(float('nan'))``

:param x: (x) Un nombre
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """Calculer ``x * (2**exp)``. (ldexp)

Example: ``math.ldexp(0.5, 2)``

:param x: (x) Un nombre
:param exp: (exp) Exposant entier
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Calculer le logarithme de ``x`` à la base donnée (logarithme naturel par défaut). (log)

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: (x) Un nombre
:param base: (base) La base à utiliser
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Calculer les parties fractionnelles et intégrales de ``x``. (modf)

Example: ``fractional, integral = math.modf(1.5)``

:param x: (x) Un nombre
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Renvoie ``x`` à la puissance ``y``. (pow)

Example: ``math.pow(4, 0.5)``

:param x: (x) Un nombre
:param y: (y) L'exposant
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Convertir les degrés en radians. (radians)

Example: ``math.radians(360)``

:param x: (x) Une valeur en degrés
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Calculer le sinus de ``x``. (sin)

Example: ``math.sin(math.pi/2)``

:param x: (x) Un nombre
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Calculer la racine carrée de ``x``. (sqrt)

Example: ``math.sqrt(4)``

:param x: (x) Un nombre
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Calculer la tangente de ``x``. (tan)

Example: ``math.tan(0)``

:param x: (x) Un nombre
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Arrondir un nombre vers 0. (trunc)

Example: ``math.trunc(-0.9)``

:param x: (x) Un nombre
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Base du logarithme naturel (e)"""
pi: float
"""Le ratio entre la circonférence d'un cercle et son diamètre (pi)"""