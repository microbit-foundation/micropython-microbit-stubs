"""Access the file system.
"""

from typing import List

def listdir() -> List[str]:
    """List files.

    :return: A list of the names of all the files contained within the local
    persistent on-device file system.
    """
    ...

def remove(filename: str) -> None:
    """Remove (delete) a file.

    :param filename: The file to delete.

    If the file does not exist an ``OSError`` exception will occur.
    """
    ...

def size(filename: str) -> int:
    """Returns the size of a file.

    :param filename: The file
    :return: The size in bytes.

    If the file does not exist an ``OSError`` exception will occur.
    """

def uname() -> str:
    """Returns information identifying the current operating system. 
    
    The return value is an object with five attributes:

    - ``sysname`` - operating system name
    - ``nodename`` - name of machine on network (implementation-defined)
    - ``release`` - operating system release
    - ``version`` - operating system version
    - ``machine`` - hardware identifier

    There is no underlying operating system in MicroPython. As a result the
    information returned by the ``uname`` function is mostly useful for
    versioning details.
    """
    ...
