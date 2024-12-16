"""Comunica amb un dispositiu mitjançant una interfície sèrie."""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Paritat senar (senar)"""
EVEN: int
"""Paritat parella (parell)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Inicialitzar la comunicació en sèrie.

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: (Velocitat de bauds) La velocitat de comunicació.
:param bits: La mida dels bytes que es transmeten. micro:bit només n'admet 8.
:param parity: (paritat) Com es verifica la paritat, ``None``, ``uart.ODD`` o ``uart.EVEN``.
:param stop: (atura) El nombre de bits de parada ha de ser 1 per micro:bit.
:param tx: Pin transmissor.
:param rx: Receiving pin.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Verifica si hi ha alguna data esperant.

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Llegeix bytes (llegeix)

Example: ``uart.read()``

:param nbytes: Si s'especifica ``nbytes``, llegeix com a màxim tants bytes, en cas contrari llegeix tants bytes com sigui possible
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Llegeix bytes al ``buf``.

Example: ``uart.readinto(input_buffer)``

:param buf: La memòria intermèdia a on escriure.
:param nbytes: Si s'especifica ``nbytes``, llegeix com a màxim aquests bytes, en cas contrari llegeix ``len(buf)`` bytes.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Llegir una línia que acaba en un caràcter de nova línia.

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Escriu una memòria intermèdia al bus (escriu)

Example: ``uart.write('hello world')``

:param buf: Un objecte bytes o una cadena.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...