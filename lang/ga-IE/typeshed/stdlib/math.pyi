"""Feidhmeanna matamaiticiúla. (mata)"""
from typing import Tuple

def acos(x: float) -> float:
    """Ríomh an cosine inbhéartach.

Example: ``math.acos(1)``

:param x: Uimhir
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Ríomh an sine inbhéartach.

Example: ``math.asin(0)``

:param x: Uimhir
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Ríomh an tadhlaí inbhéartach.

Example: ``math.atan(0)``

:param x: Uimhir
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Ríomh príomhluach an tadhlaí inbhéartach de ``y/x``.

Example: ``math.atan2(0, -1)``

:param y: Uimhir
:param x: Uimhir
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Déan roinnt a shlánú i dtreo éigríochta dearfach. (síleáil)

Example: ``math.ceil(0.1)``

:param x: Uimhir
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Ríomh ``x`` le comhartha ``y``. (cóipchomhartha)

Example: ``math.copysign(1, -1)``

:param x: Uimhir
:param y: Foinse an chomhartha don luach fillte
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Ríomh an comhshíneas de ``x``.

Example: ``math.cos(0)``

:param x: Uimhir
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """Raidian Tiontaigh go céimeanna. (céimeanna)

Example: ``math.degrees(2 * math.pi)``

:param x: Luach i radaíní
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Ríomh easpónantúil ``x``.

Example: ``math.exp(1)``

:param x: Uimhir
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Tabhair luach absalóideach ``x``ar ais.

Example: ``math.fabs(-0.1)``

:param x: Uimhir
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Babhtaigh uimhir i dtreo éigríoch diúltach. (urlár)

Example: ``math.floor(0.9)``

:param x: Uimhir
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Ríomh an chuid eile de ``x/y``.

Example: ``math.fmod(10, 3)``

:param x: An t-uimhreoir
:param y: An t-ainmneoir"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Díscaoileann sé uimhir snámhphointe isteach ina mantissa agus ina easpónant.

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: Uimhir snámhphointe
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Seiceáil an bhfuil luach críochta. (isfinideach)

Example: ``math.isfinite(float('inf'))``

:param x: Uimhir.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Seiceáil an bhfuil luach gan teorainn.

Example: ``math.isinf(float('-inf'))``

:param x: Uimhir
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """Seiceáil an luach nach uimhir é (NaN).

Example: ``math.isnan(float('nan'))``

:param x: Uimhir
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """Ríomh ``x * (2**exp)``.

Example: ``math.ldexp(0.5, 2)``

:param x: Uimhir
:param exp: Easpónant slánuimhir
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Ríomh logarithm ``x`` go dtí an bonn tugtha (réamhshocraithe don logarithm nádúrtha). (loga)

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: Uimhir
:param base: (bonn) An bonn le húsáid
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Ríomh na codanna codánacha agus lárnacha de ``x``.

Example: ``fractional, integral = math.modf(1.5)``

:param x: Uimhir
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Filleann ``x`` chuig cumhacht ``y``.

Example: ``math.pow(4, 0.5)``

:param x: Uimhir
:param y: An léiritheoir
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Tiontaigh céimeanna go raidian. (raidiáin)

Example: ``math.radians(360)``

:param x: Luach i gcéimeanna
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Ríomh an sín de ``x``. (síneas)

Example: ``math.sin(math.pi/2)``

:param x: Uimhir
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Ríomh an fhréamh chearnach de ``x``.

Example: ``math.sqrt(4)``

:param x: Uimhir
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Ríomh an tadhlaí de ``x``.

Example: ``math.tan(0)``

:param x: Uimhir
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Déan uimhir a shlánú i dtreo 0.

Example: ``math.trunc(-0.9)``

:param x: Uimhir
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Bunús an logartaim nádúrtha"""
pi: float
"""An cóimheas idir imlíne ciorcail agus a thrastomhas"""