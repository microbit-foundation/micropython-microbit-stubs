"""Cumarsáid a dhéanamh le gléas ag baint úsáide as comhéadan sraitheach."""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""Paireacht chorr (corr)"""
EVEN: int
"""Paireacht fiú (fiú amháin)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """Túsaigh cumarsáid sraitheach.

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: Luas na cumarsáide.
:param bits: Méid na mbeart atá á dtarchur. micro:bit: ní thacaíonn giotán ach le 8.
:param parity: (paireacht) Conas a dhéantar paireacht a sheiceáil, ``None``, ``uart.ODD`` nó ``uart.EVEN``.
:param stop: (stad) Líon na ngiotán stad, caithfidh sé a bheith 1 le haghaidh micro:bit.
:param tx: Bioráin a tharchur.
:param rx: Biorán glactha.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """Seiceáil an bhfuil aon sonraí ag fanacht. (aon)

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """Léigh bearta. (léamh)

Example: ``uart.read()``

:param nbytes: Má tá ``nbytes`` sonraithe ansin léigh ar a mhéad go leor beart, nó léigh an oiread beart agus is féidir
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """Léigh bearta isteach sa ``buf``.

Example: ``uart.readinto(input_buffer)``

:param buf: An maolán le scríobh chuige.
:param nbytes: Má tá ``nbytes`` sonraithe ansin léigh ar a mhéad go leor bearta, ar shlí eile a léamh ``len(buf)`` bearta.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """Léigh líne, ag críochnú i gcarachtar líne nua.

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """Scríobh maolán ar an mbus. (scríobh)

Example: ``uart.write('hello world')``

:param buf: Réad beart nó teaghrán.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...