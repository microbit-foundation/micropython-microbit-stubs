"""crwdns328732:0crwdne328732:0 (crwdns328730:0crwdne328730:0)"""
from typing import overload

def enable() -> None:
    """crwdns328736:0crwdne328736:0 (crwdns328734:0crwdne328734:0)"""
    ...

def disable() -> None:
    """crwdns328740:0crwdne328740:0 (crwdns328738:0crwdne328738:0)

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """crwdns328744:0crwdne328744:0 (crwdns328742:0crwdne328742:0)"""
    ...

def mem_alloc() -> int:
    """crwdns328748:0crwdne328748:0 (crwdns328746:0crwdne328746:0)

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """crwdns328752:0crwdne328752:0 (crwdns328750:0crwdne328750:0)

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """crwdns328756:0crwdne328756:0 (crwdns328754:0crwdne328754:0)

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """crwdns328760:0crwdne328760:0 (crwdns328758:0crwdne328758:0)

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

:param amount: (crwdns328762:0crwdne328762:0) crwdns328764:0crwdne328764:0"""
    ...