"""Funcions específiques del sistema"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """Finalitza el programa actual amb un codi de sortida determinat.

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: El codi o missatge de sortida."""
    ...

def print_exception(exc: Exception) -> None:
    """Imprimeix una excepció amb un rastreig.

Example: ``sys.print_exception(e)``

:param exc: L'excepció a imprimir

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""Una llista mutable d'arguments amb què s'ha iniciat el programa actual."""
byteorder: str
"""L'ordre dels bytes del sistema (``"little"`` o ``"big"``)."""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""Objecte amb informació sobre la implementació actual de Python. (implementació)

For MicroPython, it has following attributes:

- ``name`` - string "micropython"
- ``version`` - tuple (major, minor, micro), e.g. (1, 7, 0)

This object is the recommended way to distinguish MicroPython from other
Python implementations (note that it still may not exist in the very
minimal ports).

CPython mandates more attributes for this object, but the actual useful
bare minimum is implemented in MicroPython.
"""
maxsize: int
"""
Valor màxim que pot tenir un tipus d'enter natiu a la plataforma actual,
o valor màxim representable pel tipus d'enter MicroPython, si és més petit
que el valor màxim de la plataforma (és el cas dels ports MicroPython sense
suport d'enter llarg - long int support).

This attribute is useful for detecting "bitness" of a platform (32-bit vs
64-bit, etc.). It's recommended to not compare this attribute to some
value directly, but instead count number of bits in it::

    bits = 0
    v = sys.maxsize
    while v:
        bits += 1
        v >>= 1
    if bits > 32:
        # 64-bit (or more) platform
        ...
    else:
        # 32-bit (or less) platform
        # Note that on 32-bit platform, value of bits may be less than 32
        # (e.g. 31) due to peculiarities described above, so use "> 16",
        # "> 32", "> 64" style of comparisons.
"""
modules: Dict[str, Any]
"""Diccionari de mòduls carregats. (mòduls) 

On some ports, it may not include builtin modules."""
path: List[str]
"""Una llista mutable de directoris per cercar mòduls importats."""
platform: str
"""La plataforma en què s'executa MicroPython. (plataforma) 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""Versió del llenguatge Python a la qual s'ajusta aquesta implementació, com a cadena. (versió)"""
version_info: Tuple[int, int, int]
"""Versió del llenguatge Python a la qual s'ajusta aquesta implementació, com una tupla d'enters. (informació de la versió)

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""