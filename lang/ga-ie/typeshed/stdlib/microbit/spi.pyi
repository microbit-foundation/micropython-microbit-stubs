"""Cumarsáid a dhéanamh le gléasanna ag baint úsáide as an gcomhéadan forimeallach sraitheach (SPI) bus."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Túsaigh cumarsáid SPI.

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: (ráta baud) Luas na cumarsáide.
:param bits: (giotáin) An leithead i giotán de gach aistriú. Faoi láthair ní thacaítear ach le ``bits=8`` . Mar sin féin, d'fhéadfadh sé seo athrú amach anseo.
:param mode: (mód) Cinneann sé an meascán de polaraíocht clog agus céim - 'féach tábla ar líne <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>'_.
:param sclk: bioráin sclk (réamhshocrú 13)
:param mosi: bioráin mosi (réamhshocrú 15)
:param miso: biorán miso (réamhshocraithe 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """Léigh ar a mhéad ``nbytes`` agus an beart aonair a thugann ``out``á scríobh go leanúnach. (léamh)

Example: ``spi.read(64)``

:param nbytes: (nbeart) Líon uasta na mbeart le léamh.
:param out: (amach) An luach beart le scríobh (réamhshocrú 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Scríobh bearta chuig an mbus. (scríobh)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (maolán) Maolán chun sonraí a léamh as."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Scríobh an maolán ``out`` chuig an mbus agus léigh aon fhreagra isteach sa mhaolán ``in_`` . (scríobh readinto)

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: (amach) An maolán chun aon fhreagra a scríobh.
:param in_: (i) An maolán chun sonraí a léamh as."""
    ...