"""系統特定函式"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """使用指定的退出代碼來終止當前程式。

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: 退出代碼或訊息。"""
    ...

def print_exception(exc: Exception) -> None:
    """輸出帶有回溯的例外狀況。

Example: ``sys.print_exception(e)``

:param exc: 輸出例外狀況

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""目前程式啟動時，所使用的可變引數列表。"""
byteorder: str
"""系統的位元組順序 (``"little"`` 或 ``"big"``)。"""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""包含關於目前 Python 執行資訊的物件。

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
本機整數類型在當前平台上可以保存的最大值，或 MicroPython 整數類型可表示的最大值，如果它小於平台最大值 (對於沒有 long int 支援的 MicroPython 連接埠，就是這種情況)。

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
"""已載入模組的字典。 

On some ports, it may not include builtin modules."""
path: List[str]
"""用於搜尋匯入模組的可變字典列表。"""
platform: str
"""正在執行 MicroPython 的平台。 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""此執行符合的 Python 語言版本，做為字串。"""
version_info: Tuple[int, int, int]
"""此執行符合的 Python 語言版本，做為整數元組。

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""