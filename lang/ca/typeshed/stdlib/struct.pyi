"""Empaquetar i desempaquetar tipus de dades primitius. (struct (Empaqueta i desempaqueta tipus de dades primitius))"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Obté el nombre de bytes necessaris per emmagatzemar el ``fmt`` donat. (calcsize (calcula la mida))

Example: ``struct.calcsize('hf')``

:param fmt: (format (fmt)) Una cadena de format.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Empaqueta els valors segons una cadena de format. (pack (empaqueta))

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: (format (fmt)) La cadena de format.
:param v1: El primer valor.
:param *vn: La resta de valors.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Empaqueta els valors segons una cadena de format. (pack into (empaquetar a))

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: (fmt (format)) La cadena de format.
:param buffer: (memòria intermèdia (buffer)) La memòria intermèdia de destinació on escriure.
:param offset: (desplaçament (offset)) El desplaçament a la memòria intermèdia (buffer). Pot ser negatiu per comptar des del final de la memòria intermèdia.
:param v1: El primer valor.
:param *vn: La resta de valors."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Desempaqueta les dades segons una cadena de format. (unpack (desempaqueta))

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: (format (fmt)) La cadena de format.
:param data: (dades (data)) Les dades.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Desempaqueta les dades d'una memòria intermèdia (buffer) segons una cadena de format. (desempaqueta des de)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: (format (fmt)) La cadena de format.
:param buffer: (memòria intermèdia (buffer)) La memòria intermèdia (buffer) d'origen d'on llegir.
:param offset: (desplaçament (offset)) El desplaçament a la memòria intermèdia (buffer). Pot ser negatiu per comptar des del final de la memòria intermèdia.
:return: A tuple of the unpacked values."""
    ...