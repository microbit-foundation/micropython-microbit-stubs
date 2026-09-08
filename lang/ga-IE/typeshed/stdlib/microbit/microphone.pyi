"""Freagair fuaim ag baint úsáide as an micreafón tógtha (V2 amháin). (micreafón)"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Faigh an teagmhas fuaime taifeadta is déanaí (imeacht reatha)

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Seiceáil ar chualathas fuaim uair amháin ar a laghad ón nglao deireanach. (ba imeacht é)

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: (imeacht) An ócáid le seiceáil, mar shampla ``SoundEvent.LOUD`` nó ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Seiceáil an teagmhas fuaime is déanaí a braitheadh. (imeacht)

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: (imeacht) An ócáid le seiceáil, mar shampla ``SoundEvent.LOUD`` nó ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Faigh stair na hócáide fuaime mar thuple. (faigh imeachtaí)

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Socraigh an tairseach le haghaidh teagmhas fuaime. (tairseach shocraithe)

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: (imeacht) Imeacht fuaime, mar shampla ``SoundEvent.LOUD`` nó ``SoundEvent.QUIET``.
:param value: (luach) An leibhéal tairsí sa raon 0-255."""
    ...

def sound_level() -> int:
    """Faigh an leibhéal brú fuaime. (leibhéal fuaime)

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...