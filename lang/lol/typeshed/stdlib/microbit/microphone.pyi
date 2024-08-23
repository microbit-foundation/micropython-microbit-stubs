"""crwdns330196:0crwdne330196:0 (crwdns330194:0crwdne330194:0)"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """crwdns330200:0crwdne330200:0 (crwdns330198:0crwdne330198:0)

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """crwdns330204:0crwdne330204:0 (crwdns330202:0crwdne330202:0)

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: (crwdns330206:0crwdne330206:0) crwdns330208:0``SoundEvent.LOUD``crwdnd330208:0``SoundEvent.QUIET``crwdne330208:0
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """crwdns330212:0crwdne330212:0 (crwdns330210:0crwdne330210:0)

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: (crwdns330214:0crwdne330214:0) crwdns330216:0``SoundEvent.LOUD``crwdnd330216:0``SoundEvent.QUIET``crwdne330216:0
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """crwdns330220:0crwdne330220:0 (crwdns330218:0crwdne330218:0)

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """crwdns330224:0crwdne330224:0 (crwdns330222:0crwdne330222:0)

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: (crwdns330226:0crwdne330226:0) crwdns330228:0``SoundEvent.LOUD``crwdnd330228:0``SoundEvent.QUIET``crwdne330228:0
:param value: (crwdns330230:0crwdne330230:0) crwdns330232:0crwdne330232:0"""
    ...

def sound_level() -> int:
    """crwdns330236:0crwdne330236:0 (crwdns330234:0crwdne330234:0)

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...