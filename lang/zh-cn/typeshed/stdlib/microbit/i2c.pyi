"""使用 I²C 总线协议与设备通信。 (i2c)"""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """重新初始化外设。 (init)

Example: ``i2c.init()``

:param freq: (freq) 时钟频率
:param sda: (sda) ``sda`` 引脚(默认20)
:param scl: (scl) ``scl`` 引脚(默认19)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """扫描总线以查找设备。 (scan)

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """从设备读取字节.. (read)

Example: ``i2c.read(0x50, 64)``

:param addr: (addr) 设备的7位地址
:param n: (n) 要读取的字节数
:param repeat: (repeat) 如果为 ``True``，则不发送停止位
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """将字节写入设备。 (write)

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: (addr) 设备的7位地址
:param buf: (buf) 包含要写入的字节的缓冲区
:param repeat: (repeat) 如果为 ``True``，则不发送停止位"""
    ...