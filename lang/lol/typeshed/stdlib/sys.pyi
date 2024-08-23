"""crwdns331068:0crwdne331068:0 (crwdns331066:0crwdne331066:0)"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """crwdns331072:0crwdne331072:0 (crwdns331070:0crwdne331070:0)

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: (crwdns331074:0crwdne331074:0) crwdns331076:0crwdne331076:0"""
    ...

def print_exception(exc: Exception) -> None:
    """crwdns331080:0crwdne331080:0 (crwdns331078:0crwdne331078:0)

Example: ``sys.print_exception(e)``

:param exc: (crwdns331082:0crwdne331082:0) crwdns331084:0crwdne331084:0

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""crwdns331088:0crwdne331088:0 (crwdns331086:0crwdne331086:0)"""
byteorder: str
"""crwdns331092:0``"little"``crwdnd331092:0``"big"``crwdne331092:0 (crwdns331090:0crwdne331090:0)"""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""crwdns331096:0crwdne331096:0 (crwdns331094:0crwdne331094:0)

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
crwdns331100:0crwdne331100:0 (crwdns331098:0crwdne331098:0)

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
"""crwdns331104:0crwdne331104:0 (crwdns331102:0crwdne331102:0) 

On some ports, it may not include builtin modules."""
path: List[str]
"""crwdns331108:0crwdne331108:0 (crwdns331106:0crwdne331106:0)"""
platform: str
"""crwdns331112:0crwdne331112:0 (crwdns331110:0crwdne331110:0) 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""crwdns331116:0crwdne331116:0 (crwdns331114:0crwdne331114:0)"""
version_info: Tuple[int, int, int]
"""crwdns331120:0crwdne331120:0 (crwdns331118:0crwdne331118:0)

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""