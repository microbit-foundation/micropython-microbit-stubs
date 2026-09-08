"""使用内置麦克风响应声音（仅限 V2）。 (麦克风)"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """获取最后录制的声音事件

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """检查自上次通话后是否至少听到一次声音。 (曾经是事件)

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: (事件) 要检查的事件，例如 ``SoundEvent.LOUD`` 或 ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """检查最近检测到的声音事件。 (是事件)

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: (事件) 要检查的事件，例如 ``SoundEvent.LOUD`` 或 ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """以元组的形式获取声音事件历史。

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """设置声音事件的阈值。

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: (事件) 声音事件，如``SoundEvent.LOUD``或``SoundEvent.QUIET``。
:param value: 范围为0到255的阈值水平。"""
    ...

def sound_level() -> int:
    """获取声压级。 (音量)

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...