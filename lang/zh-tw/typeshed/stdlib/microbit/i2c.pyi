"""使用 I²C 匯流排通訊協定與裝置通訊。"""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """重新初始化周邊設備。

Example: ``i2c.init()``

:param freq: (頻率) 時脈頻率
:param sda: ``sda`` 引腳 (預設 20)
:param scl: ``scl`` 引腳 (預設 19)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """掃描匯流排以尋找裝置。

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """從裝置讀取位元組。

Example: ``i2c.read(0x50, 64)``

:param addr: 裝置的 7 位元地址
:param n: 要讀取的位元組數
:param repeat: 如果 ``True``，則不會傳送停止位元
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """將位元組寫入裝置。

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: 裝置的 7 位元位址
:param buf: 包含要寫入位元組的緩衝區
:param repeat: 如果 ``True``，則不會傳送停止位元"""
    ...