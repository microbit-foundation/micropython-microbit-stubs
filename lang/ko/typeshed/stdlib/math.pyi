"""수학 함수입니다."""
from typing import Tuple

def acos(x: float) -> float:
    """코사인의 역을 계산합니다.

Example: ``math.acos(1)``

:param x: 숫자
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """사인의 역을 계산합니다.

Example: ``math.asin(0)``

:param x: 숫자
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """탄젠트의 역을 계산합니다.

Example: ``math.atan(0)``

:param x: 숫자
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """``y/x``의 역 탄젠트의 주 값을 계산합니다.

Example: ``math.atan2(0, -1)``

:param y: 숫자
:param x: 숫자
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """양의 무한대로 숫자를 반올림합니다.

Example: ``math.ceil(0.1)``

:param x: 숫자
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """``y``의 사인 값으로 ``x``를 계산합니다.

Example: ``math.copysign(1, -1)``

:param x: 숫자
:param y: 반환값의 사인의 출처
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """``x``의 코사인을 계산합니다.

Example: ``math.cos(0)``

:param x: 숫자
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """호도법을 각도법으로 변환합니다. (도)

Example: ``math.degrees(2 * math.pi)``

:param x: 호도법 값
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """``x``의 지수를 계산합니다.

Example: ``math.exp(1)``

:param x: 숫자
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """``x``의 절댓값을 반환합니다.

Example: ``math.fabs(-0.1)``

:param x: 숫자
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """음의 무한대로 숫자를 반올림합니다.

Example: ``math.floor(0.9)``

:param x: 숫자
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """``x/y``의 나머지를 계산합니다.

Example: ``math.fmod(10, 3)``

:param x: 분자
:param y: 분모"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """부동 소수점 수를 가수와 지수로 분해합니다.

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: 부동 소수점 수
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """값이 유한값인지 확인합니다.

Example: ``math.isfinite(float('inf'))``

:param x: 숫자입니다.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """값이 무한인지 확인합니다.

Example: ``math.isinf(float('-inf'))``

:param x: 숫자입니다.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """값이 숫자가 아닌 값(NaN)인지 확인합니다.

Example: ``math.isnan(float('nan'))``

:param x: 숫자
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """``x * (2**exp)``를 계산합니다.

Example: ``math.ldexp(0.5, 2)``

:param x: 숫자
:param exp: 정수 지수
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """``x``의 로그를 주어진 베이스에 따라 계산합니다(기본값은 자연로그).

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: 숫자
:param base: 사용할 베이스
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """``x``의 분수 및 정수 부분을 계산합니다.

Example: ``fractional, integral = math.modf(1.5)``

:param x: 숫자
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """``y``의 제곱을 ``x``(으)로 반환합니다.

Example: ``math.pow(4, 0.5)``

:param x: 숫자
:param y: 지수
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """각도법을 호도법으로 변환합니다.

Example: ``math.radians(360)``

:param x: 각도법 값
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """``x``의 사인을 계산합니다.

Example: ``math.sin(math.pi/2)``

:param x: 숫자
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """``x``의 제곱근을 계산합니다.

Example: ``math.sqrt(4)``

:param x: 숫자
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """``x``의 탄젠트를 계산합니다.

Example: ``math.tan(0)``

:param x: 숫자
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """숫자를 0으로 반올림합니다.

Example: ``math.trunc(-0.9)``

:param x: 숫자
:return: ``x`` rounded towards zero."""
    ...
e: float
"""자연 알고리즘 베이스"""
pi: float
"""원의 원주와 지름의 비율"""