"""Communiceer met apparaten met behulp van het I²C bus protocol."""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """Initialiseer een randapparaat opnieuw. (initialiseren)

Example: ``i2c.init()``

:param freq: (frequentie) klok frequentie
:param sda: ``sda`` pin (standaard 20)
:param scl: ``scl`` pin (standaard 19)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """Scan de bus op apparaten. (scannen)

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """Lees bytes van een apparaat. (lezen)

Example: ``i2c.read(0x50, 64)``

:param addr: Het 7-bit adres van het apparaat
:param n: Het aantal te lezen bytes
:param repeat: (herhaal) Als ``True``, zal er geen stop bit worden verzonden
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """Schrijven van bytes naar een apparaat. (schrijven)

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: Het 7-bit adres van het apparaat
:param buf: Een buffer met de te schrijven bytes
:param repeat: (herhaal) Als ``True``, zal er geen stop bit worden verzonden"""
    ...