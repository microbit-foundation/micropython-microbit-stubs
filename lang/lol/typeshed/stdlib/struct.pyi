"""crwdns330988:0crwdne330988:0 (crwdns330986:0crwdne330986:0)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """crwdns330992:0``fmt``crwdne330992:0 (crwdns330990:0crwdne330990:0)

Example: ``struct.calcsize('hf')``

:param fmt: (crwdns330994:0crwdne330994:0) crwdns330996:0crwdne330996:0
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """crwdns331000:0crwdne331000:0 (crwdns330998:0crwdne330998:0)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: (crwdns331006:0crwdne331006:0) crwdns331008:0crwdne331008:0
:param v1: (crwdns331010:0crwdne331010:0) crwdns331012:0crwdne331012:0
:param *vn: (crwdns331002:0crwdne331002:0) crwdns331004:0crwdne331004:0
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """crwdns331016:0crwdne331016:0 (crwdns331014:0crwdne331014:0)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: (crwdns331026:0crwdne331026:0) crwdns331028:0crwdne331028:0
:param buffer: (crwdns331022:0crwdne331022:0) crwdns331024:0crwdne331024:0
:param offset: (crwdns331030:0crwdne331030:0) crwdns331032:0crwdne331032:0
:param v1: (crwdns331034:0crwdne331034:0) crwdns331036:0crwdne331036:0
:param *vn: (crwdns331018:0crwdne331018:0) crwdns331020:0crwdne331020:0"""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """crwdns331040:0crwdne331040:0 (crwdns331038:0crwdne331038:0)

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: (crwdns331046:0crwdne331046:0) crwdns331048:0crwdne331048:0
:param data: (crwdns331042:0crwdne331042:0) crwdns331044:0crwdne331044:0
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """crwdns331052:0crwdne331052:0 (crwdns331050:0crwdne331050:0)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: (crwdns331058:0crwdne331058:0) crwdns331060:0crwdne331060:0
:param buffer: (crwdns331054:0crwdne331054:0) crwdns331056:0crwdne331056:0
:param offset: (crwdns331062:0crwdne331062:0) crwdns331064:0crwdne331064:0
:return: A tuple of the unpacked values."""
    ...