"""Mathematical functions. ()"""
from typing import Tuple

def acos(x: float) -> float:
    """Calculate the inverse cosine. (acos)

Example: ``math.acos(1)``

:param x: (x) A number
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Calculate the inverse sine. (asin)

Example: ``math.asin(0)``

:param x: (x) A number
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Calculate the inverse tangent. (atan)

Example: ``math.atan(0)``

:param x: (x) A number
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Calculate the principal value of the inverse tangent of ``y/x``. (atan2)

Example: ``math.atan2(0, -1)``

:param y: (x) (y) A number
:param x: (x) (y) A number
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Round a number towards positive infinity. (ceil)

Example: ``math.ceil(0.1)``

:param x: (x) A number
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Calculate ``x`` with the sign of ``y``. (copysign)

Example: ``math.copysign(1, -1)``

:param x: (x) A number
:param y: (y) The source of the sign for the return value
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Calculate the cosine of ``x``. (cos)

Example: ``math.cos(0)``

:param x: (x) A number
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """Convert radians to degrees. (degrees)

Example: ``math.degrees(2 * math.pi)``

:param x: (x) A value in radians
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Calculate the exponential of ``x``. (exp)

Example: ``math.exp(1)``

:param x: (x) A number
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Return the absolute value of ``x``. (fabs)

Example: ``math.fabs(-0.1)``

:param x: (x) A number
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Round a number towards negative infinity. (floor)

Example: ``math.floor(0.9)``

:param x: (x) A number
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Calculate the remainder of ``x/y``. (fmod)

Example: ``math.fmod(10, 3)``

:param x: (x) The numerator
:param y: (y) The denominator"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Decomposes a floating-point number into its mantissa and exponent. (frexp)

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: (x) A floating-point number
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Check if a value is finite. (isfinite)

Example: ``math.isfinite(float('inf'))``

:param x: (x) A number.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Check if a value is infinite. (isinf)

Example: ``math.isinf(float('-inf'))``

:param x: (x) A number.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """Check is a value is not-a-number (NaN). (isnan)

Example: ``math.isnan(float('nan'))``

:param x: (x) A number
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """Calculate ``x * (2**exp)``. (ldexp)

Example: ``math.ldexp(0.5, 2)``

:param x: (x) A number
:param exp: (exp) Integer exponent
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Calculate the logarithm of ``x`` to the given base (defaults to natural logorithm). (log)

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: (x) A number
:param base: (base) The base to use
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Calculate the fractional and integral parts of ``x``. (modf)

Example: ``fractional, integral = math.modf(1.5)``

:param x: (x) A number
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Returns ``x`` to the power of ``y``. (pow)

Example: ``math.pow(4, 0.5)``

:param x: (x) A number
:param y: (y) The exponent
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Convert a degrees to radians. (radians)

Example: ``math.radians(360)``

:param x: (x) A value in degrees
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Calculate the sine of ``x``. (sin)

Example: ``math.sin(math.pi/2)``

:param x: (x) A number
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Calculate the square root of ``x``. (sqrt)

Example: ``math.sqrt(4)``

:param x: (x) A number
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Calculate the tangent of ``x``. (tan)

Example: ``math.tan(0)``

:param x: (x) A number
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Round a number towards 0. (trunc)

Example: ``math.trunc(-0.9)``

:param x: (x) A number
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Base of the natural logarithm (e)"""
pi: float
"""The ratio of a circle's circumference to its diameter (pi)"""