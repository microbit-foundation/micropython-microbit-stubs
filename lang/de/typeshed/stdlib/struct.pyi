"""Packe und entpacke primitive Datentypen. (struktur)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Rufe die Anzahl der benötigten Bytes ab, um den angegebenen ``fmt`` zu speichern.

Example: ``struct.calcsize('hf')``

:param fmt: Ein Format-String.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Werte nach einem Format-String packen. (packen)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: Der Formatstring
:param v1: Der erste Wert.
:param *vn: Die verbleibenden Werte.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Werte nach einem Format-String packen. (packen in)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: Der Formatstring
:param buffer: (Puffer) Der Buffer, in den geschrieben werden soll.
:param offset: Der Offset in den Puffer. Kann negativ sein, um vom Ende des Puffers aus zu zählen.
:param v1: Der erste Wert.
:param *vn: Die verbleibenden Werte."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Daten nach einem Format-String entpacken.

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: Der Formatstring
:param data: (Daten) Die Daten.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Daten aus einem Puffer nach einem Format-String entpacken. (entpacken von)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: Der Formatstring
:param buffer: (Puffer) Der Quellpuffer, von dem gelesen werden soll.
:param offset: Der Offset in den Puffer. Kann negativ sein, um vom Ende des Puffers aus zu zählen.
:return: A tuple of the unpacked values."""
    ...