"""crwdns328912:0crwdne328912:0 (crwdns328910:0crwdne328910:0)"""
from typing import Tuple

def acos(x: float) -> float:
    """crwdns328916:0crwdne328916:0 (crwdns328914:0crwdne328914:0)

Example: ``math.acos(1)``

:param x: (crwdns328918:0crwdne328918:0) crwdns328920:0crwdne328920:0
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """crwdns328924:0crwdne328924:0 (crwdns328922:0crwdne328922:0)

Example: ``math.asin(0)``

:param x: (crwdns328926:0crwdne328926:0) crwdns328928:0crwdne328928:0
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """crwdns328932:0crwdne328932:0 (crwdns328930:0crwdne328930:0)

Example: ``math.atan(0)``

:param x: (crwdns328934:0crwdne328934:0) crwdns328936:0crwdne328936:0
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """crwdns328940:0``y/x``crwdne328940:0 (crwdns328938:0crwdne328938:0)

Example: ``math.atan2(0, -1)``

:param y: (crwdns328942:0crwdne328942:0) crwdns328944:0crwdne328944:0
:param x: (crwdns328942:0crwdne328942:0) crwdns328944:0crwdne328944:0
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """crwdns328952:0crwdne328952:0 (crwdns328950:0crwdne328950:0)

Example: ``math.ceil(0.1)``

:param x: (crwdns328954:0crwdne328954:0) crwdns328956:0crwdne328956:0
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """crwdns328960:0``x``crwdnd328960:0``y``crwdne328960:0 (crwdns328958:0crwdne328958:0)

Example: ``math.copysign(1, -1)``

:param x: (crwdns328962:0crwdne328962:0) crwdns328964:0crwdne328964:0
:param y: (crwdns328966:0crwdne328966:0) crwdns328968:0crwdne328968:0
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """crwdns328972:0``x``crwdne328972:0 (crwdns328970:0crwdne328970:0)

Example: ``math.cos(0)``

:param x: (crwdns328974:0crwdne328974:0) crwdns328976:0crwdne328976:0
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """crwdns328980:0crwdne328980:0 (crwdns328978:0crwdne328978:0)

Example: ``math.degrees(2 * math.pi)``

:param x: (crwdns328982:0crwdne328982:0) crwdns328984:0crwdne328984:0
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """crwdns328988:0``x``crwdne328988:0 (crwdns328986:0crwdne328986:0)

Example: ``math.exp(1)``

:param x: (crwdns328990:0crwdne328990:0) crwdns328992:0crwdne328992:0
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """crwdns328996:0``x``crwdne328996:0 (crwdns328994:0crwdne328994:0)

Example: ``math.fabs(-0.1)``

:param x: (crwdns328998:0crwdne328998:0) crwdns329000:0crwdne329000:0
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """crwdns329004:0crwdne329004:0 (crwdns329002:0crwdne329002:0)

Example: ``math.floor(0.9)``

:param x: (crwdns329006:0crwdne329006:0) crwdns329008:0crwdne329008:0
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """crwdns329012:0``x/y``crwdne329012:0 (crwdns329010:0crwdne329010:0)

Example: ``math.fmod(10, 3)``

:param x: (crwdns329014:0crwdne329014:0) crwdns329016:0crwdne329016:0
:param y: (crwdns329018:0crwdne329018:0) crwdns329020:0crwdne329020:0"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """crwdns329024:0crwdne329024:0 (crwdns329022:0crwdne329022:0)

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: (crwdns329026:0crwdne329026:0) crwdns329028:0crwdne329028:0
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """crwdns329032:0crwdne329032:0 (crwdns329030:0crwdne329030:0)

Example: ``math.isfinite(float('inf'))``

:param x: (crwdns329034:0crwdne329034:0) crwdns329036:0crwdne329036:0
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """crwdns329040:0crwdne329040:0 (crwdns329038:0crwdne329038:0)

Example: ``math.isinf(float('-inf'))``

:param x: (crwdns329042:0crwdne329042:0) crwdns329044:0crwdne329044:0
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """crwdns329048:0crwdne329048:0 (crwdns329046:0crwdne329046:0)

Example: ``math.isnan(float('nan'))``

:param x: (crwdns329050:0crwdne329050:0) crwdns329052:0crwdne329052:0
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """crwdns329056:0crwdne329056:0 (crwdns329054:0crwdne329054:0)

Example: ``math.ldexp(0.5, 2)``

:param x: (crwdns329062:0crwdne329062:0) crwdns329064:0crwdne329064:0
:param exp: (crwdns329058:0crwdne329058:0) crwdns329060:0crwdne329060:0
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """crwdns329068:0``x``crwdne329068:0 (crwdns329066:0crwdne329066:0)

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: (crwdns329074:0crwdne329074:0) crwdns329076:0crwdne329076:0
:param base: (crwdns329070:0crwdne329070:0) crwdns329072:0crwdne329072:0
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """crwdns329080:0``x``crwdne329080:0 (crwdns329078:0crwdne329078:0)

Example: ``fractional, integral = math.modf(1.5)``

:param x: (crwdns329082:0crwdne329082:0) crwdns329084:0crwdne329084:0
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """crwdns329088:0``x``crwdnd329088:0``y``crwdne329088:0 (crwdns329086:0crwdne329086:0)

Example: ``math.pow(4, 0.5)``

:param x: (crwdns329090:0crwdne329090:0) crwdns329092:0crwdne329092:0
:param y: (crwdns329094:0crwdne329094:0) crwdns329096:0crwdne329096:0
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """crwdns329100:0crwdne329100:0 (crwdns329098:0crwdne329098:0)

Example: ``math.radians(360)``

:param x: (crwdns329102:0crwdne329102:0) crwdns329104:0crwdne329104:0
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """crwdns329108:0``x``crwdne329108:0 (crwdns329106:0crwdne329106:0)

Example: ``math.sin(math.pi/2)``

:param x: (crwdns329110:0crwdne329110:0) crwdns329112:0crwdne329112:0
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """crwdns329116:0``x``crwdne329116:0 (crwdns329114:0crwdne329114:0)

Example: ``math.sqrt(4)``

:param x: (crwdns329118:0crwdne329118:0) crwdns329120:0crwdne329120:0
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """crwdns329124:0``x``crwdne329124:0 (crwdns329122:0crwdne329122:0)

Example: ``math.tan(0)``

:param x: (crwdns329126:0crwdne329126:0) crwdns329128:0crwdne329128:0
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """crwdns329132:0crwdne329132:0 (crwdns329130:0crwdne329130:0)

Example: ``math.trunc(-0.9)``

:param x: (crwdns329134:0crwdne329134:0) crwdns329136:0crwdne329136:0
:return: ``x`` rounded towards zero."""
    ...
e: float
"""crwdns329140:0crwdne329140:0 (crwdns329138:0crwdne329138:0)"""
pi: float
"""crwdns329144:0crwdne329144:0 (crwdns329142:0crwdne329142:0)"""