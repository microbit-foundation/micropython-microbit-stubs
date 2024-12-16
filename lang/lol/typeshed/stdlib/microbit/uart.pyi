"""crwdns330312:0crwdne330312:0 (crwdns330310:0crwdne330310:0)"""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""crwdns330316:0crwdne330316:0 (crwdns330314:0crwdne330314:0)"""
EVEN: int
"""crwdns330320:0crwdne330320:0 (crwdns330318:0crwdne330318:0)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """crwdns330324:0crwdne330324:0 (crwdns330322:0crwdne330322:0)

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: (crwdns330326:0crwdne330326:0) crwdns330328:0crwdne330328:0
:param bits: (crwdns330330:0crwdne330330:0) crwdns330332:0crwdne330332:0
:param parity: (crwdns330334:0crwdne330334:0) crwdns330336:0``None``crwdnd330336:0``uart.ODD``crwdnd330336:0``uart.EVEN``crwdne330336:0
:param stop: (crwdns330342:0crwdne330342:0) crwdns330344:0crwdne330344:0
:param tx: (crwdns330346:0crwdne330346:0) crwdns330348:0crwdne330348:0
:param rx: (crwdns330338:0crwdne330338:0) crwdns330340:0crwdne330340:0

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """crwdns334688:0crwdne334688:0 (crwdns330350:0crwdne330350:0)

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """crwdns330356:0crwdne330356:0 (crwdns330354:0crwdne330354:0)

Example: ``uart.read()``

:param nbytes: (crwdns330358:0crwdne330358:0) crwdns330360:0``nbytes``crwdne330360:0
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """crwdns330364:0``buf``crwdne330364:0 (crwdns330362:0crwdne330362:0)

Example: ``uart.readinto(input_buffer)``

:param buf: (crwdns330366:0crwdne330366:0) crwdns330368:0crwdne330368:0
:param nbytes: (crwdns330370:0crwdne330370:0) crwdns330372:0``nbytes``crwdnd330372:0``len(buf)``crwdne330372:0
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """crwdns330376:0crwdne330376:0 (crwdns330374:0crwdne330374:0)

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """crwdns330380:0crwdne330380:0 (crwdns330378:0crwdne330378:0)

Example: ``uart.write('hello world')``

:param buf: (crwdns330382:0crwdne330382:0) crwdns330384:0crwdne330384:0
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...