"""控管垃圾資料回收機制 (gc)"""
from typing import overload

def enable() -> None:
    """啟用自動垃圾收集。 (啟用)"""
    ...

def disable() -> None:
    """停用自動垃圾收集。 (停用)

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """執行垃圾資料回收。 (收集)"""
    ...

def mem_alloc() -> int:
    """獲取分配的堆積 RAM 的位元組。 (記憶體分配)

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """獲取可用堆積 RAM 的位元組，如果此數量未知，則為 -1。 (mem free)

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """查詢額外的GC分配閾值。 (閾值)

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """設定額外的 GC 分配閾值。 (閾值)

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

:param amount: (數量) 應該觸發垃圾回收的位元組。"""
    ...