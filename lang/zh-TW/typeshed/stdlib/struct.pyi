"""壓縮和解壓縮原始資料類型。"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """取得存儲特定 ``fmt`` 所需的位元組數。

Example: ``struct.calcsize('hf')``

:param fmt: 格式字串。
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """根據格式字串，壓縮數值。

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: 格式字串。
:param v1: 首位數值。
:param *vn: 剩餘數值。
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """根據格式字串，壓縮數值。

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: 格式字串。
:param buffer: 要寫入的緩衝區。
:param offset: 緩衝區內的位移。從緩衝區結尾開始計數，該位移可能為負數。
:param v1: 首位數值。
:param *vn: 剩餘數值。"""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """根據格式字串，解壓縮數值。

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: 格式字串。
:param data: 資料。
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """根據格式字串，從緩衝區解壓縮資料。

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: 格式字串。
:param buffer: 要讀取的來源緩衝區。
:param offset: 緩衝區內的位移。從緩衝區結尾開始計數，該位移可能為負數。
:return: A tuple of the unpacked values."""
    ...