"""Comunicarse con un dispositivo usando una interfaz serie. (uart)"""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Paridad impar (odd)"""
EVEN: int
"""Paridad par (even)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Inicializa la comunicación serie. (init)

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: (baudrate) La velocidad de comunicación.
:param bits: (bits) El tamaño de bytes transmitidos; micro:bit solo admite 8.
:param parity: (parity) Cómo se comprueba la paridad: ``None``, ``uart.ODD`` o ``uart.EVEN``.
:param stop: (stop) El número de bits de parada; tiene que ser 1 para el micro:bit.
:param tx: (tx) Pin transmisor.
:param rx: (rx) Pin receptor.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Comprueba si hay algún dato esperando. (any)

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Lee bytes. (read)

Example: ``uart.read()``

:param nbytes: (nbytes) Si se especifica ``nbytes``, lee como máximo ese número de bytes; si no, lee tantos bytes como sea posible
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Lee bytes en el ``buf``. (readinto)

Example: ``uart.readinto(input_buffer)``

:param buf: (buf) El búfer en el que escribir.
:param nbytes: (nbytes) Si se especifica ``nbytes``, lee como máximo ese número de bytes; si no, lee ``len(buf)`` bytes.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Lee una línea, terminando en un carácter de nueva línea. (readline)

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Escribe un búfer en el bus. (write)

Example: ``uart.write('hello world')``

:param buf: (buf) Un objeto de bytes o una cadena.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...