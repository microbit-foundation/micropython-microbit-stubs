"""Fonctions spécifiques au système"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """Terminer le programme en cours avec un code de sortie donné.

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: Le code de sortie ou le message."""
    ...

def print_exception(exc: Exception) -> None:
    """Imprime une exception avec une pile d'appels.

Example: ``sys.print_exception(e)``

:param exc: L'exception à imprimer

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""Une liste mutable d'arguments avec lesquels le programme courant a été démarré."""
byteorder: str
"""L'ordre des octets du système (``"little"`` ou ``"big"``)."""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""Objet avec des informations sur l'implémentation actuelle de Python.

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
Valeur maximale qu'un entier natif peut stocker sur la plate-forme courante,
ou valeur maximale représentable par le type entier de MicroPython, si elle est plus petite
que la valeur maximale de la plate-forme (c'est le cas pour les portages MicroPython sans support
des entiers long).

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
"""Dictionnaire des modules chargés. 

On some ports, it may not include builtin modules."""
path: List[str]
"""Une liste mutable de répertoires dans lesquels rechercher des modules importés."""
platform: str
"""La plate-forme sur laquelle MicroPython s'exécute. 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""Version du langage Python à laquelle cette implémentation correspond, sous la forme d'une chaîne de caractères ."""
version_info: Tuple[int, int, int]
"""Version du langage Python à laquelle cette implémentation correspond, sous forme d'un tuple d'entiers.

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""