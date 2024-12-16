"""Steruj zbieraniem śmieci"""
from typing import overload

def enable() -> None:
    """Włącz automatyczne zbieranie śmieci."""
    ...

def disable() -> None:
    """Wyłącz automatyczne zbieranie śmieci.

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """Uruchom zbieranie śmieci."""
    ...

def mem_alloc() -> int:
    """Znajdź liczbę przydzielonych bajtów sterty pamięci RAM.

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """Znajdź liczbę bajtów dostępnej sterty pamięci RAM lub -1, jeśli ta liczba nie jest znana.

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """Zapytanie o dodatkowy próg przydziału GC.

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """Ustaw próg dodatkowego przydziału GC.

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

:param amount: Liczba bajtów, po których powinno zostać uruchomione zbieranie śmieci."""
    ...