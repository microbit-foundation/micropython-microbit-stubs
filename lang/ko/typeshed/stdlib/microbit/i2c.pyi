"""I²C 버스 프로토콜을 사용해 기기와 통신합니다."""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """주변 장치를 다시 초기화합니다.

Example: ``i2c.init()``

:param freq: 클럭 진동수
:param sda: ``scl`` 핀(기본값 20)
:param scl: ``scl`` 핀(기본값 19)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """버스에서 장치를 스캔합니다.

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """장치에서 바이트 값을 읽습니다.

Example: ``i2c.read(0x50, 64)``

:param addr: 장치의 7비트 주소
:param n: 읽을 바이트 수
:param repeat: ``True``인 경우 스톱 비트가 전송되지 않습니다
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """장치에 바이트를 작성합니다.

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: 장치의 7비트 주소
:param buf: 작성할 바이트가 포함된 버퍼
:param repeat: ``True``인 경우 스톱 비트가 전송되지 않습니다"""
    ...