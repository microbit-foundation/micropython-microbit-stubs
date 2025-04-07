"""通过串行外设接口（SPI）总线与设备通信。 (串行外围接口（SPI）)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """初始化串行外设接口（SPI ）通信。

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: (波特率) 通信速度。
:param bits: (位) 每次传输的宽度（单位：bit）。目前只支持 ``bits=8``，但是未来可能支持其他宽度。
:param mode: (模式) 决定时钟极性和相位的组合——“参见在线表格<https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>”。
:param sclk: (SCLK) sclk 引脚(默认 13)
:param mosi: (MOSI) mosi 引脚(默认 15)
:param miso: (MISO) MISO引脚（默认值14）"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """读取字节数。 (读取)

Example: ``spi.read(64)``

:param nbytes: (字节数) 要读取的最大字节数。
:param out: (写出) 要写入的字节值（默认为0）。
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """将字节写入总线。 (写入)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (缓冲区) 读取数据的缓冲区。"""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """将 ``out`` 缓冲区写入总线，并将任何响应读入 ``in_`` 缓冲区。 (写并读入)

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: (写出) 写入任何响应的缓冲区。
:param in_: (读入) 读取数据的缓冲区。"""
    ...