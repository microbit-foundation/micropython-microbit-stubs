"""Communicate with devices using the I²C bus protocol.
"""

from _typeshed import ReadableBuffer
from . import MicroBitDigitalPin, pin19, pin20
from typing import List, Union
from . import pin19, pin20

def init(
    freq: int = 100000, sda: MicroBitDigitalPin = pin20, scl: MicroBitDigitalPin = pin19
) -> None:
    """Re-initialize a peripheral.

    :param freq: clock frequency
    :param sda: ``sda`` pin (default 20)
    :param scl: ``scl`` pin (default 19)

    On a micro:bit V1 board, changing the I²C pins from defaults will make
    the accelerometer and compass stop working, as they are connected
    internally to those pins. This warning does not apply to the **V2**
    revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
    for the motion sensors and the edge connector.
    """
    ...

def scan() -> List[int]:
    """Scan the bus for devices.

    :return: A list of 7-bit addresses corresponding to those devices that responded to the scan.
    """
    ...

def read(addr: int, n: int, repeat: bool = False) -> bytes:
    """Read bytes from a device..

    :param addr: The 7-bit address of the device
    :param n: The number of bytes to read
    :param repeat: If ``True``, no stop bit will be sent
    :return: The bytes read
    """
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool = False) -> None:
    """Write bytes to a device.

    :param addr: The 7-bit address of the device
    :param buf: A buffer containing the bytes to write
    :param repeat: If ``True``, no stop bit will be sent
    """
    ...
