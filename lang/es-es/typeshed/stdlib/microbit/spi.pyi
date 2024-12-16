"""Comunicarse con dispositivos que usan el bus de interfaz de periféricos serie (SPI, por sus siglas en inglés)."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Inicializa la comunicación SPI.

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: (tasa de baudios) La velocidad de comunicación.
:param bits: El ancho en bits de cada transferencia. Actualmente solo se admite ``bits=8}, pero esto puede cambiar en el futuro.
:param mode: (modo) Determina la combinación de fase y polaridad del reloj - `ver tabla en línea <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: pin SCLK (por defecto, 13)
:param mosi: pin MOSI (por defecto, 15)
:param miso: pin MISO (por defecto, 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """Lee como máximo ``nbytes`` mientras está escribiendo continuamente el byte individual dado por ``out``. (leer)

Example: ``spi.read(64)``

:param nbytes: Número máximo de bytes a leer.
:param out: (salida) El valor del byte a escribir (por defecto 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Escribe bytes en el bus. (escribir)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (búfer) Un búfer del que leer datos."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Escribe el búfer ``out`` en el bus y lee cualquier respuesta en el búfer ``in_``. (escritura leeren)

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: (a) El búfer en el que escribe una respuesta.
:param in_: (de) El búfer del que leer datos."""
    ...