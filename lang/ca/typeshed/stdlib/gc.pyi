"""Controla el recol·lector de memòria brossa"""
from typing import overload

def enable() -> None:
    """Habilita la recol·lecció automàtica de la memòria brossa (habilita)"""
    ...

def disable() -> None:
    """Inhabilita la recol·lecció automàtica de la memòria brossa (desactiva)

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """Executa la recol·lecció automàtica de la memòria brossa (Recull)"""
    ...

def mem_alloc() -> int:
    """Obté el nombre de bytes assignats a la memòria dinàmica. (espai de memòria)

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """Obté el nombre disponible de bytes de la memòria dinàmica, o -1 si no es coneix la quantitat. (memòria lliure)

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """Consulta l'assignació del llindar del col·lector d'escombraries. (llindar)

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """Assigna un espai adicional al llindar del col·lector d'escombraries. (llindar)

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

:param amount: (quantitat) El nombre de bytes després del qual s'activarà la recol·lecció de la memòria brossa."""
    ...