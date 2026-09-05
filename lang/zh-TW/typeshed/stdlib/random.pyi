"""生成隨機數。"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """生成具有 ``n`` 個隨機位元的整數。

Example: ``random.getrandbits(1)``

:param n: 介於 1-30 (包含) 之間的值。"""
    ...

def seed(n: int) -> None:
    """初始化隨機數生成器。

Example: ``random.seed(0)``

:param n: 整數種子

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """在 ``a`` 和 ``b`` (包含) 之間選擇一個隨機整數。

Example: ``random.randint(0, 9)``

:param a: 範圍的起始值 (包含)
:param b: 範圍的結束值 (包含)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """在零到 (但不包括) ``stop`` 之間隨機選擇一個整數。

Example: ``random.randrange(10)``

:param stop: 範圍的結束值 (排除)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """從 ``range(start, stop, step)`` 中選擇一個隨機選擇的元素。

Example: ``random.randrange(0, 10)``

:param start: 範圍的開始 (包含)
:param stop: 範圍結束 (排除)
:param step: 步驟。"""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """從非空序列 ``seq`` 中選擇一個隨機元素。

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: 序列。

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """在 [0.0, 1.0) 範圍內生成一個隨機浮點數。

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """傳回一個介於 ``a`` 和 ``b`` 之間的隨機浮點數。

Example: ``random.uniform(0, 9)``

:param a: 範圍的起始值 (包括)
:param b: 範圍的結束值 (包含)"""
    ...