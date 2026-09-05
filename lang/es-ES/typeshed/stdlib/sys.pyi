"""Funciones específicas del sistema"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """Termina el programa actual con un código de salida determinado. (salir)

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: El mensaje o código de salida."""
    ...

def print_exception(exc: Exception) -> None:
    """Imprime una excepción con un seguimiento. (imprimir excepción)

Example: ``sys.print_exception(e)``

:param exc: La excepción a imprimir

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""Una lista mutable de argumentos con los que se inició el programa actual."""
byteorder: str
"""El orden de bytes del sistema (``"little"`` o ``"big"``). (ordenbytes)"""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""Objeto con información sobre la implementación actual de Python. (implementación)

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
Valor máximo que un tipo entero nativo puede contener en la plataforma actual
o valor máximo representable por el tipo entero de MicroPython, en el caso de que sea más pequeño
que el valor máximo de la plataforma (que es el caso de los puertos de MicroPython incompatibles con el
tipo entero largo). (tamañomáx)

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
"""Diccionario de módulos cargados. (módulos) 

On some ports, it may not include builtin modules."""
path: List[str]
"""Una lista mutable de directorios para buscar módulos importados. (ruta)"""
platform: str
"""La plataforma en la que se está ejecutando MicroPython. (plataforma) 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""Versión del lenguaje Python a la que se ajusta esta implementación, en forma de cadena. (versión)"""
version_info: Tuple[int, int, int]
"""Versión del lenguaje Python a la que se ajusta esta implementación, en forma de tupla de enteros. (info de versión)

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""