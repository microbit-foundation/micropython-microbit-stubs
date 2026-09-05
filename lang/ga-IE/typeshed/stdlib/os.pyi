"""Rochtain a fháil ar an gcóras comhad."""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Liostaigh comhaid.

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Bain (scrios) comhad. (bain)

Example: ``os.remove('data.txt')``

:param filename: (ainm comhaid) An comhad le scriosadh.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Tuairisceáin méid comhaid. (méid)

Example: ``os.size('data.txt')``

:param filename: (ainm comhaid) An comhad
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Toradh de ``os.uname()`` (toradh uname)"""
    sysname: str
    """Ainm an chórais oibriúcháin. (ainm an chórais)"""
    nodename: str
    """Ainm an mheaisín ar an líonra (cur i bhfeidhm sainithe). (ainm nóid)"""
    release: str
    """Scaoileadh an chórais oibriúcháin. (scaoileadh)"""
    version: str
    """Leagan an chórais oibriúcháin. (leagan)"""
    machine: str
    """Aitheantóir crua-earraí. (meaisín)"""

def uname() -> uname_result:
    """Tuairisceáin faisnéis a aithníonn an córas oibriúcháin reatha.

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