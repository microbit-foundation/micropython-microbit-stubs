"""crwdns330668:0crwdne330668:0 (crwdns330666:0crwdne330666:0)"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """crwdns330672:0crwdne330672:0 (crwdns330670:0crwdne330670:0)

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """crwdns330676:0crwdne330676:0 (crwdns330674:0crwdne330674:0)

Example: ``os.remove('data.txt')``

:param filename: (crwdns330678:0crwdne330678:0) crwdns330680:0crwdne330680:0

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """crwdns330684:0crwdne330684:0 (crwdns330682:0crwdne330682:0)

Example: ``os.size('data.txt')``

:param filename: (crwdns330686:0crwdne330686:0) crwdns330688:0crwdne330688:0
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """crwdns330692:0``os.uname()``crwdne330692:0 (crwdns330690:0crwdne330690:0)"""
    sysname: str
    """crwdns330696:0crwdne330696:0 (crwdns330694:0crwdne330694:0)"""
    nodename: str
    """crwdns330700:0crwdne330700:0 (crwdns330698:0crwdne330698:0)"""
    release: str
    """crwdns330704:0crwdne330704:0 (crwdns330702:0crwdne330702:0)"""
    version: str
    """crwdns330708:0crwdne330708:0 (crwdns330706:0crwdne330706:0)"""
    machine: str
    """crwdns330712:0crwdne330712:0 (crwdns330710:0crwdne330710:0)"""

def uname() -> uname_result:
    """crwdns330716:0crwdne330716:0 (crwdns330714:0crwdne330714:0)

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