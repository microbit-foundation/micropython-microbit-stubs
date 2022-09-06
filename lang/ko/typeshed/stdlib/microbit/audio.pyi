"""micro:bit을 활용해 소리 재생(V1 호환성의 경우 ``audio`` 입력). (audio)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """내장된 소리 또는 커스텀 오디오 프레임을 재생합니다. (play)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (source) ``Sound.GIGGLE`` 등의 내장된 ``Sound`` 또는 ``AudioFrame`` 오브젝트의 연속형 자료 샘플 데이터.
:param wait: (wait) ``wait``이 ``True``인 경우 사운드 재생이 완료될 때까지 이 기능(함수)이 차단됩니다.
:param pin: (핀) ``pin0``의 기본값을 무시하고 사용할 출력 핀을 특정하는 선택형 인자입니다. 사운드를 재생하고 싶지 않다면 ``pin=None``을 사용할 수 있습니다.
:param return_pin: (return pin) 접지 대신 외부 스피커에 연결할 차동 엣지 커넥터(differential edge connector) 핀을 특정합니다. **V2** 리비전에서는 무시됩니다."""

def is_playing() -> bool:
    """소리가 재생 중인지 체크합니다. (is playing)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """모든 오디오 플레이백을 중지합니다. (stop)

Example: ``audio.stop()``"""
    ...

class AudioFrame:
    """``AudioFrame`` 오브젝트는 부호가 없는 바이트(unsigned byte) 샘플 32개의 목록입니다. (whole number between 0 and 255). (audioframe)

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...