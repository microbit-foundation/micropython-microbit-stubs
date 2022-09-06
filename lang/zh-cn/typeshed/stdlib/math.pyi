"""数学函数。 (math)"""
from typing import Tuple

def acos(x: float) -> float:
    """计算反余弦。 (acos)

Example: ``math.acos(1)``

:param x: (x) 一个数字
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """计算反正弦值。 (asin)

Example: ``math.asin(0)``

:param x: (x) 一个数字
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """计算反正切。 (atan)

Example: ``math.atan(0)``

:param x: (x) 一个数字
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """计算 ``y/x`` 的反正切的主值。 (atan2)

Example: ``math.atan2(0, -1)``

:param y: (x) 一个数字
:param x: (x) 一个数字
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """
将数字向正无穷大取整(向上取整) (ceil)

Example: ``math.ceil(0.1)``

:param x: (x) 一个数字
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """获取 ``y`` 的符号和 ``x``的绝对值。 (copysign)

Example: ``math.copysign(1, -1)``

:param x: (x) 一个数字
:param y: (y) 返回值的符号来源
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """计算 ``x`` 的余弦。 (cos)

Example: ``math.cos(0)``

:param x: (x) 一个数字
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """将弧度转换为度。 (degrees)

Example: ``math.degrees(2 * math.pi)``

:param x: (x) 一个以弧度为单位的值
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """计算E的``x``指数。 (exp)

Example: ``math.exp(1)``

:param x: (x) 一个数字
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """返回``x`` 的绝对值。 (fabs)

Example: ``math.fabs(-0.1)``

:param x: (x) 一个数字
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """将数字向负无穷大取整(向下取整)。 (floor)

Example: ``math.floor(0.9)``

:param x: (x) 一个数字
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """计算 ``x/y`` 的余数。 (fmod)

Example: ``math.fmod(10, 3)``

:param x: (x) 分子
:param y: (y) 分母"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """将一个浮点数分解为其尾数和指数。 (frexp)

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: (x) 一个浮点数
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """检查值是否有限。 (isfinite)

Example: ``math.isfinite(float('inf'))``

:param x: (x) 一个数字。
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """检查值是否无限。 (isinf)

Example: ``math.isinf(float('-inf'))``

:param x: (x) 一个数字。
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """检查一个值是否不是一个数字 (NaN)。 (isnan)

Example: ``math.isnan(float('nan'))``

:param x: (x) 一个数字
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """计算 ``x * (2**exp)`` 。 (ldexp)

Example: ``math.ldexp(0.5, 2)``

:param x: (x) 一个数字
:param exp: (exp) 整数指数
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """计算给定底数 ``x`` 的对数（默认为自然对数）。 (log)

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: (x) 一个数字
:param base: (base) 要使用的底数
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """计算 ``x`` 的小数和整数部分。 (modf)

Example: ``fractional, integral = math.modf(1.5)``

:param x: (x) 一个数字
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """返回 ``x`` 的 ``y``次幂。 (pow)

Example: ``math.pow(4, 0.5)``

:param x: (x) 一个数字
:param y: (y) 指数值
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """将度数转换为弧度。 (radians)

Example: ``math.radians(360)``

:param x: (x) 以度为单位的值
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """
计算 ``x`` 的正弦值。 (sin)

Example: ``math.sin(math.pi/2)``

:param x: (x) 一个数字
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """计算 ``x`` 的平方根。 (sqrt)

Example: ``math.sqrt(4)``

:param x: (x) 一个数字
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """计算 ``x`` 的正切。 (tan)

Example: ``math.tan(0)``

:param x: (x) 一个数字
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """将数字向 0 舍入。 (trunc)

Example: ``math.trunc(-0.9)``

:param x: (x) 一个数字
:return: ``x`` rounded towards zero."""
    ...
e: float
"""自然对数的底数 (e)"""
pi: float
"""圆的周长与其直径的比值 (pi)"""