"""Réagir à du son en utilisant le microphone intégré (V2 uniquement)."""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Récupérer le dernier événement sonore enregistré

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Vérifier si un son a été entendu au moins une fois depuis le dernier appel.

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: L'événement à vérifier, tel que ``SoundEvent.LOUD`` ou ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Vérifier l'événement sonore le plus récent détecté.

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: L'événement à vérifier, tel que ``SoundEvent.LOUD`` ou ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Récupérer l'historique des événements sonores en tant que tuple.

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Définir le seuil pour un événement sonore.

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: Un événement sonore, tel que ``SoundEvent.LOUD`` ou ``SoundEvent.QUIET``.
:param value: Le niveau du seuil dans la plage 0-255."""
    ...

def sound_level() -> int:
    """Obtenir le niveau de pression acoustique.

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...