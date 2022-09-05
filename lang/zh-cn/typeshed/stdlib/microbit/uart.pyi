"""使用串行接口与设备通信。 (uart)"""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""奇校验 (odd)"""
EVEN: int
"""
偶校验 (even)"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """初始化串行通信。 (init)

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: (baudrate) 通信速度。
:param bits: (bits) 正在传输的字节大小。micro:bit 仅支持 8 字节。
:param parity: (parity) 如何检查奇偶性，``None``、``uart.ODD`` 或 ``uart.EVEN``。
:param stop: (stop) 停止位的数量，对于 micro:bit，必须为 1。
:param tx: (tx) 传输引脚。
:param rx: (rx) 接收引脚。

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """检查是否有任何数据正在等待。 (any)

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """读取字节。 (read)

Example: ``uart.read()``

:param nbytes: (nbytes) 如果指定了 ``nbytes``，则最多读取那么多字节，否则读取尽可能多的字节
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """读取字节到 ``buf``。 (readinto)

Example: ``uart.readinto(input_buffer)``

:param buf: (buf) 要写入的缓存。
:param nbytes: (nbytes) 如果指定了 ``nbytes``，则最多读取那么多字节，否则读取 ``len(buf)`` 个字节。
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """读取一行，以换行符结尾。 (readline)

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """将缓冲区写入总线。 (write)

Example: ``uart.write('hello world')``

:param buf: (buf) 一个字节对象或一个字符串。
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...