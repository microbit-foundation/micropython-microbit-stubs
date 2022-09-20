"""控制垃圾回收器 (垃圾回收(gc))"""
from typing import overload

def enable() -> None:
    """启用自动垃圾回收机制。"""
    ...

def disable() -> None:
    """禁用自动垃圾回收机制。

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """执行一次垃圾回收。"""
    ...

def mem_alloc() -> int:
    """获取分配的堆内存的字节数。

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """获取可用堆内存的字节数，如果此数量未知，则返回值为 -1。

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """查询额外的垃圾回收分配阈值。

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """设置额外的垃圾回收分配阈值。

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

:param amount: 触发进行垃圾回收的字节数。"""
    ...