from typing import Tuple
"""Access the file system.
"""
from typing import List

def listdir() -> List[str]:
    """List files. (listdir)

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Remove (delete) a file. (remove)

Example: ``os.remove('data.txt')``

:param filename: (filename) The file to delete.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Returns the size of a file. (size)

Example: ``os.size('data.txt')``

:param filename: (filename) The file
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Result of ``os.uname()`` (uname result)"""
    sysname: str
    """Operating system name. (sysname)"""
    nodename: str
    """Name of machine on network (implementation-defined). (nodename)"""
    release: str
    """Operating system release. (release)"""
    version: str
    """Operating system version. (version)"""
    machine: str
    """Hardware identifier. (machine)"""

def uname() -> uname_result:
    """Returns information identifying the current operating system. (uname)

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