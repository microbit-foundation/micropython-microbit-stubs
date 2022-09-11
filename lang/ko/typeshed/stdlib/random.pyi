"""무작위 숫자를 생성합니다."""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """무작위 비트가 ``n``개 있는 정수를 생성합니다.

Example: ``random.getrandbits(1)``

:param n: 1~30 사이의 값입니다(경계값 포함)."""
    ...

def seed(n: int) -> None:
    """무작위 숫자 생성기를 초기화합니다.

Example: ``random.seed(0)``

:param n: 정수 시드

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """``a``부터 ``b``까지 중 무작위 정수를 선택합니다(경계값 포함).

Example: ``random.randint(0, 9)``

:param a: 범위 시작 값(경계값 포함)
:param b: 범위 종료 값(경계값 포함)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """0과``stop``사이의 무작위 정수를 선택합니다(경계값 제외).

Example: ``random.randrange(10)``

:param stop: 범위 종료 값(경계값 제외)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """``range(start, stop, step)``에서 무작위로 정해지는 요소를 선택합니다.

Example: ``random.randrange(0, 10)``

:param start: 범위 시작(경계값 포함)
:param stop: 범위 끝(경계값 제외)
:param step: 걸음 수입니다."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """공백이 아닌 ``seq`` 시퀀스로부터 무작위 요소를 선택합니다.

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: 시퀀스입니다.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """[0.0, 1.0) 범위 내의 무작위 부동 소수점 수를 생성합니다.

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """경계값을 포함한 ``a``와 ``b``사이의 무작위 부동 소수점 수를 반환합니다.

Example: ``random.uniform(0, 9)``

:param a: 범위 시작 값(경계값 포함)
:param b: 범위 종료 값(경계값 포함)"""
    ...