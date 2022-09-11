"""生成随机数。 (随机数)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """生成一个具有``n``个随机位的整数。 (生成随机位)

Example: ``random.getrandbits(1)``

:param n: 一个在1到30之间（包含30）的数值。"""
    ...

def seed(n: int) -> None:
    """初始化随机数生成器。 (种子)

Example: ``random.seed(0)``

:param n: 整数种子

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """在``a``到``b``（包含``b``）之间随机选择一个整数。 (随机整数)

Example: ``random.randint(0, 9)``

:param a: 区间起始值（包含）
:param b: 区间结束值（包含）

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """在零到``stop``（不含``stop``）之间随机选择一个整数。 (随机区间)

Example: ``random.randrange(10)``

:param stop: (结束值) 区间结束值（不含）"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """从区间``range(start, stop, step)``中随机选择一个元素。 (随机区间)

Example: ``random.randrange(0, 10)``

:param start: (起始值) 区间起始值（包含）
:param stop: (结束值) 区间结束值（不含）
:param step: (步长) 步长。"""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """从非空序列``seq``中选择一个随机元素。 (选择)

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: (序列) 序列。

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """在区间[0.0, 1.0)内生成一个随机浮点数。 (随机)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """返回一个介于``a``和``b``（包含``b``）之间的随机浮点数。 (均匀分布随机数)

Example: ``random.uniform(0, 9)``

:param a: 区间起始值（包含）
:param b: 区间结束值（包含）"""
    ...