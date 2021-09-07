"""The ``i2c`` module lets you communicate with devices connected to your board
using the I²C bus protocol. There can be multiple slave devices connected at
the same time, and each one has its own unique address, that is either fixed
for the device or configured on it. Your board acts as the I²C master.

We use 7-bit addressing for devices because of the reasons stated
`here <http://www.totalphase.com/support/articles/200349176-7-bit-8-bit-and-10-bit-I2C-Slave-Addressing>`_.

This may be different to other micro:bit related solutions.

How exactly you should communicate with the devices, that is, what bytes to
send and how to interpret the responses, depends on the device in question and
should be described separately in that device's documentation.
"""

from . import MicroBitDigitalPin, pin19, pin20
from typing import List, Union
from . import pin19, pin20


def init(freq: int = 100000, sda: MicroBitDigitalPin = pin20, scl: MicroBitDigitalPin = pin19) -> None:
    """Re-initialize peripheral with the specified clock frequency ``freq`` on the
    specified ``sda`` and ``scl`` pins.

    .. warning::

        On a micro:bit V1 board, changing the I²C pins from defaults will make
        the accelerometer and compass stop working, as they are connected
        internally to those pins. This warning does not apply to the **V2**
        revision of the micro:bit as this has `separate I²C lines
        <https://tech.microbit.org/hardware/i2c/>`_
        for the motion sensors and the edge connector.
    """
    ...

def scan() -> List[int]:
    """Scan the bus for devices.  Returns a list of 7-bit addresses corresponding
    to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool = False) -> bytes:
    """Read ``n`` bytes from the device with 7-bit address ``addr``. If ``repeat``
    is ``True``, no stop bit will be sent.
    """
    ...


def write(addr: int, buf: Union[bytes, bytearray], repeat=False) -> None:
    """Write bytes from ``buf`` to the device with 7-bit address ``addr``. If
    ``repeat`` is ``True``, no stop bit will be sent.
    """
    ...