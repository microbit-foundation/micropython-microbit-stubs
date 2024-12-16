"""내장 라디오를 사용해 micro:bit끼리 통신합니다."""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""초당 1 MBit의 처리율을 지정하는 데 사용하는 상수"""
RATE_2MBIT: int
"""초당 2 MBit의 처리율을 지정하는 데 사용하는 상수."""

def on() -> None:
    """라디오를 켭니다.

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """라디오를 꺼 전력과 메모리를 절약합니다.

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """라디오를 설정합니다.

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (기본값=32) 라디오를 통해 전송되는 메시지의 최대 길이를 바이트로 정의합니다.
최대 251바이트까지 정의할 수 있습니다(S0, LENGTH 및 S1 프리앰블의 경우 254 - 3바이트).
:param queue: (기본값=3) 수신 메시지 대기열에 보관할 수 있는 메시지의 수를 특정합니다. 만약 수신 메시지의 대기열 공간이 부족하다면 수신 메시지는 드롭됩니다.
:param channel: (기본값=7) 임의의 "채널"을 라디오 채널로 설정하는 0부터 83까지의 정수(경계값 포함)입니다. 메시지는 이 채널로 전송되며 이 채널을 통해 받은 메시지만 수신 메시지 대기열에 등록됩니다. 2400MHz 기준으로 각 단계는 1MHz 대역입니다.
:param power: (기본값=6) 0부터 7의 정수값(경계값 포함)으로 메시지를 송출할 때의 신호 강도를 표현합니다.
값이 높을 수록 신호는 강해지지만 장치의 전력을 더 소모합니다. 각 숫자는 다음 dBm(데시벨 밀리와트)값 리스트의 위치로 변환됩니다: -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (기본=0x75626974) 32비트로 표현되는 임의의 이름입니다. 하드웨어 레벨에서 수신 패킷을 필터링하는 데 사용되며 설정한 주소와 일치하는 패킷만 유지합니다. 다른 micro:bit 관련 플랫폼이 사용하는 기본값은 여기에서도 사용됩니다.
:param group: 메시지를 필터링할 때 ``address``와 함께 사용되는 8비트 값(0~255)입니다. 개념상 "address(주소)"는 집/사무실 주소, "group(그룹)"은 해당 주소에서 메시지를 보내고자 하는 인물입니다.
:param data_rate: (default=``radio.RATE_1MBIT``) 데이터 처리율의 속도를 지정합니다. ``radio`` 모듈의 다음 상수 중 하나가 될 수 있습니다: ``RATE_250KBIT``, ``RATE_1MBIT`` 또는 ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """설정을 기본값으로 초기화합니다.

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """바이트가 포함된 메시지를 전송합니다.

Example: ``radio.send_bytes(b'hello')``

:param message: 전송할 바이트입니다."""
    ...

def receive_bytes() -> Optional[bytes]:
    """메시지 대기열에 있는 다음 수신 메시지를 받습니다.

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """메시지 대기열에 있는 다음 수신 메시지를 버퍼에 복사합니다.

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: 목표 버퍼입니다. 메시지가 버퍼보다 크면 메시지가 잘립니다.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """메시지 문자열을 전송합니다.

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: 전송할 문자열입니다."""
    ...

def receive() -> Optional[str]:
    """``receive_bytes``와 정확히 동일한 작업을 하지만 모든 전송 항목을 반환한다는 차이가 있습니다.

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """메시지 대기열에 있는 다음 수신 메시지의 정보를 세 종류의 값이 포함된 튜플로 반환합니다.

Example: ``radio.receive_full()``

If there are no pending messages then ``None`` is returned.

The three values in the tuple represent:

- the next incoming message on the message queue as bytes.
- the RSSI (signal strength): a value between 0 (strongest) and -255 (weakest) as measured in dBm.
- a microsecond timestamp: the value returned by ``time.ticks_us()`` when the message was received.

For example::

    details = radio.receive_full()
    if details:
        msg, rssi, timestamp = details

This function is useful for providing information needed for triangulation
and/or trilateration with other micro:bit devices.

:return: ``None`` if there is no message, otherwise a tuple of length three with the bytes, strength and timestamp values."""
    ...