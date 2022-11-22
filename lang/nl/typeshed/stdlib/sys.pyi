"""Systeem specifieke functies"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """Beëindig het huidige programma met een bepaalde exit code. (afsluiten)

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: De exit code of bericht."""
    ...

def print_exception(exc: Exception) -> None:
    """Print een exception met traceback. (exceptie afdrukken)

Example: ``sys.print_exception(e)``

:param exc: De af te drukken uitzondering

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""Een veranderlijke lijst met argumenten waarmee het huidige programma is gestart."""
byteorder: str
"""De byte volgorde van het systeem (``"little"`` of ``"big"``). (byte volgorde)"""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""Object met informatie over de huidige Python implementatie. (implementatie)

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
Maximale waarde die een native integer type kan aanhouden op het huidige platform, of de maximale waarde die kan worden vertegenwoordigd door MicroPython integer type, als het kleiner is dan platform max waarde (dat is het geval voor MicroPython poorten zonder
lange int ondersteuning).

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
"""Woordenboek van geladen modules. 

On some ports, it may not include builtin modules."""
path: List[str]
"""Een aanpasbare lijst van mappen om te zoeken naar geïmporteerde modules. (pad)"""
platform: str
"""Het platform waarop MicroPython actief is. 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""Python taalversie waar deze implementatie mee overeenstemt als tekenreeks. (versie)"""
version_info: Tuple[int, int, int]
"""Python taalversie waaraan deze implementatie voldoet, als een tupel van ints. (versie informatie)

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""