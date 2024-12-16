"""Systemspezifische Funktionen"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """Beendet ein Programm mit dem gegeneben Exit-Code.

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: Der Exit-Code oder die Nachricht."""
    ...

def print_exception(exc: Exception) -> None:
    """Eine Ausnahme mit einem Traceback ausgeben. (Ausnahme ausgeben)

Example: ``sys.print_exception(e)``

:param exc: Die auszugebende Ausnahme

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""Eine veränderbare Liste von Argumenten, mit denen das aktuelle Programm gestartet wurde."""
byteorder: str
"""Die Byte-Reihenfolge des Systems (``"little"`` oder ``"big"``)."""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""Objekt mit Informationen über die aktuelle Python-Implementierung. (Implementierung)

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
Maximaler Wert, den ein nativer Integer-Typ auf der aktuellen Plattform halten kann, oder maximaler Wert, der durch den MicroPython-Integer-Typ darstellbar ist, wenn er kleiner ist als der maximale Plattformwert (das ist der Fall bei MicroPython-Ports ohne "long int"-Unterstützung).

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
"""Wörterbuch der geladenen Module. (module) 

On some ports, it may not include builtin modules."""
path: List[str]
"""Eine veränderbare Liste von Verzeichnissen zum Suchen nach importierten Modulen."""
platform: str
"""Die Plattform, auf der MicroPython läuft. (plattform) 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""Python-Sprachversion, der diese Implementierung als String entspricht. (Version)"""
version_info: Tuple[int, int, int]
"""Python-Sprachversion, der diese Implementierung als Tuple mit Ints entspricht. (Versionsinformationen)

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""