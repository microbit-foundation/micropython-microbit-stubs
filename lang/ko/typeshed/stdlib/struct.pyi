"""원시 데이터 유형을 패킹하고 언패킹합니다."""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """주어진 ``fmt``를 저장하는 데 필요한 바이트의 수를 불러옵니다.

Example: ``struct.calcsize('hf')``

:param fmt: 형식 문자열입니다.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """형식 문자열에 따라 값을 패킹합니다.

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: 형식 문자열입니다.
:param v1: 첫 값입니다.
:param *vn: 남은 값입니다.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """형식 문자열에 따라 값을 패킹합니다.

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: 형식 문자열입니다.
:param buffer: 작성할 목표 버퍼입니다.
:param offset: 버퍼에 적용할 오프셋입니다. 음수를 입력하면 버퍼 끝부터 셀 수 있습니다.
:param v1: 첫 값입니다.
:param *vn: 남은 값입니다."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """형식 문자열에 따라 데이터를 언패킹합니다.

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: 형식 문자열입니다.
:param data: 데이터입니다.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """형식 문자열에 따라 버퍼로부터 데이터를 언패킹합니다.

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: 형식 문자열입니다.
:param buffer: 읽을 소스 버퍼입니다.
:param offset: (오프셋) 버퍼에 적용할 오프셋입니다. 음수를 입력하면 버퍼 끝부터 셀 수 있습니다.
:return: A tuple of the unpacked values."""
    ...