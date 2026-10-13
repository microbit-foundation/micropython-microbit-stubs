"""Empacotar e desempacotar tipos de dados primitivos. (estrutura)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Obtém o número de bytes necessários para armazenar o dado ``fmt``. (tamanho do cálculo)

Example: ``struct.calcsize('hf')``

:param fmt: Uma string de formato.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Empacota valores de acordo com uma string de formato. (empacotar)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: A string de formato.
:param v1: O primeiro valor.
:param *vn: Os valores restantes.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Empacota valores de acordo com uma string de formato. (empacotar em)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: A string de formato.
:param buffer: (Tampão) O buffer de destino para gravar.
:param offset: (deslocamento) O deslocamento no buffer. Pode ser negativo para contar a partir do final do buffer.
:param v1: O primeiro valor.
:param *vn: Os valores restantes."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Desempacota dados de acordo com uma string de formato. (descompactar)

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: A string de formato.
:param data: (dados) Os dados.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Desempacota dados de um buffer de acordo com uma string de formato. (desempacotar de)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: A string de formato.
:param buffer: (Tampão) O buffer de origem para leitura.
:param offset: (deslocamento) O deslocamento no buffer. Pode ser negativo para contar a partir do final do buffer.
:return: A tuple of the unpacked values."""
    ...