"""Cumarsáid a dhéanamh le gléasanna ag baint úsáide as prótacal bus I²C."""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """Ath-thúsaigh forimeallach.

Example: ``i2c.init()``

:param freq: minicíocht cloig
:param sda: biorán ``sda`` (réamhshocrú 20)
:param scl: biorán ``scl`` (réamhshocrú 19)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """Scan an bus le haghaidh gléasanna. (scanadh)

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """Léigh bearta ó ghléas. (léigh)

Example: ``i2c.read(0x50, 64)``

:param addr: Seoladh 7 ngiotán an ghléis
:param n: Líon na mbeart atá le léamh
:param repeat: (athdhéanamh) Má ``True``, ní sheolfar aon ghiotán stad
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """Scríobh bearta chuig gléas. (scríobh)

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: Seoladh 7 ngiotán an ghléis
:param buf: Maolán ina bhfuil na bearta le scríobh
:param repeat: (athdhéanamh) Má ``True``, ní sheolfar aon ghiotán stad"""
    ...