"""crwdns330140:0crwdne330140:0 (crwdns330138:0crwdne330138:0)"""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """crwdns330144:0crwdne330144:0 (crwdns330142:0crwdne330142:0)

Example: ``i2c.init()``

:param freq: (crwdns330146:0crwdne330146:0) crwdns330148:0crwdne330148:0
:param sda: (crwdns330154:0crwdne330154:0) crwdns330156:0``sda``crwdne330156:0
:param scl: (crwdns330150:0crwdne330150:0) crwdns330152:0``scl``crwdne330152:0

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """crwdns330160:0crwdne330160:0 (crwdns330158:0crwdne330158:0)

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """crwdns330164:0crwdne330164:0 (crwdns330162:0crwdne330162:0)

Example: ``i2c.read(0x50, 64)``

:param addr: (crwdns330166:0crwdne330166:0) crwdns330168:0crwdne330168:0
:param n: (crwdns330170:0crwdne330170:0) crwdns330172:0crwdne330172:0
:param repeat: (crwdns330174:0crwdne330174:0) crwdns330176:0``True``crwdne330176:0
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """crwdns330180:0crwdne330180:0 (crwdns330178:0crwdne330178:0)

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: (crwdns330182:0crwdne330182:0) crwdns330184:0crwdne330184:0
:param buf: (crwdns330186:0crwdne330186:0) crwdns330188:0crwdne330188:0
:param repeat: (crwdns330190:0crwdne330190:0) crwdns330192:0``True``crwdne330192:0"""
    ...