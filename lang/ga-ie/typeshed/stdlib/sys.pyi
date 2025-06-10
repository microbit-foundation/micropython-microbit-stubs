"""Feidhmeanna a bhaineann go sonrach leis an gcóras"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """Cuir deireadh leis an ríomhchlár reatha le cód scoir ar leith. (scoir)

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: An cód scoir nó an teachtaireacht."""
    ...

def print_exception(exc: Exception) -> None:
    """Priontáil eisceacht le rianú siar. (eisceacht priontála)

Example: ``sys.print_exception(e)``

:param exc: An eisceacht maidir le priontáil

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""Liosta inathraithe d'argóintí a cuireadh tús leis an gclár reatha leo."""
byteorder: str
"""Ord beart an chórais (``"little"`` nó ``"big"``)."""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""Cuspóir le faisnéis faoi chur i bhfeidhm reatha Python. (cur i bhfeidhm)

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
Uasluach is féidir le cineál slánuimhir dhúchasach a shealbhú ar an ardán reatha,
nó an luach uasta is féidir a léiriú le cineál slánuimhir MicroPython, má tá sé níos lú
ná uasluach ardáin (is é sin an cás i gcás calafoirt MicroPython gan
tacaíocht int fada). (uasmhéid)

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
"""Foclóir modúil luchtaithe. (modúil) 

On some ports, it may not include builtin modules."""
path: List[str]
"""Liosta inathraithe d’eolairí le cuardach a dhéanamh ar mhodúil allmhairithe. (cosán)"""
platform: str
"""An t-ardán a bhfuil MicroPython ag rith air. (ardán) 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""Leagan teanga Python a chloíonn leis an gcur i bhfeidhm seo, mar theaghrán. (leagan)"""
version_info: Tuple[int, int, int]
"""Leagan teanga Python a gcomhlíonann an cur i bhfeidhm seo, mar thupla de shláintiúirí. (eolas faoin leagan)

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""