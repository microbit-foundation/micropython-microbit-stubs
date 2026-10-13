"""Comunique-se com um dispositivo usando uma ‘interface’ de série."""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Paridade ímpar (ímpar)"""
EVEN: int
"""Paridade par (par)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Inicializar comunicação serial. (iniciar)

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: (Taxa de transmissão) A velocidade da comunicação.
:param bits: O tamanho dos ‘bytes’ sendo transmitidos. Micro:bit suporta apenas 8.
:param parity: (paridade) Como a paridade é verificada, ``None``, ``uart.ODD`` ou ``uart.EVEN``.
:param stop: (parar) O número de bits de parada, precisa ser de 1 para micro:bit.
:param tx: Pino de transmissão.
:param rx: Pino receptor.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Verifique se algum dado está esperando. (algum)

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Ler ‘bytes’. (ler)

Example: ``uart.read()``

:param nbytes: Se ``nbytes`` for especificado, então leia no máximo essa quantidade de bytes, caso contrário, leia o máximo de bytes possível
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Ler bytes para o ``buf``. (ler diretamente)

Example: ``uart.readinto(input_buffer)``

:param buf: O buffer para onde escrever.
:param nbytes: Se ``nbytes`` for especificado, leia no máximo essa quantidade de bytes, caso contrário, leia ``len(buf)`` bytes.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Ler uma linha, terminando com um caractere de nova linha. (ler linha)

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Escrever um buffer no barramento. (escrever)

Example: ``uart.write('hello world')``

:param buf: Um objeto de bytes ou uma string.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...