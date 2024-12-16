"""システム固有関数。"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """与えた終了コードで現在のプログラムを終了します。

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: 終了コードまたはメッセージ。"""
    ...

def print_exception(exc: Exception) -> None:
    """例外をトレースバック付きで出力します。

Example: ``sys.print_exception(e)``

:param exc: 表示する例外

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""現在のプログラム開始時の引数の変更可能なリスト。"""
byteorder: str
"""システムのバイト順（``"little"`` または ``"big"``）。"""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""現在の Python 処理系に関する情報を持つオブジェクト。

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
現在のプラットフォームでネイティブ整数型が保持できる最大値、またはプラットフォームの最大値より小さい場合は MicroPython 整数型で表現可能な最大値（MicroPython ポートで 長整数をサポートしないとした場合）。

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
"""読み込まれたモジュールの辞書。 

On some ports, it may not include builtin modules."""
path: List[str]
"""インポートするモジュールを検索するディレクトリの変更可能なリスト。"""
platform: str
"""MicroPython が実行されているプラ\u200b\u200bットフォーム。 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""この処理系が準拠するPython言語バージョンを表す文字列。"""
version_info: Tuple[int, int, int]
"""この実装が準拠しているPython言語バージョンを表すintのタプル。

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""