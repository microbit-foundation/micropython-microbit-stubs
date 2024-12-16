"""Reagiere auf Ton mithilfe des integrierten Mikrofons (nur V2). (Mikrofon)"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Abrufen des letzten aufgezeichneten Sound-Ereignisses

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Überprüft, ob seit dem letzten Anruf mindestens einmal ein Geräusch gehört wurde.

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: Das Ereignis, auf das geprüft werden soll, z. B. ``SoundEvent.LOUD`` oder ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Überprüft das zuletzt erkannte Sound-Ereignis.

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: Das Ereignis, auf das geprüft werden soll, z. B. ``SoundEvent.LOUD`` oder ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Liefert den Verlauf der Sound-Ereignisse in Form eines Tupels.

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Legt den Schwellenwert für ein Sound-Ereignis fest.

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: Ein Sound-Ereignis, wie ``SoundEvent.LOUD`` oder ``SoundEvent.QUIET``.
:param value: (wert) Der Schwellenwert im Bereich 0-255."""
    ...

def sound_level() -> int:
    """Ermittelt den Schalldruckpegel. (Lautstärke)

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...