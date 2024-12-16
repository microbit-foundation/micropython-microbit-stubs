"""내장 마이크를 사용해 소리에 반응합니다(V2 전용)."""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """마지막으로 기록된 소리 이벤트

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """마지막 호출 이후로 소리가 들렸는지 확인합니다.

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: ``SoundEvent.LOUD`` 또는 ``SoundEvent.QUIET`` 등을 확인하기 위한 이벤트
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """가장 최근 탐지된 소리 이벤트를 확인합니다.

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: ``SoundEvent.LOUD`` 또는 ``SoundEvent.QUIET`` 등을 확인하기 위한 이벤트
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """소리 이벤트 기록을 튜플로 가져옵니다.

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """소리 이벤트 임계값을 설정합니다.

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: ``SoundEvent.LOUD`` 또는 ``SoundEvent.QUIET`` 등의 소리 이벤트입니다.
:param value: 0~255의 범위로 된 임계값입니다."""
    ...

def sound_level() -> int:
    """음압 레벨을 불러옵니다.

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...