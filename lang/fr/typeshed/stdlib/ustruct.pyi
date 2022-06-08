"""Pack and unpack primitive data types. (ustruct)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Get the number of bytes needed to store the given ``fmt``. (calcsize)

Example: ``ustruct.calcsize('hf')``

:param fmt: (fmt) A format string.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Pack values according to a format string. (pack)

Example: ``ustruct.pack('hf', 1, 3.1415)``

:param fmt: (fmt) The format string.
:param v1: (v1) The first value.
:param *vn: (*vn) The remaining values.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Pack values according to a format string. (pack into)

Example: ``ustruct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: (fmt) The format string.
:param buffer: (buffer) The target buffer to write into.
:param offset: (offset) The offset into the buffer. May be negative to count from the end of the buffer.
:param v1: (v1) The first value.
:param *vn: (*vn) The remaining values."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Unpack data according to a format string. (unpack)

Example: ``v1, v2 = ustruct.unpack('hf', buffer)``

:param fmt: (fmt) The format string.
:param data: (data) The data.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Unpack data from a buffer according to a format string. (unpack from)

Example: ``v1, v2 = ustruct.unpack_from('hf', buffer)``

:param fmt: (fmt) The format string.
:param buffer: (buffer) The source buffer to read from.
:param offset: (offset) The offset into the buffer. May be negative to count from the end of the buffer.
:return: A tuple of the unpacked values."""
    ...