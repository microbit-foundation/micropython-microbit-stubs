"""使用周邊設備介面 (SPI) 匯流排與裝置進行通訊。"""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """初始化 SPI 通訊。

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: 通訊速度。
:param bits: 每次傳輸的位元寬度。目前僅支援 ``bits=8``。然而，這種情況在未來可能會改變。
:param mode: 確定時脈極性和相位的組合 - 請見線上表格 <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_。
:param sclk: sclk 引腳 (預設 13)
:param mosi: mosi 引腳 (預設 15)
:param miso: miso 引腳 (預設 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """讀取位元組。

Example: ``spi.read(64)``

:param nbytes: 要讀取的最大位元組數。
:param out: The byte value to write (default 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """將位元組寫入匯流排。

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: 讀取資料的來源緩衝區。"""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """將 ``out`` 緩衝區寫入匯流排，並將任何回應寫入 ``in_`` 緩衝區。

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: 要寫入任何回應的緩衝區。
:param in_: 要從中讀取資料的緩衝區。"""
    ...