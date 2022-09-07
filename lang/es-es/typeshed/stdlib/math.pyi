"""Funciones matemáticas. (matemáticas)"""
from typing import Tuple

def acos(x: float) -> float:
    """Calcula el inverso del coseno. (acos)

Example: ``math.acos(1)``

:param x: (x) Un número
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Calcula el inverso del seno. (asin)

Example: ``math.asin(0)``

:param x: (x) Un número
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Calcula el inverso de la tangente. (atan)

Example: ``math.atan(0)``

:param x: (x) Un número
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Calcula el valor principal del inverso de la tangente de ``y/x``. (atan2)

Example: ``math.atan2(0, -1)``

:param y: (x) Un número
:param x: (x) Un número
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Redondea un número hacia el infinito positivo. (ceil)

Example: ``math.ceil(0.1)``

:param x: (x) Un número
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Calcula ``x`` con el signo de ``y``. (copysign)

Example: ``math.copysign(1, -1)``

:param x: (x) Un número
:param y: (y) Procedencia del signo para el valor que devuelve
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Calcula el coseno de ``x``. (cos)

Example: ``math.cos(0)``

:param x: (x) Un número
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """Convierte radianes a grados. (grados)

Example: ``math.degrees(2 * math.pi)``

:param x: (x) Un valor en radianes
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Calcular el exponencial de ``x``. (exp)

Example: ``math.exp(1)``

:param x: (x) Un número
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Devuelve el valor absoluto de ``x``. (fabs)

Example: ``math.fabs(-0.1)``

:param x: (x) Un número
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Redondea un número hacia el infinito negativo. (floor)

Example: ``math.floor(0.9)``

:param x: (x) Un número
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Calcula el resto de ``x/y``. (fmod)

Example: ``math.fmod(10, 3)``

:param x: (x) El numerador
:param y: (y) El denominador"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Descompone un número de coma flotante en su mantisa y exponente. (frexp)

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: (x) Un número de coma flotante
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Comprueba si un valor es finito. (isfinite)

Example: ``math.isfinite(float('inf'))``

:param x: (x) Un número.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Compruebe si un valor es infinito. (isinf)

Example: ``math.isinf(float('-inf'))``

:param x: (x) Un número.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """Comprueba si un valor no es un número (NaN, not-a-number en inglés). (isnan)

Example: ``math.isnan(float('nan'))``

:param x: (x) Un número
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """Calcula ``x * (2**exp)``. (ldexp)

Example: ``math.ldexp(0.5, 2)``

:param x: (x) Un número
:param exp: (exp) Exponente entero
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Calcula el logaritmo de ``x`` en la base dada (por defecto, el logaritmo natural). (log)

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: (x) Un número
:param base: (base) La base a usar
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Calcula la parte fraccionaria y entera de ``x``. (modf)

Example: ``fractional, integral = math.modf(1.5)``

:param x: (x) Un número
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Devuelve ``x`` elevado a ``y``. (pow)

Example: ``math.pow(4, 0.5)``

:param x: (x) Un número
:param y: (y) El exponente
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Convierte grados a radianes. (radianes)

Example: ``math.radians(360)``

:param x: (x) Un valor en grados
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Calcula el seno de ``x``. (sin)

Example: ``math.sin(math.pi/2)``

:param x: (x) Un número
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Calcula la raíz cuadrada de ``x``. (sqrt)

Example: ``math.sqrt(4)``

:param x: (x) Un número
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Calcula la tangente de ``x``. (tan)

Example: ``math.tan(0)``

:param x: (x) Un número
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Redondea un número hacia 0. (trunc)

Example: ``math.trunc(-0.9)``

:param x: (x) Un número
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Base del logaritmo natural (e)"""
pi: float
"""La relación entre la longitud de una circunferencia y su diámetro (pi)"""