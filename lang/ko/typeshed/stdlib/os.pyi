"""파일 시스템에 액세스합니다. (os)"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """파일을 나열합니다. (listdir)

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """파일을 제거(삭제)합니다. (remove)

Example: ``os.remove('data.txt')``

:param filename: (filename) 삭제할 파일입니다.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """파일의 크기를 반환합니다. (size)

Example: ``os.size('data.txt')``

:param filename: (filename) 파일
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """``os.uname()``의 결과 (uname result)"""
    sysname: str
    """운영 체제 이름입니다. (sysname)"""
    nodename: str
    """네트워크상의 머신 이름입니다(구현 방법에 따라 정의됨). (nodename)"""
    release: str
    """운영 체제 릴리스입니다. (release)"""
    version: str
    """운영 체제 버전입니다. (version)"""
    machine: str
    """하드웨어 식별자입니다. (machine)"""

def uname() -> uname_result:
    """현재 운영 시스템을 식별하는 정보를 반환합니다. (uname)

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