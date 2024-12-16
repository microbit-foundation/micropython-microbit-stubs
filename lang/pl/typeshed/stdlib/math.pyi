"""Funkcje matematyczne."""
from typing import Tuple

def acos(x: float) -> float:
    """Obliczyć odwrotność cosinusa.

Example: ``math.acos(1)``

:param x: Liczba
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Obliczyć odwrotność sinusa.

Example: ``math.asin(0)``

:param x: Liczba
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Oblicz odwrotność tangensa.

Example: ``math.atan(0)``

:param x: Liczba
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Oblicz wartość główną odwrotności tangensa ``y/x``.

Example: ``math.atan2(0, -1)``

:param y: Liczba
:param x: Liczba
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Zaokrąglij liczbę w kierunku dodatniej nieskończoności.

Example: ``math.ceil(0.1)``

:param x: Liczba
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Oblicz ``x`` ze znakiem ``y``.

Example: ``math.copysign(1, -1)``

:param x: Liczba
:param y: Źródło znaku dla wartości zwracanej
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Oblicz cosinus ``x``.

Example: ``math.cos(0)``

:param x: Liczba
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """Konwertuj radiany na stopnie.

Example: ``math.degrees(2 * math.pi)``

:param x: Wartość w radianach
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Oblicz potęgę ``x``.

Example: ``math.exp(1)``

:param x: Liczba
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Zwróć wartość bezwzględną ``x``.

Example: ``math.fabs(-0.1)``

:param x: Liczba
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Zaokrąglij liczbę w kierunku ujemnej nieskończoności.

Example: ``math.floor(0.9)``

:param x: Liczba
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Oblicz resztę z ``x/y``.

Example: ``math.fmod(10, 3)``

:param x: Licznik
:param y: Mianownik"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Rozkłada liczbę zmiennopozycyjną na mantysę i wykładnik.

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: Liczba zmiennopozycyjna
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Sprawdź, czy wartość jest skończona.

Example: ``math.isfinite(float('inf'))``

:param x: Liczba.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Sprawdź, czy wartość jest nieskończona.

Example: ``math.isinf(float('-inf'))``

:param x: Liczba.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """Sprawdź, czy wartość nie jest liczbą (NaN).

Example: ``math.isnan(float('nan'))``

:param x: Liczba
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """Oblicz ``x * (2**exp)``.

Example: ``math.ldexp(0.5, 2)``

:param x: Liczba
:param exp: Wykładnik całkowity
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Oblicz logarytm z ``x`` przy podanej podstawie (domyślnie loggorytm naturalny).

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: Liczba
:param base: Podstawa do użycia
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Oblicz część ułamkową i całkowitą z ``x``.

Example: ``fractional, integral = math.modf(1.5)``

:param x: Liczba
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Zwraca ``x`` do potęgi ``y``.

Example: ``math.pow(4, 0.5)``

:param x: Liczba
:param y: Wykładnik
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Konwertuj stopnie na radiany.

Example: ``math.radians(360)``

:param x: Wartość w stopniach
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Oblicz sinus ``x``.

Example: ``math.sin(math.pi/2)``

:param x: Liczba
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Oblicz pierwiastek kwadratowy z ``x``.

Example: ``math.sqrt(4)``

:param x: Liczba
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Oblicz tangens z ``x``.

Example: ``math.tan(0)``

:param x: Liczba
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Zaokrąglij liczbę w kierunku 0.

Example: ``math.trunc(-0.9)``

:param x: Liczba
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Podstawa logarytmu naturalnego"""
pi: float
"""Stosunek obwodu okręgu do jego średnicy"""