"""Controlar el recolector de basura (rb)"""
from typing import overload

def enable() -> None:
    """Activar la recolección automática de basura. (habilitado)"""
    ...

def disable() -> None:
    """Desactiva la recolección automática de basura. (deshabilitar)

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """Ejecuta una recolección de basura. (recoger)"""
    ...

def mem_alloc() -> int:
    """Obtiene el número de bytes asignados a la RAM dinámica. (memoria asignada)

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """Obtiene el número de bytes de la RAM dinámica disponible o -1 si se desconoce esta cantidad. (memoria libre)

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """Consulta el umbral de asignación de GC (recolector de basura) adicional. (límite)

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """Establece el umbral de asignación de GC (recolector de basura) adicional. (límite)

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

:param amount: (cantidad) Número de bytes después de los cuales se debe activar una recolección de basura."""
    ...