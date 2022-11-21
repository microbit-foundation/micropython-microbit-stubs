"""Communiceer met een apparaat via een seriële interface."""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Oneven pariteit (oneven)"""
EVEN: int
"""Even pariteit"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Initialiseer seriële communicatie. (initialiseren)

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: De snelheid van de communicatie.
:param bits: De grootte van de bytes die worden verzonden. micro:bit ondersteunt slechts 8.
:param parity: (pariteit) Hoe de pariteit is aangevinkt, ``None``, ``uart.ODD`` of ``uart.EVEN``.
:param stop: Het aantal stop bits, moet 1 zijn voor micro:bit.
:param tx: Verzend pin.
:param rx: Ontvangende pin.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Controleer of er nog gegevens staan te wachten. (elke)

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Lees bytes. (lezen)

Example: ``uart.read()``

:param nbytes: Als ``nbytes`` is gespecificeerd, lees dan maximaal zoveel bytes, anders lees zo veel mogelijk bytes
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Lees bytes in de ``buf``. (inlezen)

Example: ``uart.readinto(input_buffer)``

:param buf: De buffer om naar te schrijven.
:param nbytes: Als ``nbytes`` is gespecificeerd, lees dan hooguit zoveel bytes, anders lees ``len(buf)`` bytes.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Lees een regel, eindigend in een nieuw karakter regel. (leesregel)

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Schrijf bytes naar de bus. (schrijven)

Example: ``uart.write('hello world')``

:param buf: Een bytes object of een tekenreeks.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...