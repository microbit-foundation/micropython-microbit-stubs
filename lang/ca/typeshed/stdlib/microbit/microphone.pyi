"""Respon al so fent servir el micròfon integrat (només V2). (micròfon)"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Obté l'últim esdeveniment de sonor gravat (esdeveniment actual)

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Comprova si s'ha sentit un so almenys una vegada des de l'última crida. (va ser un esdeveniment)

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: (esdeveniment) L'esdeveniment per comprovar, com ara ``SoundEvent.LOUD`` o ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Comprova l'esdeveniment sonor més recent detectat. (és un esdeveniment)

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: (esdeveniment) L'esdeveniment per comprovar, com ara ``SoundEvent.LOUD`` o ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Obté l'historial d'esdeveniments sonors com una tupla. (obté esdeveniments)

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Assigna el llinar per un esdeveniment sonor (estableix llindar)

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: (esdeveniment) Un esdeveniment sonor, com ara ``SoundEvent.LOUD`` o ``SoundEvent.QUIET``.
:param value: (valor) El llindar en l'interval 0-255."""
    ...

def sound_level() -> int:
    """Obté el nivell de pressió sonora. (nivell de so)

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...