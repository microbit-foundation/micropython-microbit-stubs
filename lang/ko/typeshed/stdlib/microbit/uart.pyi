"""직렬 인터페이스를 사용해 장치와 통신합니다."""
from _typeshed import WriteableBuffer
from ..microbit import MicroBitDigitalPin
from typing import Optional, Union
ODD: int
"""홀수 패리티"""
EVEN: int
"""짝수 패리티"""

def init(baudrate: int=9600, bits: int=8, parity: Optional[int]=None, stop: int=1, tx: Optional[MicroBitDigitalPin]=None, rx: Optional[MicroBitDigitalPin]=None) -> None:
    """직렬 통신을 시작합니다. (string)

Example: ``uart.init(115200, tx=pin0, rx=pin1)``

:param baudrate: 통신 속도입니다.
:param bits: 전송되는 바이트의 크기입니다. micro:bit는 8바이트만 지원합니다.
:param parity: (패리티) 패리티가 체크되는 방식으로 ``None``, ``uart.ODD`` 또는 ``uart.EVEN``을 사용합니다.
:param stop: 스톱 비트의 번호입니다. micro:bit는 1이어야 합니다.
:param tx: 전송하는 핀입니다.
:param rx: 수신하는 핀입니다.

Initializing the UART on external pins will cause the Python console on
USB to become unaccessible, as it uses the same hardware. To bring the
console back you must reinitialize the UART without passing anything for
``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
that calling ``uart.init(115200)`` is enough to restore the Python console.

For more details see `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/uart.html>`_."""
    ...

def any() -> bool:
    """대기 중인 데이터가 있는지 확인합니다.

Example: ``uart.any()``

:return: ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: Optional[int]=None) -> Optional[bytes]:
    """바이트를 읽습니다.

Example: ``uart.read()``

:param nbytes: ``nbytes``가 특정되어 있다면 해당 바이트 수만큼 읽습니다. 특정되지 않은 경우 최대한 많은 바이트를 읽습니다.
:return: A bytes object or ``None`` on timeout"""
    ...

def readinto(buf: WriteableBuffer, nbytes: Optional[int]=None) -> Optional[int]:
    """``buf``로 바이트를 읽습니다.

Example: ``uart.readinto(input_buffer)``

:param buf: 바이트를 기록할 버퍼입니다.
:param nbytes: ``nbytes``가 특정되어 있다면 해당 바이트 수만큼 읽습니다. 특정되지 않은 경우 ``len(buf)``바이트를 읽습니다.
:return: number of bytes read and stored into ``buf`` or ``None`` on timeout."""
    ...

def readline() -> Optional[bytes]:
    """새로운 줄 문자로 끝나는 줄을 읽습니다.

Example: ``uart.readline()``

:return: The line read or ``None`` on timeout. The newline character is included in the returned bytes."""
    ...

def write(buf: Union[bytes, str]) -> Optional[int]:
    """버스에 버퍼를 기록합니다.

Example: ``uart.write('hello world')``

:param buf: 바이트 오브젝트 또는 문자열입니다.
:return: The number of bytes written, or ``None`` on timeout.

Examples::

    uart.write('hello world')
    uart.write(b'hello world')
    uart.write(bytes([1, 2, 3]))"""
    ...