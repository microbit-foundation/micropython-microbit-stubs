"""가비지 컬렉터 제어"""
from typing import overload

def enable() -> None:
    """자동 가비지 컬렉션을 활성화합니다."""
    ...

def disable() -> None:
    """자동 가비지 컬렉션을 비활성화합니다.

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """가비지 컬렉션을 실행합니다."""
    ...

def mem_alloc() -> int:
    """할당된 힙 RAM의 바이트 수를 불러옵니다.

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """이용 가능한 힙 RAM의 바이트 수를 불러옵니다. 값을 알 수 없는 경우 -1을 반환합니다.

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """추가 GC 할당 임계값을 요청합니다.

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """추가 GC 할당 임계값을 설정합니다.

Normally, a collection is triggered only when a new allocation
cannot be satisfied, i.e. on an  out-of-memory (OOM) condition.
If this function is called, in addition to OOM, a collection
will be triggered each time after ``amount`` bytes have been
allocated (in total, since the previous time such an amount of bytes
have been allocated). ``amount`` is usually specified as less than the
full heap size, with the intention to trigger a collection earlier than when the
heap becomes exhausted, and in the hope that an early collection will prevent
excessive memory fragmentation. This is a heuristic measure, the effect
of which will vary from application to application, as well as
the optimal value of the ``amount`` parameter.

A value of -1 means a disabled allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different.

:param amount: 가비지 컬렉션이 트리거되는 바이트 수입니다."""
    ...