"""Empaquetar y desempaquetar tipos de dato primitivos. (estruc)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Obtiene el número de bytes necesarios para almacenar el ``fmt`` dado. (calctamaño)

Example: ``struct.calcsize('hf')``

:param fmt: Una cadena de formato.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Empaqueta valores según una cadena de formato. (empaquetar)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: La cadena de formato.
:param v1: El primer valor.
:param *vn: Los valores restantes.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Empaqueta valores según una cadena de formato. (empaquetar en)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: La cadena de formato.
:param buffer: (búfer) El búfer de destino en el que se va a escribir.
:param offset: (desplazamiento) El desplazamiento en el búfer. Puede ser negativo para contar desde el final del búfer.
:param v1: El primer valor.
:param *vn: Los valores restantes."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Desempaqueta datos según una cadena de formato. (desempaquetar)

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: La cadena de formato.
:param data: (datos) Los datos.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Desempaqueta datos de un búfer según una cadena de formato. (desempaquetar de)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: La cadena de formato.
:param buffer: (búfer) El búfer de origen del que leer.
:param offset: (desplazamiento) El desplazamiento en el búfer. Puede ser negativo para contar desde el final del búfer.
:return: A tuple of the unpacked values."""
    ...