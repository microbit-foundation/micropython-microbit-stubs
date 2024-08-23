"""Pakuj i rozpakowuj prymitywne typy danych."""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Uzyskaj liczbę bajtów potrzebnych do przechowywania podanego ``fmt``.

Example: ``struct.calcsize('hf')``

:param fmt: Łańcuch formatu.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Upakuj wartości zgodnie z łńcuchem formatu.

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: Łańcuch formatu.
:param v1: Pierwsza wartość.
:param *vn: Pozostałe wartości.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Upakuj wartości zgodnie z łńcuchem formatu.

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: Łańcuch formatu.
:param buffer: Bufor docelowy do zapisu.
:param offset: Przesunięcie do bufora. Wartość ujemna może być liczona od końca bufora.
:param v1: (w1) Pierwsza wartość.
:param *vn: Pozostałe wartości."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Rozpakuj dane zgodnie z łańcuchem formatu.

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: Łańcuch formatu.
:param data: Dane
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Rozpakuj dane z buforu zgodnie z łańcuchem formatu.

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: Łańcuch formatu.
:param buffer: Bufor źródłowy do odczytu.
:param offset: Przesunięcie do bufora. Wartość ujemna może być liczona od końca bufora.
:return: A tuple of the unpacked values."""
    ...