"""Uzyskaj dostęp do systemu plików."""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Lista plików.

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Usuń (usuń) plik.

Example: ``os.remove('data.txt')``

:param filename: Plik do usunięcia.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Zwraca rozmiar pliku.

Example: ``os.size('data.txt')``

:param filename: Plik
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Wynik ``os.uname()``"""
    sysname: str
    """Nazwa systemu operacyjnego."""
    nodename: str
    """Nazwa maszyny w sieci (zdefiniowana w implementacji)."""
    release: str
    """Wydanie systemu operacyjnego."""
    version: str
    """Wersja systemu operacyjnego"""
    machine: str
    """Identyfikator sprzętu."""

def uname() -> uname_result:
    """Zwraca informacje identyfikujące bieżący system operacyjny.

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