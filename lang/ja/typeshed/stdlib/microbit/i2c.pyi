"""I²C バスプロトコルでデバイスと通信します。 (i2c)"""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """ペリフェラルを再初期化します。 (init)

Example: ``i2c.init()``

:param freq: (freq) クロック周波数
:param sda: (sda) ``sda`` 端子（デフォルト20）
:param scl: (scl) ``scl`` 端子（デフォルト19）

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """デバイスのバスをスキャンします。 (scan)

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """デバイスからバイト列を読み取ります。 (read)

Example: ``i2c.read(0x50, 64)``

:param addr: (addr) デバイスの7ビットアドレス
:param n: (n) 読み取るバイト数
:param repeat: (repeat) ``True`` にすると、ストップビットが送られません。
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """デバイスにバイト列を書き込みます。 (write)

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: (addr) デバイスの7ビットアドレス
:param buf: (buf) 書き込むバイトを含むバッファ
:param repeat: (repeat) ``True`` にすると、ストップビットが送られません。"""
    ...