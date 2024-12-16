"""Komunikuj się z urządzeniami za pomocą magistrali szeregowego interfejsu (SPI)."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Zainicjuj komunikację SPI.

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: Szybkość komunikacji.
:param bits: Szerokość w bitach każdego transferu. Obecnie obsługiwanych jest tylko ``bits=8``. Może to jednak ulec zmianie w przyszłości.
:param mode: Określa połączenie polarności zegara i fazy - `zobacz tabelę online <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: pin sclk (domyślnie 13)
:param mosi: pin mosi (domyślnie 15)
:param miso: pin miso (domyślnie 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """Przeczytaj co najwyżej ``nbytes`` podczas ciągłego pisania pojedynczego bajtu danego przez ``out``.

Example: ``spi.read(64)``

:param nbytes: Maksymalna liczba bajtów do odczytu.
:param out: Wartość bajtu do zapisu (domyślnie 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Zapisz bajty na magistrali.

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: Bufor do odczytu danych."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Zapisz bufor ``out`` do magistrali i wczytaj dowolną odpowiedź do bufora ``in_``.

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: Bufor do zapisu dowolnej odpowiedzi.
:param in_: Bufor do odczytu danych."""
    ...