"""系统特定功能 (sys)"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """根据给定退出代码终止当前程序。 (exit)

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: (retval) 退出代码或者消息。"""
    ...

def print_exception(exc: Exception) -> None:
    """
打印带有回溯的异常。 (print exception)

Example: ``sys.print_exception(e)``

:param exc: (exc) 需打印的异常

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""当前程序启动时使用的参数的可变列表。 (argv)"""
byteorder: str
"""系统的字节顺序 (``"little"`` 或 ``"big"``)。 (byteorder)"""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""包含有关当前 Python 实现的信息的对象。 (implementation)

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
"""在当前平台上可以容纳的整数类型的最大值，
或 MicroPython 整数类型可表示的最大值，如果它小于
平台的最大值（这见于 MicroPython 端口不支持长整数的情况）。 (maxsize)

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
"""已加载模块的字典。  (modules)

On some ports, it may not include builtin modules."""
path: List[str]
"""用于搜索导入模块的目录的可变列表。 (path)"""
platform: str
"""正在运行 MicroPython 的平台。 (platform)

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""此实现符合的 Python 语言版本，为字符串。 (version)"""
version_info: Tuple[int, int, int]
"""此实现符合的 Python 语言版本，为整数元组。 (version info)

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""