"""Funkcje specyficzne dla systemu"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """Zakończ bieżący program z podanym kodem wyjścia.

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: Kod lub wiadomość wyjściowa."""
    ...

def print_exception(exc: Exception) -> None:
    """Wydrukuj wyjątek ze śledzeniem.

Example: ``sys.print_exception(e)``

:param exc: Wyjątek do wydrukowania

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""Zmienna lista argumentów, od których uruchomiono bieżący program."""
byteorder: str
"""Kolejność bajtów systemu (``"little"`` lub ``"big"``)."""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""Obiekt z informacjami o bieżącej implementacji Pythona.

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
Maksymalna wartość, jaką może przechowywać natywny typ całkowity na bieżącej platformie,
lub maksymalna wartość reprezentowana przez typ całkowity MicroPythona, jeśli jest mniejsza
niż maksymalna wartość platformy (tak jest w przypadku portów MicroPython bez
wsparcia long int).

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
"""Słownik załadowanych modułów. 

On some ports, it may not include builtin modules."""
path: List[str]
"""Zmienna lista katalogów do wyszukiwania importowanych modułów."""
platform: str
"""Platforma na której działa MicroPython. 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""Wersja Pythona, z którą ta implementacja jest zgodna, jako łańcuch."""
version_info: Tuple[int, int, int]
"""Wersja Pythona, z którą ta implementacja jest zgodna, jako krotka typu int.

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""