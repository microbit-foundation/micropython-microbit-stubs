"""Communiceer met apparaten met behulp van de seriële perifere interface (SPI) bus."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Initialiseer SPI communicatie. (initialiseren)

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: De snelheid van de communicatie.
:param bits: De breedte in bits van elke overdracht. Momenteel wordt alleen ``bits=8`` ondersteund. Dit kan echter veranderen in de toekomst.
:param mode: (modus) Bepaalt de combinatie van klokpolariteit en fase - `zie online tabel <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: sclk pin (standaard 13)
:param mosi: mosi pin (standaard 15)
:param miso: miso pin (standaard 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """Lees minstens ``nbytes`` terwijl het enkele byte gegeven in ``out`` continu geschreven wordt. (lezen)

Example: ``spi.read(64)``

:param nbytes: Maximum aantal te lezen bytes.
:param out: (uit) De byte-waarde om te schrijven (standaard 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Schrijf bytes naar de bus. (schrijven)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: Een buffer om gegevens van te lezen."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Schrijf de ``out`` buffer naar de bus en lees elke reactie in de ``in_`` buffer. (schrijf readinto)

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: (uit) De buffer om een reactie naar te schrijven.
:param in_: De buffer om gegevens van te lezen."""
    ...