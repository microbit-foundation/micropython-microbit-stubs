"""Comunicarse con dispositivos que usan el bus de interfaz de periféricos serie (SPI, por sus siglas en inglés). (spi)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Inicializa la comunicación SPI. (init)

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: (baudrate) La velocidad de comunicación.
:param bits: (bits) El ancho en bits de cada transferencia. Actualmente solo se admite ``bits=8}, pero esto puede cambiar en el futuro.
:param mode: (mode) Determina la combinación de fase y polaridad del reloj - `ver tabla en línea <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: (sclk) pin SCLK (por defecto, 13)
:param mosi: (mosi) pin MOSI (por defecto, 15)
:param miso: (miso) pin MISO (por defecto, 14)"""
    ...

def read(nbytes: int) -> bytes:
    """Lee bytes. (read)

Example: ``spi.read(64)``

:param nbytes: (nbytes) Número máximo de bytes a leer.
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Escribe bytes en el bus. (write)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (buffer) Un búfer del que leer datos."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Escribe el búfer ``out`` en el bus y lee cualquier respuesta en el búfer ``in_``. (write readinto)

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: (out) El búfer en el que escribe una respuesta.
:param in_: (in) El búfer del que leer datos."""
    ...