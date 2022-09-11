"""シリアルインタフェースを使ってデバイスと通信します。"""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""奇数パリティ"""
EVEN: int
"""偶数パリティ"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """シリアル通信を初期化します。

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: 通信速度。
:param bits: 送信するビット幅。micro:bitは8だけをサポートしています。
:param parity: パリティのチェック方法。``None``、``uart.ODD``、``uart.EVEN`` のいずれかを指定できます。
:param stop: ストップビットの数はmicro:bitでは1にする必要があります。
:param tx: 送信端子。
:param rx: 受信端子。

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """受信待ちのデータがあるかを確認します。

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """バイト列を読み取ります。

Example: ``uart.read()``

:param nbytes: ``nbytes`` が指定されていれば、そのバイト数まで読み込みます。指定されていなければ、できるだけ多く読み取ります
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """``buf`` にバイト列を読み取ります。

Example: ``uart.readinto(input_buffer)``

:param buf: 書き込みバッファ。
:param nbytes: ``nbytes`` が指定されていれば、そのバイト数まで読み込みます。指定されていなければ、``len(buf)`` を読み取ります。
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """改行文字で終わる行を読みます。

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """バスにバッファを書き込みます。

Example: ``uart.write('hello world')``

:param buf: バイト列オブジェクトまたは文字列。
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...