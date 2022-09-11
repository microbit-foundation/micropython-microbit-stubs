"""乱数を生成します。"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """``n`` 乱数ビット数を持つ整数を生成します。

Example: ``random.getrandbits(1)``

:param n: 1～30の値（指定の値を含みます）。"""
    ...

def seed(n: int) -> None:
    """乱数ジェネレータを初期化します。

Example: ``random.seed(0)``

:param n: 整数シード

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """``a``  から ``b`` の区間内のランダムな整数値を返します（指定の値を含みます）。

Example: ``random.randint(0, 9)``

:param a: (A) 乱数区間の開始値（指定の値を含みます）
:param b: 乱数区間の終了値（指定の値を含みます）

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """0 から ``stop`` 未満までの間で無作為に選択された整数を返します。

Example: ``random.randrange(10)``

:param stop: 乱数区間の終了値（指定の値を含みません）"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """``range(start, stop, step)`` から無作為に選択された整数を返します。

Example: ``random.randrange(0, 10)``

:param start: 乱数区間の開始値（指定の値を含みます）
:param stop: 乱数区間の終了値（指定の値を含みません）
:param step: ステップ値。"""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """空でないシーケンス ``seq`` からランダムな要素を返します。

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: シーケンス。

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """0.0 以上、1.0 未満の区間から無作為に選択された浮動小数点数を生成します。

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """``a`` から ``b`` の区間内のランダムな浮動小数点数を返します（指定の値を含みます）。

Example: ``random.uniform(0, 9)``

:param a: (A) 乱数区間の開始値（指定の値を含みます）
:param b: 乱数区間の終了値（指定の値を含みます）"""
    ...