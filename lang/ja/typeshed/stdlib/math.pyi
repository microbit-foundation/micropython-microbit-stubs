"""数学関数。"""
from typing import Tuple

def acos(x: float) -> float:
    """逆余弦を算出します。

Example: ``math.acos(1)``

:param x: 数値
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """逆正弦を算出します。

Example: ``math.asin(0)``

:param x: 数値
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """逆正接を算出します。

Example: ``math.atan(0)``

:param x: 数値
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """``y/x`` の逆正接の主値を算出します。

Example: ``math.atan2(0, -1)``

:param y: 数値
:param x: 数値
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """正の無限大方向に数値を丸めます。

Example: ``math.ceil(0.1)``

:param x: 数値
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """``y`` の符号で ``x`` を算出します。

Example: ``math.copysign(1, -1)``

:param x: 数値
:param y: 戻り値の符号の元になる値
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """``x`` の余弦を算出します。

Example: ``math.cos(0)``

:param x: 数値
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """ラジアンを度に変換します。 (゜(度))

Example: ``math.degrees(2 * math.pi)``

:param x: ラジアン単位の値
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """``x`` の指数を算出します。

Example: ``math.exp(1)``

:param x: 数値
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """``x`` の絶対値を返します。

Example: ``math.fabs(-0.1)``

:param x: 数値
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """負の無限大方向に数値を丸めます。

Example: ``math.floor(0.9)``

:param x: 数値
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """``x/y`` の剰余を算出します。

Example: ``math.fmod(10, 3)``

:param x: 分子の値
:param y: 分母の値"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """浮動小数点数を仮数部と指数部に分解します。

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: 浮動小数点数
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """有限数かどうかを確認します。

Example: ``math.isfinite(float('inf'))``

:param x: 数値。
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """無限数かどうかを確認します。

Example: ``math.isinf(float('-inf'))``

:param x: 数値。
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """非数（NaN: Not-a-Number）かどうかを確認します。

Example: ``math.isnan(float('nan'))``

:param x: 数値
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """``x * (2**exp)`` を算出します。

Example: ``math.ldexp(0.5, 2)``

:param x: 数値
:param exp: 整数の指数
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """``x`` の対数を指定された底（デフォルトは自然対数）で算出します。

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: 数値
:param base: 使用する底
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """``x`` の整数部分と小数部分を返します。

Example: ``fractional, integral = math.modf(1.5)``

:param x: 数値
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """``x`` の ``y`` 乗を返します。

Example: ``math.pow(4, 0.5)``

:param x: 数値
:param y: 指数
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """度をラジアンに変換します。

Example: ``math.radians(360)``

:param x: 度単位の角度
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """``x`` の正弦を算出します。

Example: ``math.sin(math.pi/2)``

:param x: 数値
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """``x`` の平方根を算出します。

Example: ``math.sqrt(4)``

:param x: 数値
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """``x`` の正接を算出します。

Example: ``math.tan(0)``

:param x: 数値
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """0 方向に数値を丸めます。

Example: ``math.trunc(-0.9)``

:param x: 数値
:return: ``x`` rounded towards zero."""
    ...
e: float
"""自然対数の底"""
pi: float
"""円の円周と直径の比"""