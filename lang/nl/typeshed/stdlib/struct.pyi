"""Primitieve datatypes inpakken en uitpakken."""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Haal het aantal bytes op dat nodig is om de gegeven ``fmt`` op te slaan.

Example: ``struct.calcsize('hf')``

:param fmt: Tekenreeks opmaak.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Verpak de waarden op basis van een string formaat. (inpakken)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: De formaat tekenreeks.
:param v1: De eerste waarde.
:param *vn: De resterende waarden.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Verpak de waarden op basis van een string formaat. (inpakken)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: De formaat tekenreeks.
:param buffer: De doelbuffer om in te schrijven.
:param offset: (Offset) De compensatie in de buffer. Kan negatief zijn om te tellen aan het einde van de buffer.
:param v1: De eerste waarde.
:param *vn: De resterende waarden."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Uitpakken van gegevens volgens een opmaakreeks. (uitpakken)

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: De formaat tekenreeks.
:param data: (gegevens) De gegevens.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Uitpakken van gegevens van een buffer volgens een opmaak. (uitpakken van)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: De formaat tekenreeks.
:param buffer: De bronbuffer om uit te lezen.
:param offset: (Offset) De compensatie in de buffer. Kan negatief zijn om te tellen aan het einde van de buffer.
:return: A tuple of the unpacked values."""
    ...