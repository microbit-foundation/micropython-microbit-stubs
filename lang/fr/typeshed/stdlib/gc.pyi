"""Contrôler le ramasse-miettes"""
from typing import overload

def enable() -> None:
    """Active la collecte automatique du ramasse-miettes."""
    ...

def disable() -> None:
    """Désactive la collecte automatique du ramasse-miettes.

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """Exécute une collecte avec le ramasse-miettes"""
    ...

def mem_alloc() -> int:
    """Obtenir le nombre d'octets alloués pour le tas en RAM

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """Obtenir le nombre d'octets disponibles pour le tas en RAM, ou -1 si ce nombre est inconnu.

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """Demander le seuil d'allocation supplémentaire GC.

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """Fixer le seuil d'allocation supplémentaire GC.

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

:param amount: Le nombre d'octets après lequel un passage du ramasse-miettes doit être déclenché."""
    ...