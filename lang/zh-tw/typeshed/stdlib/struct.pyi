"""拆包和解包原始資料類型。 (struct)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """取得儲存特定 ``fmt`` 所需的位元組數。 (calcsize)

Example: ``struct.calcsize('hf')``

:param fmt: (fmt) 格式字串
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """根據格式字串打包數值。 (pack)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: (fmt) 格式字串
:param v1: (v1) 首位數值
:param *vn: (*vn) 剩餘數值。
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """根據格式字串打包數值。 (pack into)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: (fmt) 格式字串
:param buffer: (buffer) 要寫入的緩衝區。
:param offset: (offset) 緩衝區的偏移量。 從緩衝區末尾開始計數可能為負數。
:param v1: (v1) 首位數值
:param *vn: (*vn) 剩餘數值"""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """根據格式字串解包數值。 (unpack)

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: (fmt) 格式字串
:param data: (data) 資料。
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """根據格式字串解包數值。 (unpack from)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: (fmt) 格式字串
:param buffer: (buffer) 要讀取的來源緩衝區。
:param offset: (offset) 緩衝區的偏移量。 從緩衝區末尾開始計數可能為負數。
:return: A tuple of the unpacked values."""
    ...