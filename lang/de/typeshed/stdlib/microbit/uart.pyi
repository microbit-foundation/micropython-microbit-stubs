"""Kommunikation mit einem Gerät über eine serielle Schnittstelle."""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Ungerade Parität"""
EVEN: int
"""Gerade Parität (gerade)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Initialisiert die serielle Kommunikation.

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: (Baudrate) Die Übertragungsgeschwindigkeit.
:param bits: (Bits) Die Größe der Bytes die übertragen werden. micro:bit unterstützt nur 8.
:param parity: (Parität) Wie Parität geprüft wird, ``None``, ``uart.ODD`` oder ``uart.EVEN``.
:param stop: (Stop) Die Anzahl der Stopbits, muss 1 für micro:bit sein.
:param tx: Sendepin.
:param rx: Empfangspin.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Überprüft, ob irgendwelche Daten warten.

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Bytes lesen.

Example: ``uart.read()``

:param nbytes: Wenn ``nbytes`` angegeben ist, werden höchstens so viele Bytes gelesen. Andernfalls werden so viele Bytes wie möglich gelesen.
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Liest Bytes in ``buf``.

Example: ``uart.readinto(input_buffer)``

:param buf: Der Puffer, in den geschrieben werden soll.
:param nbytes: Wenn ``nbytes`` angegeben ist, werden höchstens so viele Bytes gelesen. Andernfalls werden ``len(buf)`` Bytes gelesen.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Liest eine Zeile bis zu einem Zeilenumbruch.

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Schreibt einen Puffer auf den Bus. (schreiben)

Example: ``uart.write('hello world')``

:param buf: Ein Byte-Objekt oder ein String.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...