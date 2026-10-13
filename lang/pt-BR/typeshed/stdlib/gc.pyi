"""Controle o coletor de lixo"""
from typing import overload

def enable() -> None:
    """Ativar coleta automática de lixo. (Ativado)"""
    ...

def disable() -> None:
    """Ativar coleta automática de lixo. (desativado)

Heap memory can still be allocated,
and garbage collection can still be initiated manually using ``gc.collect``."""

def collect() -> None:
    """Executa uma coleta de lixo. (Coletar)"""
    ...

def mem_alloc() -> int:
    """Obter o número de bites de memória RAM oca que são alocados.

:return: The number of bytes allocated.

This function is MicroPython extension."""
    ...

def mem_free() -> int:
    """Obtenha o número de bytes de memória RAM disponível, ou -1 se este valor não for conhecido. (Memória livre)

:return: The number of bytes free.

This function is MicroPython extension."""
    ...

@overload
def threshold() -> int:
    """Consulta o limiar de alocação de coleta de lixo adicional. (limite)

:return: The GC allocation threshold.

This function is a MicroPython extension. CPython has a similar
function - ``set_threshold()``, but due to different GC
implementations, its signature and semantics are different."""
    ...

@overload
def threshold(amount: int) -> None:
    """Defina o limite de alocação de coleta de lixo adicional. (limite)

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

:param amount: (Quantidade) O número de bytes para os quais uma coleta de lixo deve ser acionada."""
    ...