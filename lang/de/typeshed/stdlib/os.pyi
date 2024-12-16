"""Auf das Dateisystem zugreifen."""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Dateien auflisten.

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Entfernt\xa0/ Löscht eine Datei. (Entfernen)

Example: ``os.remove('data.txt')``

:param filename: (Dateiname) Die zu löschende Datei.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Gibt die Größe einer Datei zurück

Example: ``os.size('data.txt')``

:param filename: (Dateiname) Die Datei
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Ergebnis von  ``os.uname()``"""
    sysname: str
    """Name des Betriebssystems."""
    nodename: str
    """Name des Rechners im Netz (durch die Implementierung definiert). (Knotenname)"""
    release: str
    """Betriebssystemveröffentlichung. (Veröffentlichung)"""
    version: str
    """Betriebssystemversion. (Version)"""
    machine: str
    """Hardware-Kennung. (maschine)"""

def uname() -> uname_result:
    """Gibt Informationen zum aktuellen Betriebssystem zurück.

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