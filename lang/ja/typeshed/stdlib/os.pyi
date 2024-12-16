"""ファイルシステムにアクセスします。"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """ファイルすべての名前のリストを取得します。

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """ファイルを削除します。

Example: ``os.remove('data.txt')``

:param filename: 削除するファイルの名前。

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """ファイルのサイズを返します。

Example: ``os.size('data.txt')``

:param filename: ファイル
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """``os.uname()`` の結果"""
    sysname: str
    """オペレーティングシステム名。"""
    nodename: str
    """ネットワーク上のマシンの名前（実装定義）。"""
    release: str
    """オペレーティングシステムのリリース。"""
    version: str
    """オペレーティングシステムのバージョン。"""
    machine: str
    """ハードウェア識別子。"""

def uname() -> uname_result:
    """現在のオペレーティングシステムを識別する情報を返します。

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