"""Wiskundige functies. (wiskunde)"""
from typing import Tuple

def acos(x: float) -> float:
    """Bereken de inverse cosinus.

Example: ``math.acos(1)``

:param x: (х) Een getal
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Bereken de inverse sinus.

Example: ``math.asin(0)``

:param x: (х) Een getal
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Bereken de inverse tangens.

Example: ``math.atan(0)``

:param x: (х) Een getal
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Bereken de hoofdwaarde van de inverse tangens van ``y/x``.

Example: ``math.atan2(0, -1)``

:param y: (х) Een getal
:param x: (х) Een getal
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Rond een getal af op een positief oneindig. (plafond)

Example: ``math.ceil(0.1)``

:param x: (х) Een getal
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Bereken ``x`` met de teken van ``y``.

Example: ``math.copysign(1, -1)``

:param x: (х) Een getal
:param y: De bron van het teken voor de retourwaarde
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Bereken de cosinus van ``x``.

Example: ``math.cos(0)``

:param x: (х) Een getal
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """radialen converteren naar graden: (graden)

Example: ``math.degrees(2 * math.pi)``

:param x: (х) Een waarde in radialen
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Bereken de exponentiële van ``x``.

Example: ``math.exp(1)``

:param x: (х) Een getal
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Geeft de absolute waarde van ``x``.

Example: ``math.fabs(-0.1)``

:param x: (х) Een getal
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Rond een getal af op een negatief oneindig.

Example: ``math.floor(0.9)``

:param x: (х) Een getal
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Bereken de rest van ``x/y``.

Example: ``math.fmod(10, 3)``

:param x: (х) De nummeraar
:param y: De noemer"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Ontleedt een getal met drijvende komma in zijn mantisse en exponent.

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: (х) Getal met drijvende komma
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Controleer of een waarde eindig is. (is eindig)

Example: ``math.isfinite(float('inf'))``

:param x: (х) Een getal.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Controleer of een waarde oneindig is.

Example: ``math.isinf(float('-inf'))``

:param x: (х) Een getal.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """Check if is een waarde is geen getal (NaN).

Example: ``math.isnan(float('nan'))``

:param x: (х) Een getal
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """Bereken ``x * (2**exp)``.

Example: ``math.ldexp(0.5, 2)``

:param x: (х) Een getal
:param exp: Integer exponent
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Bereken het logaritme van ``x`` naar de opgegeven basis (standaard is het natuurlijke logalgoritme).

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: (х) Een getal
:param base: (grondtal) Het grondtal om te gebruiken
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Bereken de fractionele en integrale onderdelen van ``x``.

Example: ``fractional, integral = math.modf(1.5)``

:param x: (х) Een getal
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Retourneert ``x`` naar de kracht van ``y``.

Example: ``math.pow(4, 0.5)``

:param x: (х) Een getal
:param y: De exponent
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Converteer graden naar radialen. (radialen)

Example: ``math.radians(360)``

:param x: (х) Een waarde in graden
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Bereken de sinus van ``x``.

Example: ``math.sin(math.pi/2)``

:param x: (х) Een getal
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Bereken de wortel van ``x``. (wortel)

Example: ``math.sqrt(4)``

:param x: (х) Een getal
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Bereken de tangens van ``x``.

Example: ``math.tan(0)``

:param x: (х) Een getal
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Rond een getal af naar 0.

Example: ``math.trunc(-0.9)``

:param x: (х) Een getal
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Basis van het natuurlijke logaritme"""
pi: float
"""De omtrek van een cirkel tot de diameter"""