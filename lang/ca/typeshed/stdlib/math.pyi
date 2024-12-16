"""Funcions matemàtiques (matemàtiques)"""
from typing import Tuple

def acos(x: float) -> float:
    """Calcula l'invers del cosinus (arc cosinus)

Example: ``math.acos(1)``

:param x: Un nombre
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Calcula l'invers del sinus (arc sinus)

Example: ``math.asin(0)``

:param x: Un nombre
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Calcula l'invers de la tangent (arc tangent)

Example: ``math.atan(0)``

:param x: Un nombre
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Calcula el valor principal de l'invers de la tangent de ``y/x``. (arc tangent 2)

Example: ``math.atan2(0, -1)``

:param y: Un nombre
:param x: Un nombre
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Arrodoneix un nombre cap a l'infinit positiu. (arrodoniment per excés)

Example: ``math.ceil(0.1)``

:param x: Un nombre
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Calcula ``x`` amb el signe de ``y``.

Example: ``math.copysign(1, -1)``

:param x: Un nombre
:param y: L'origen del signe pel valor retornat.
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Calcula el cosinus de ``x``. (cosinus)

Example: ``math.cos(0)``

:param x: Un nombre
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """Convertir radiants a graus (graus)

Example: ``math.degrees(2 * math.pi)``

:param x: Un valor en radians
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Calcula l'exponencial de ``x``.

Example: ``math.exp(1)``

:param x: Un nombre
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Retorna el valor absolut de ``x``.

Example: ``math.fabs(-0.1)``

:param x: Un nombre
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Arrodoneix un nombre cap a l'infinit negatiu. (arrodoniment per defecte)

Example: ``math.floor(0.9)``

:param x: Un nombre
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Calcula el residu de ``x/y``.

Example: ``math.fmod(10, 3)``

:param x: El numerador
:param y: El denominador"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Descompon un nombre de coma flotant en la seva mantissa i el seu exponent.

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: Un nombre de coma flotant
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Verifica si un valor és finit.

Example: ``math.isfinite(float('inf'))``

:param x: Un nombre.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Verifica si un valor és infinit.

Example: ``math.isinf(float('-inf'))``

:param x: Un nombre.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """Verifica si un valor és un "no nombre" (NaN)

Example: ``math.isnan(float('nan'))``

:param x: Un nombre
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """Calcula ``x * (2**exp)``. (ldexp (Calcula ``x * (2**exp)``))

Example: ``math.ldexp(0.5, 2)``

:param x: Un nombre
:param exp: Exponent enter
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Calcula el logaritme ``x`` d'una base donada (per defecte al logaritme natural). (registre)

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: Un nombre
:param base: La base a utilitzar
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Calcula les parts fraccionàries i integrals de ``x``.

Example: ``fractional, integral = math.modf(1.5)``

:param x: Un nombre
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Retorna ``x`` a la potència de ``y``.

Example: ``math.pow(4, 0.5)``

:param x: Un nombre
:param y: L'exponent
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Converteix graus a radians

Example: ``math.radians(360)``

:param x: Un valor en graus
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Calcula el sinus de ``x``. (sinus)

Example: ``math.sin(math.pi/2)``

:param x: Un nombre
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Calcula l'arrel quadrada de ``x``.

Example: ``math.sqrt(4)``

:param x: Un nombre
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Calcula la tangent de ``x``.

Example: ``math.tan(0)``

:param x: Un nombre
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Arrodoneix un nombre cap al 0. (trunca)

Example: ``math.trunc(-0.9)``

:param x: Un nombre
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Base del logaritme natural"""
pi: float
"""La relació entre la circumferència d'un cercle i el seu diàmetre"""