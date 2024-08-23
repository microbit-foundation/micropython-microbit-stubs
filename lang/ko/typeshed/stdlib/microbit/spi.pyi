"""직렬 주변 장치 인터페이스(SPI) 버스를 사용해 장치와 통신합니다."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """SPI 통신을 시작합니다. (string)

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: 통신 속도입니다.
:param bits: 각 전송의 비트의 너비입니다. 현재 ``bits=8``만 지원되나 향후 변경될 수 있습니다.
:param mode: 클럭 극성과 페이즈의 조합을 결정합니다. 온라인 테이블을 참조하세요 <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: sclk 핀(기본값 13)
:param mosi: mosi 핀(기본값 15)
:param miso: miso 핀(기본값 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """바이트를 읽습니다.

Example: ``spi.read(64)``

:param nbytes: 읽을 바이트의 최대 수입니다.
:param out: The byte value to write (default 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """버스에 바이트를 작성합니다.

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: 데이터를 읽을 버퍼입니다."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """버스에 ``out`` 버퍼를 작성하고 발생하는 ``in_`` 버퍼의 모든 응답을 읽습니다.

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: 응답을 작성할 버퍼입니다.
:param in_: 데이터를 읽을 버퍼입니다."""
    ...