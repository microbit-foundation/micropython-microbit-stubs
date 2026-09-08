"""Pacáistiú agus díphacáil cineálacha sonraí bunúsach."""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Faigh líon na mbeart a theastaíonn chun an ``fmt`` tugtha a stóráil.

Example: ``struct.calcsize('hf')``

:param fmt: Teaghrán formáide.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Pacáil luachanna de réir teaghrán formáide. (pacáiste)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: An teaghrán formáide.
:param v1: An chéad luach.
:param *vn: Na luachanna atá fágtha.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Pacáil luachanna de réir teaghrán formáide. (pacáil isteach i)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: An teaghrán formáide.
:param buffer: (maolán) An maolán sprice le scríobh isteach.
:param offset: (fritháireamh) An fritháireamh isteach sa mhaolán. D'fhéadfadh sé a bheith diúltach le comhaireamh ó dheireadh an mhaoláin.
:param v1: An chéad luach.
:param *vn: Na luachanna atá fágtha."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Díphacáil sonraí de réir teaghrán formáide. (díphacáil)

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: An teaghrán formáide.
:param data: (sonraí) Na sonraí.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Díphacáil sonraí ó mhaolán de réir teaghrán formáide. (díphacáil ó)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: An teaghrán formáide.
:param buffer: (maolán) An maolán foinseach le léamh as.
:param offset: (fritháireamh) An fritháireamh isteach sa mhaolán. D'fhéadfadh sé a bheith diúltach le comhaireamh ó dheireadh an mhaoláin.
:return: A tuple of the unpacked values."""
    ...