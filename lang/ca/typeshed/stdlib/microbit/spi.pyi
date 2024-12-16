"""Comunica amb dispositius mitjançant el bus d'interfície perifèrica sèrie (SPI)."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Inicialitzar la comunicació SPI.

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: (Velocitat de bauds) La velocitat de comunicació.
:param bits: L'amplada en bits de cada transferència. Actualment només ``bits=8`` és acceptada . Tot i que això pot canviar en el futur
:param mode: Determina la combinació de polaritat i fase del rellotge: `consulta la taula en línia <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: pin sclk (per defecte 13)
:param mosi: mosi pin (per defecte 15)
:param miso: miso pin (per defecte 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """Llegeix com a màxim ``nbytes`` mentre escriu contínuament l'únic byte donat per ``out``. (llegeix)

Example: ``spi.read(64)``

:param nbytes: Nombre màxim de bytes per llegir.
:param out: El valor del byte a escriure (per defecte 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Escriu bytes al bus. (escriu)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (memòria intermèdia) Una memòria intermèdia per a llegir dades."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Escriu la memòria intermèdia ``out`` al bus i llegeix qualsevol resposta a la memòria intermèdia ``in_``.

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: La memòria intermèdia per a escriure qualsevol resposta.
:param in_: La memòria intermèdia per a llegir dades."""
    ...