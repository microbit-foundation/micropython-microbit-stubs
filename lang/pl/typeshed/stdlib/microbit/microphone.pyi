"""Odpowiedz na dźwięk przy użyciu wbudowanego mikrofonu (tylko V2)."""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Pobierz ostatnie nagrane zdarzenie dźwiękowe

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Sprawdź, czy dźwięk był słyszany co najmniej raz od ostatniego połączenia.

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: Zdarzenie do sprawdzenia, takie jak ``SoundEvent.LOUD`` lub ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Sprawdź najnowsze wykryte zdarzenie dźwiękowe.

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: Zdarzenie do sprawdzenia, takie jak ``SoundEvent.LOUD`` lub ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Pobierz historię zdarzeń dźwiękowych jako krotkę.

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Ustaw próg dla zdarzenia dźwiękowego.

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: Zdarzenie dźwiękowe, takie jak ``SoundEvent.LOUD`` lub ``SoundEvent.QUIET``.
:param value: Poziom progu w zakresie 0-255."""
    ...

def sound_level() -> int:
    """Uzyskaj poziom ciśnienia akustycznego.

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...