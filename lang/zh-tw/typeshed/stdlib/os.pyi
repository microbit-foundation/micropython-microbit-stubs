"""存取檔案系統。 (os)"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """列出檔案。 (listdir)

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """移除（刪除）一個檔案。 (remove)

Example: ``os.remove('data.txt')``

:param filename: (filename) 要刪除的文件。

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """傳回檔案的大小。 (size)

Example: ``os.size('data.txt')``

:param filename: (filename) 檔案
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """``os.uname()`` 的結果 (未命名結果)"""
    sysname: str
    """作業系統名稱。 (sysname)"""
    nodename: str
    """網路上的機器名稱（實現定義）。 (nodename)"""
    release: str
    """作業系統發佈。 (release)"""
    version: str
    """作業系統版本。 (version)"""
    machine: str
    """硬體標識碼。 (機器)"""

def uname() -> uname_result:
    """傳回標識目前作業系統的資訊。 (uname)

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