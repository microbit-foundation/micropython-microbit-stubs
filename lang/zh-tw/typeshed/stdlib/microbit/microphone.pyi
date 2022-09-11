"""使用內建麥克風回應聲音 (僅限 V2)。"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """獲取最後錄製的聲音事件

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """檢查自上次通話後是否至少聽到一次聲音。

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: 要檢查的事件，例如 ``SoundEvent.LOUD`` 或 ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """檢查檢測到的最新聲音事件。

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: 要檢查的事件，例如 ``SoundEvent.LOUD`` 或 ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """以元組的形式獲取聲音事件歷史。

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """設定聲音事件的閾值。

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: 聲音事件，例如 ``SoundEvent.LOUD`` 或 ``SoundEvent.QUIET``。
:param value: 0-255 範圍內的閾值級別。"""
    ...

def sound_level() -> int:
    """獲取聲壓等級。

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...