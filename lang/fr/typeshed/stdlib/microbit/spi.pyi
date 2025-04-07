"""Communiquer avec les périphériques à l'aide du bus SPI (Serial Peripheral Interface)."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Initialiser la communication SPI.

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: La vitesse de communication.
:param bits: La largeur en bits de chaque transfert. Actuellement, seul ``bits=8`` est pris en charge. Cependant, cela peut évoluer à l'avenir.
:param mode: Détermine la combinaison de la polarité et de la phase de l'horloge. - `voir le tableau en ligne <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: Broche sclk (13 par défaut)
:param mosi: Broche mosi (15 par défaut)
:param miso: Broche miso (14 par défaut)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """Lire au maximum ``nbytes`` tout en écrivant continuellement l'octet unique donné par ``out``.

Example: ``spi.read(64)``

:param nbytes: Nombre maximal d'octets à lire.
:param out: La valeur d'octet à écrire (0 par défaut).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Écrire des octets sur le bus.

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: Un buffer à partir duquel lire les données."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Ecrire le buffer ``out`` sur le bus et lire toute réponse dans le buffer ``in_``.

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: Le buffer vers lequel écrire une réponse.
:param in_: Le buffer depuis lequel lire les données."""
    ...