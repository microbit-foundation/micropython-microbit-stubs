"""存取檔案系統。"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """列出檔案。

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """移除 (刪除) 一個檔案。

Example: ``os.remove('data.txt')``

:param filename: 要刪除的檔案。

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """傳回檔案的大小。

Example: ``os.size('data.txt')``

:param filename: 檔案
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """``os.uname()`` 的結果"""
    sysname: str
    """作業系統名稱。"""
    nodename: str
    """網路上的機器名稱 (執行定義)。"""
    release: str
    """作業系統發佈。"""
    version: str
    """作業系統版本。"""
    machine: str
    """硬體識別碼。"""

def uname() -> uname_result:
    """傳回識別目前作業系統的資訊。

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