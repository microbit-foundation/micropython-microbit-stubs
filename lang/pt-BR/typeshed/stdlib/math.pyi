"""Funções matemáticas. (matemática)"""
from typing import Tuple

def acos(x: float) -> float:
    """Calcule o cosseno inverso. (arco de cosseno)

Example: ``math.acos(1)``

:param x: Um número
:return: The inverse cosine of ``x``"""
    ...

def asin(x: float) -> float:
    """Calcule o seno inverso.

Example: ``math.asin(0)``

:param x: Um número
:return: The inverse sine of ``x``"""
    ...

def atan(x: float) -> float:
    """Calcule a tangente inversa.

Example: ``math.atan(0)``

:param x: Um número
:return: The inverse tangent of ``x``"""
    ...

def atan2(y: float, x: float) -> float:
    """Calcule o valor principal da tangente inversa de ``y/x``.

Example: ``math.atan2(0, -1)``

:param y: Um número
:param x: Um número
:return: The principal value of the inverse tangent of ``y/x``"""
    ...

def ceil(x: float) -> float:
    """Arredondar um número para um infinito positivo. (cego)

Example: ``math.ceil(0.1)``

:param x: Um número
:return: ``x`` rounded towards positive infinity."""
    ...

def copysign(x: float, y: float) -> float:
    """Calcule ``x`` com o sinal de ``y``. (cópia)

Example: ``math.copysign(1, -1)``

:param x: Um número
:param y: A fonte do sinal para o valor de retorno
:return: ``x`` with the sign of ``y``"""
    ...

def cos(x: float) -> float:
    """Calcule o cosseno de ``x``.

Example: ``math.cos(0)``

:param x: Um número
:return: The cosine of ``x``"""
    ...

def degrees(x: float) -> float:
    """Converte radianos em graus (Graus)

Example: ``math.degrees(2 * math.pi)``

:param x: Um valor em radianos
:return: The value converted to degrees"""
    ...

def exp(x: float) -> float:
    """Calcule o exponencial de ``x``.

Example: ``math.exp(1)``

:param x: Um número
:return: The exponential of ``x``."""
    ...

def fabs(x: float) -> float:
    """Retorna o valor absoluto de ``x``.

Example: ``math.fabs(-0.1)``

:param x: Um número
:return: The absolute value of ``x``"""
    ...

def floor(x: float) -> int:
    """Arredonde um número para o infinito negativo. (piso)

Example: ``math.floor(0.9)``

:param x: Um número
:return: ``x`` rounded towards negative infinity."""
    ...

def fmod(x: float, y: float) -> float:
    """Calcule o resto de ``x/y``.

Example: ``math.fmod(10, 3)``

:param x: O numerador
:param y: Denominador da Escala"""
    ...

def frexp(x: float) -> Tuple[float, int]:
    """Decompõe um número de ponto flutuante em sua mantissa e expoente.

Example: ``mantissa, exponent = math.frexp(2)``

The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
the relation ``0.5 <= abs(m) < 1`` holds.

:param x: Número de ponto flutuante
:return: A tuple of length two containing its mantissa then exponent"""
    ...

def isfinite(x: float) -> bool:
    """Verificar se um valor é finito. (isfinito)

Example: ``math.isfinite(float('inf'))``

:param x: Um número.
:return: ``True`` if ``x`` is finite, ``False`` otherwise."""
    ...

def isinf(x: float) -> bool:
    """Verifique se um valor é infinito.

Example: ``math.isinf(float('-inf'))``

:param x: Um número.
:return: ``True`` if ``x`` is infinite, ``False`` otherwise."""
    ...

def isnan(x: float) -> bool:
    """A verificação é um valor não é um número (NaN). (énue)

Example: ``math.isnan(float('nan'))``

:param x: Um número
:return: ``True`` if ``x`` is not-a-number (NaN), ``False`` otherwise."""
    ...

def ldexp(x: float, exp: int) -> float:
    """Calcular ``x * (2**exp)``. (Idexp)

Example: ``math.ldexp(0.5, 2)``

:param x: Um número
:param exp: Expoente inteiro
:return: ``x * (2**exp)``"""
    ...

def log(x: float, base: float=e) -> float:
    """Calcule o logaritmo de ``x`` para a base determinada (o padrão é de logaritmo natural).

Example: ``math.log(math.e)``

With one argument, return the natural logarithm of x (to base e).

With two arguments, return the logarithm of x to the given base, calculated as ``log(x)/log(base)``.

:param x: Um número
:param base: A base para usar
:return: The natural logarithm of ``x``"""
    ...

def modf(x: float) -> Tuple[float, float]:
    """Calcule as partes fracionária e integral de ``x``.

Example: ``fractional, integral = math.modf(1.5)``

:param x: Um número
:return: A tuple of two floats representing the fractional then integral parts of ``x``.

Both the fractional and integral values have the same sign as ``x``."""
    ...

def pow(x: float, y: float) -> float:
    """Retorna ``x`` à potência de ``y``.

Example: ``math.pow(4, 0.5)``

:param x: Um número
:param y: O expoente
:return: ``x`` to the power of ``y``"""
    ...

def radians(x: float) -> float:
    """Converta graus em radianos. (radianos)

Example: ``math.radians(360)``

:param x: Um valor em graus
:return: The value converted to radians"""
    ...

def sin(x: float) -> float:
    """Calcule o seno de ``x``. (seno)

Example: ``math.sin(math.pi/2)``

:param x: Um número
:return: The sine of ``x``"""
    ...

def sqrt(x: float) -> float:
    """Calcule a raiz quadrada de ``x``.

Example: ``math.sqrt(4)``

:param x: Um número
:return: The square root of ``x``"""
    ...

def tan(x: float) -> float:
    """Calcule a tangente de ``x``. (tangente)

Example: ``math.tan(0)``

:param x: Um número
:return: The tangent of ``x``."""
    ...

def trunc(x: float) -> int:
    """Arredonde um número para 0.

Example: ``math.trunc(-0.9)``

:param x: Um número
:return: ``x`` rounded towards zero."""
    ...
e: float
"""Base do logaritmo natural"""
pi: float
"""A razão entre a circunferência de um círculo e seu diâmetro"""