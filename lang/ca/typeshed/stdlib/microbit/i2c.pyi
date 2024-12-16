"""Comunicar-se amb dispositius mitjançant el protocol de bus I²C."""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """Reinicialitzar un perifèric.

Example: ``i2c.init()``

:param freq: freqüència del rellotge
:param sda: Pin ``sda`` (per defecte 20)
:param scl: pin ``scl``  (per defecte 19)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """Escaneja el bus dels dispositius

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """Llegeix bytes des d'un dispositiu. (llegeix)

Example: ``i2c.read(0x50, 64)``

:param addr: L'adreça de 7-bit del dispositiu
:param n: El nombre de bytes a llegir
:param repeat: (repeteix) Si ``True``, no s'enviarà cap bit d'aturada
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """Escriu bytes en un dispositiu (escriu)

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: L'adreça de 7-bit del dispositiu
:param buf: Una memòria intermèdia que conté els bytes per escriure
:param repeat: (repeteix) Si ``True``, no s'enviarà cap bit d'aturada"""
    ...