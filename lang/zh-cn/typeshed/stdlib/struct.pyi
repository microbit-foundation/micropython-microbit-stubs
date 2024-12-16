"""打包和解包原始数据类型。 (结构)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """获取存储给定 ``fmt`` 所需的字节数。 (计算大小)

Example: ``struct.calcsize('hf')``

:param fmt: (格式字符串) 格式字符串。
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """根据格式字符串打包值。 (打包)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: (格式字符串) 格式字符串。
:param v1: 第一个值。
:param *vn: 剩余值。
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """根据格式字符串打包值。

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: (格式字符串) 格式字符串。
:param buffer: (缓冲区) 待写入的目标缓冲区。
:param offset: (偏移量) 缓冲区内的偏移量。如果从缓冲区末端开始算起，该偏移量可能是负数。
:param v1: 第一个值。
:param *vn: 剩余值。"""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """根据格式字符串解压数据。 (解包)

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: (格式字符串) 格式字符串。
:param data: (数据) 数据。
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """根据格式字符串从缓冲区解压数据。

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: (格式字符串) 格式字符串。
:param buffer: 待读取的源缓冲区。
:param offset: (偏移量) 缓冲区内的偏移量。如果从缓冲区末端开始算起，该偏移量可能是负数。
:return: A tuple of the unpacked values."""
    ...