"""Responda ao som usando o microfone integrado (apenas V2). (microfone)"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Obter o último evento de som gravado (Evento atual)

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Verifique se um som foi ouvido pelo menos uma vez desde a última chamada. (Foi evento)

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: (evento) O evento para verificar, como ``SoundEvent.LOUD`` ou ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Verifique o evento sonoro mais recente detectado (É evento)

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: (evento) O evento para verificar, como ``SoundEvent.LOUD`` ou ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Obtenha o histórico de evento sonoro como uma tupla. (Obter eventos)

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Defina o limiar para um evento de som. (Definir limiar)

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: (evento) Um evento de som, como ``SoundEvent.LOUD`` ou ``SoundEvent.QUIET``.
:param value: (Valor) O nível do limiar no intervalo de 0–255."""
    ...

def sound_level() -> int:
    """Obtenha o nível de pressão sonora. (Nível de som)

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...