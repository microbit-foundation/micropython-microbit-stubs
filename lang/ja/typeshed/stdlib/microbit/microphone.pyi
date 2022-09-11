"""内蔵マイクを使って音に応答します（V2 のみ）。"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """記録されている最新のサウンドイベントを取得します。

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """直前の呼び出しから少なくとも一度はサウンドイベントが発生したかどうかを確認します。

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: ``SoundEvent.LOUD`` や ``SoundEvent.QUIET`` などのイベント
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """直近に検出されたサウンドイベントを確認します。

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: ``SoundEvent.LOUD`` や ``SoundEvent.QUIET`` など、確認するサウンドイベント
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """サウンドイベント履歴をタプルとして取得します。

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """サウンドイベントのしきい値を設定します。

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: ``SoundEvent.LOUD`` や ``SoundEvent.QUIET`` などのサウンドイベント。
:param value: 0～255の範囲で指定するしきい値レベル。"""
    ...

def sound_level() -> int:
    """音圧レベルを取得します。

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...