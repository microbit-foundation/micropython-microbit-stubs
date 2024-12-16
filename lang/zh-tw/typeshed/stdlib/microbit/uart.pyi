"""使用序列介面與裝置通訊。"""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""奇數同位檢查"""
EVEN: int
"""偶數同位檢查"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """初始化序列通訊。

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: 通訊速度。
:param bits: 正在傳輸的位元組大小，micro:bit 只支援 8。
:param parity: 如何檢查奇偶性，``None``、``uart.ODD`` 或 ``uart.EVEN``。
:param stop: 停止位元的數量，micro:bit 必須為 1。
:param tx: 傳輸引腳。
:param rx: 正在接收引腳。

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """檢查是否有任何資料正在等待。

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """讀取位元組。

Example: ``uart.read()``

:param nbytes: 如果指定了 ``nbytes``，則最多讀取那麼多位元組，否則讀取盡可能多的位元組
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """將位元組讀入 ``buf``。

Example: ``uart.readinto(input_buffer)``

:param buf: 要寫入的緩衝區。
:param nbytes: 如果指定了 ``nbytes``，則最多讀取那麼多位元組，否則讀取 ``len(buf)`` 個位元組。
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """讀取一行，以新行字元結尾。

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """將緩衝區寫入匯流排。

Example: ``uart.write('hello world')``

:param buf: 一個位元組物件或一個字串。
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...