"""數學函數。 (math)"""
from typing import Tuple

def acos(x: float) -> float:
    """計算反餘弦。 (acos)

Example: ``math.acos(1)``

:param x: (x) 數字
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """計算反正弦值。 (asin)

Example: ``math.asin(0)``

:param x: (x) 數字
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """計算反正切。 (atan)

Example: ``math.atan(0)``

:param x: (x) 數字
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """計算 ``y/x`` 的反正切主值。 (atan2)

Example: ``math.atan2(0, -1)``

:param y: (x) 數字
:param x: (x) 數字
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """將數字向正無限大捨入。 (ceil)

Example: ``math.ceil(0.1)``

:param x: (x) 一個數字
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """用 ``y`` 的符號計算 ``x``。 (copysign)

Example: ``math.copysign(1, -1)``

:param x: (x) 數字
:param y: (y) 傳回值的符號來源
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """計算 ``x`` 的餘弦。 (cos)

Example: ``math.cos(0)``

:param x: (x) 一個數字
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """將 弧度(Radians) 轉換為 度(Degrees) (度)

Example: ``math.degrees(2 * math.pi)``

:param x: (x) 單位為度數的角度
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """計算 ``x`` 的指數。 (指數的)

Example: ``math.exp(1)``

:param x: (x) 一個數字
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """傳回 ``x`` 的絕對值。 (fabs)

Example: ``math.fabs(-0.1)``

:param x: (x) 數字
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """將數字向負無限大捨入。 (floor)

Example: ``math.floor(0.9)``

:param x: (x) 數字
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """計算 ``x/y`` 的餘數。 (fmod)

Example: ``math.fmod(10, 3)``

:param x: (x) 分子
:param y: (y) 分母"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """將浮點數分解為其尾數和指數。 (frexp)

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: (x) 浮點數
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """檢查值是否是有限的。 (isfinite)

Example: ``math.isfinite(float('inf'))``

:param x: (x) 數字。
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """檢查值是否是無限的。 (isinf)

Example: ``math.isinf(float('-inf'))``

:param x: (x) 數字。
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """檢查值是否不是數字 (NaN)。 (isnan)

Example: ``math.isnan(float('nan'))``

:param x: (x) 數字
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """計算 ``x * (2**exp)``。 (ldexp)

Example: ``math.ldexp(0.5, 2)``

:param x: (x) 數字
:param exp: (指數的) 整數指數
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """計算指定底數 ``x`` 的對數 (預設為自然對數)。 (log)

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: (x) 數字
:param base: (base) 要使用的底數
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """計算 ``x`` 的小數部分和整數部分。 (modf)

Example: ``fractional, integral = math.modf(1.5)``

:param x: (x) 數字
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """傳回 ``x`` 的 ``y`` 次方。 (pow)

Example: ``math.pow(4, 0.5)``

:param x: (x) 數字
:param y: (y) 指數
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """將角度轉換為弧度。 (radians)

Example: ``math.radians(360)``

:param x: (x) 以角度為單位的值
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """計算 ``x`` 的正弦。 (sin)

Example: ``math.sin(math.pi/2)``

:param x: (x) 數字
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """計算 ``x`` 的平方根。 (sqrt)

Example: ``math.sqrt(4)``

:param x: (x) 數字
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """計算 ``x`` 的正切。 (tan)

Example: ``math.tan(0)``

:param x: (x) 數字
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """將數字向 0 舍入。 (trunc)

Example: ``math.trunc(-0.9)``

:param x: (x) 數字
:return: ``x`` rounded towards zero."""
    ...
e: float
"""自然對數的底數 (e)"""
pi: float
"""圓的周長與其直徑的比率 (pi)"""