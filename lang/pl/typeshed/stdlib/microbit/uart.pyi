"""Komunikuj się z urządzeniem za pomocą interfejsu szeregowego."""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Nieparzysta parzystość"""
EVEN: int
"""Parzysta parzystość"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Zainicjuj komunikację seryjną.

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: Szybkość komunikacji.
:param bits: Rozmiar przesyłanych bajtów. micro:bit obsługuje tylko 8.
:param parity: Jak sprawdzana jest parzystość, ``None``, ``uart.ODD`` lub ``uart.EVEN``.
:param stop: Liczba bitów stopu musi wynosić 1 dla micro:bita.
:param tx: Transmitując pin.
:param rx: Odbieranie pinu.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Sprawdź, czy czekają jakieś dane.

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Czytaj bajty.

Example: ``uart.read()``

:param nbytes: Jeśli ``nbytes`` jest określony, przeczytaj co najwyżej tę liczbę bajtów, w przeciwnym razie przeczytaj jak najwięcej bajtów
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Przeczytaj bajty do ``buf``.

Example: ``uart.readinto(input_buffer)``

:param buf: Bufor do zapisu.
:param nbytes: Jeśli ``nbytes`` jest określony,  przeczytaj co najwyżej tę liczbę bajtów, w przeciwnym razie przeczytaj ``len(buf)`` bajtów.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Przeczytaj wiersz kończący się znakiem nowej linii.

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Zapisz bufor na magistrali.

Example: ``uart.write('hello world')``

:param buf: Obiekt bajtów lub łańcuch.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...