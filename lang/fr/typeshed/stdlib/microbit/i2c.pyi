"""Communiquer avec les périphériques en utilisant le protocole de bus I²C."""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """Réinitialiser un périphérique.

Example: ``i2c.init()``

:param freq: fréquence d'horloge
:param sda: Broche ``sda`` (19 par défaut)
:param scl: Broche ``scl`` (19 par défaut)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """Scanner le bus pour détecter des périphériques.

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """Lire des octets depuis un périphérique.

Example: ``i2c.read(0x50, 64)``

:param addr: L'adresse 7-bit du périphérique
:param n: Le nombre d'octets à lire
:param repeat: Si ``True``, aucun bit d'arrêt ne sera envoyé
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """Écrire des octets sur un périphérique.

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: L'adresse 7-bit du périphérique
:param buf: Un buffer contenant les octets à écrire
:param repeat: Si ``True``, aucun bit d'arrêt ne sera envoyé"""
    ...