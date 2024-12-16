"""ガベージコレクターを制御します。"""
from typing import overload

def enable() -> None:
    """自動ガベージコレクションを有効にします。"""
    ...

def disable() -> None:
    """自動ガベージコレクションを無効にします。

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """ガベージコレクションを実行します。"""
    ...

def mem_alloc() -> int:
    """割り当てられているヒープRAMのバイト数を取得します。

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """使用可能なヒープRAMのバイト数を取得します。この量が不明の場合は -1が返されます。

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """追加のGC 割り当てしきい値を照会します。

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """追加の GC 割り当てしきい値を設定します。

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

:param amount: ガベージコレクションを起こすバイト数。"""
    ...