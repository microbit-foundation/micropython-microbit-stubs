"""Comunicarse con un dispositivo usando una interfaz serie."""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Paridad impar (impar)"""
EVEN: int
"""Paridad par (par)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Inicializa la comunicación serie.

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: (tasa de baudios) La velocidad de comunicación.
:param bits: El tamaño de bytes transmitidos; micro:bit solo admite 8.
:param parity: (paridad) Cómo se comprueba la paridad: ``None``, ``uart.ODD`` o ``uart.EVEN``.
:param stop: (detener) El número de bits de parada; tiene que ser 1 para el micro:bit.
:param tx: Pin transmisor.
:param rx: Pin receptor.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Comprueba si hay datos en espera. (algún)

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Lee bytes. (leer)

Example: ``uart.read()``

:param nbytes: Si se especifica ``nbytes``, lee como máximo ese número de bytes; si no, lee tantos bytes como sea posible
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Lee bytes en el ``buf``. (leeren)

Example: ``uart.readinto(input_buffer)``

:param buf: (búf) El búfer en el que escribir.
:param nbytes: Si se especifica ``nbytes``, lee como máximo ese número de bytes; si no, lee ``len(buf)`` bytes.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Lee una línea, terminando en un carácter de nueva línea. (leerlínea)

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Escribe un búfer en el bus. (escribir)

Example: ``uart.write('hello world')``

:param buf: (búf) Un objeto de bytes o una cadena.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...