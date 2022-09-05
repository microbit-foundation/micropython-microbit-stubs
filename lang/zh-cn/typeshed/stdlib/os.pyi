"""访问文件系统。 (os)"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """列出文件。 (listdir)

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """移除（删除）一份文件。 (remove)

Example: ``os.remove('data.txt')``

:param filename: (filename) 要删除的文件。

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """返回文件的大小。 (size)

Example: ``os.size('data.txt')``

:param filename: (filename) 此文件
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """``os.uname()`` 的结果 (uname result)"""
    sysname: str
    """操作系统名称。 (sysname)"""
    nodename: str
    """网络上机器的名称（实现-定义）。 (nodename)"""
    release: str
    """操作系统发布版本。 (release)"""
    version: str
    """操作系统版本。 (version)"""
    machine: str
    """硬件标识符。 (machine)"""

def uname() -> uname_result:
    """返回标识当前操作系统的信息。 (uname)

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