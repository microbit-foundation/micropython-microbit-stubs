"""시스템 특정 함수"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """주어진 종료 코드로 현재 프로그램을 종료합니다.

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: 종료 코드 또는 메시지입니다."""
    ...

def print_exception(exc: Exception) -> None:
    """트레이스백으로 예외를 프린트합니다.

Example: ``sys.print_exception(e)``

:param exc: 프린트할 예외

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""현재 프로그램과 같이 시작된 인자의 가변 리스트입니다."""
byteorder: str
"""시스템의 바이트 순서를 (``"little"`` 또는 ``"big"``)으로 정렬합니다."""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""현재 Python 구현에 관한 정보가 담긴 개체

For MicroPython, it has following attributes:

- ``name`` - string "micropython"
- ``version`` - tuple (major, minor, micro), e.g. (1, 7, 0)

This object is the recommended way to distinguish MicroPython from other
Python implementations (note that it still may not exist in the very
minimal ports).

CPython mandates more attributes for this object, but the actual useful
bare minimum is implemented in MicroPython.
"""
maxsize: int
"""
현재 플랫폼에서 자연 정수 유형이 지원할 수 있는 최대 값, 또는 값이 플랫폼의 최대 값보다 작다면 MicroPython 정수 유형으로 표현할 수 있는 최대 값입니다(long int를 지원하지 않는 MicroPython 포트의 경우).

This attribute is useful for detecting "bitness" of a platform (32-bit vs
64-bit, etc.). It's recommended to not compare this attribute to some
value directly, but instead count number of bits in it::

    bits = 0
    v = sys.maxsize
    while v:
        bits += 1
        v >>= 1
    if bits > 32:
        # 64-bit (or more) platform
        ...
    else:
        # 32-bit (or less) platform
        # Note that on 32-bit platform, value of bits may be less than 32
        # (e.g. 31) due to peculiarities described above, so use "> 16",
        # "> 32", "> 64" style of comparisons.
"""
modules: Dict[str, Any]
"""로드된 모듈의 딕셔너리입니다. 

On some ports, it may not include builtin modules."""
path: List[str]
"""불러온 모듈을 검색하기 위한 딕셔너리 가변 리스트입니다."""
platform: str
"""MicroPython이 실행되고 있는 플랫폼입니다. 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""이 구현이 준수하는 Python 언어 버전을 문자열로 제공합니다."""
version_info: Tuple[int, int, int]
"""이 구현이 준수하는 Python 언어 버전을 정수 튜플로 제공합니다.

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""