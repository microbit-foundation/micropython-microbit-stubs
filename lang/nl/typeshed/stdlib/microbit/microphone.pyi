"""Reageer op geluid met de ingebouwde microfoon (V2 alleen). (microfoon)"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Krijg de laatst opgenomen geluidsgebeurtenis (huidige gebeurtenis)

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Controleer of een geluid tenminste één keer is gehoord sinds het laatste gesprek.

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: (gebeurtenis) Het te controleren evenement, zoals ``SoundEvent.LOUD`` of ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Controleer de meest recente geluidsgebeurtenis gedetecteerd.

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: (gebeurtenis) Het te controleren evenement, zoals ``SoundEvent.LOUD`` of ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Krijg de geluidsgeschiedenis als tuple.

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Stel de drempel in voor een geluidsgebeurtenis. (stel drempelwaarde in)

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: (gebeurtenis) Een geluidsgebeurtenis, zoals ``SoundEvent.LOUD`` of ``SoundEvent.QUIET``.
:param value: (waarde) Het drempelniveau in het bereik 0-255."""
    ...

def sound_level() -> int:
    """Krijg het Geluidsdrukniveau. (geluidsniveau)

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...