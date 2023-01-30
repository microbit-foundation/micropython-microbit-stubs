"""Accedeix al sistema de fitxers."""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Llista dels fitxers.

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Eliminar (suprimir) un fitxer. (eliminar)

Example: ``os.remove('data.txt')``

:param filename: (nom del fitxer) El fitxer a suprimir.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Retorna la mida d'un fitxer (mida)

Example: ``os.size('data.txt')``

:param filename: (nom del fitxer) El fitxer
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Resultat de ``os.uname()``"""
    sysname: str
    """Nom del sistema operatiu."""
    nodename: str
    """Nom de la màquina a la xarxa (definida per la implementació)."""
    release: str
    """Versió del sistema operatiu. (versió)"""
    version: str
    """Versió del sistema operatiu. (versió)"""
    machine: str
    """Identificador del maquinari. (màquina)"""

def uname() -> uname_result:
    """Retorna informació que identifica el sistema operatiu actual.

Example: ``os.uname()``

The return value is an object with five attributes:

- ``sysname`` - operating system name
- ``nodename`` - name of machine on network (implementation-defined)
- ``release`` - operating system release
- ``version`` - operating system version
- ``machine`` - hardware identifier

There is no underlying operating system in MicroPython. As a result the
information returned by the ``uname`` function is mostly useful for
versioning details."""
    ...