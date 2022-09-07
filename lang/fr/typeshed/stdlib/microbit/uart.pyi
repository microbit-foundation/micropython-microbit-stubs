"""Communiquer avec un périphérique à l'aide d'une interface série. (uart)"""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Parité impaire (odd)"""
EVEN: int
"""Parité paire (even)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Initialiser la communication série. (init)

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: (baudrate) La vitesse de communication.
:param bits: (bits) La taille des octets transmis. micro:bit ne prend en charge que 8.
:param parity: (parity) Comment la parité est vérifiée, ``None``, ``uart.ODD`` ou ``uart.EVEN``.
:param stop: (stop) Le nombre de bits d'arrêt, doit être 1 pour micro:bit.
:param tx: (tx) Broche de transmission.
:param rx: (rx) Broche de réception.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Check if any data is waiting. (any)

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Lire des octets. (read)

Example: ``uart.read()``

:param nbytes: (nbytes) Si ``nbytes`` est spécifié, alors lire au maximum cette quantité d'octets, sinon lire autant d'octets que possible
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Lire les octets dans le ``buf``. (readinto)

Example: ``uart.readinto(input_buffer)``

:param buf: (buf) Le buffer dans lequel écrire.
:param nbytes: (nbytes) Si ``nbytes`` est spécifié, alors lire au maximum cette quantité d'octets, sinon lire ``len(buf)`` octets.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Lire une ligne terminée par un caractère de nouvelle ligne. (readline)

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Écrire un buffer sur un bus (write)

Example: ``uart.write('hello world')``

:param buf: (buf) Un objet d'octets ou une chaîne de caractères.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...