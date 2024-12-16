"""Toegang tot het bestandssysteem."""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Bestanden weergeven.

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Verwijder (verwijder) een bestand. (verwijder)

Example: ``os.remove('data.txt')``

:param filename: (bestands naam) Het bestand is verwijderd

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Geeft de grootte van een bestand weer. (grootte)

Example: ``os.size('data.txt')``

:param filename: (bestands naam) Het bestand
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Resultaat van ``os.uname()`` (uname resultaat)"""
    sysname: str
    """Besturingssysteem naam"""
    nodename: str
    """Naam van machine op het netwerk (implementation-defined)."""
    release: str
    """Besturingssysteem release. (vrijgeven)"""
    version: str
    """Besturingssysteem versie. (versie)"""
    machine: str
    """Identificatie hardware"""

def uname() -> uname_result:
    """Geeft informatie terug die het huidige besturingssysteem identificeert.

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