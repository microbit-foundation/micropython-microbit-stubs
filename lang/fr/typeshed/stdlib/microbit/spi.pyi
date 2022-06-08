"""Communicate with devices using the serial peripheral interface (SPI) bus. (spi)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Initialize SPI communication. (init)

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: (baudrate) The speed of communication.
:param bits: (bits) The size of bytes being transmitted. Currently only ``bits=8`` is supported. However, this may change in the future.
:param mode: (mode) Determines the combination of clock polarity and phase - `see online table <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: (sclk) sclk pin (default 13)
:param mosi: (mosi) mosi pin (default 15)
:param miso: (miso) miso pin (default 14)"""
    ...

def read(nbytes: int) -> bytes:
    """Read bytes. (read)

Example: ``spi.read(64)``

:param nbytes: (nbytes) Maximum number of bytes to read.
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Write bytes to the bus. (write)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (buffer) A buffer to read data from."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Write the ``out`` buffer to the bus and read any response into the ``in_`` buffer. (write readinto)

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: (out) The buffer to write any response to.
:param in_: (in) The buffer to read data from."""
    ...