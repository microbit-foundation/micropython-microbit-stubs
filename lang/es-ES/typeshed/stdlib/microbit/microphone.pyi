"""Responde al sonido usando el micrófono integrado (solo V2). (micrófono)"""
from typing import Optional, Tuple
from ..microbit import SoundEvent

def current_event() -> Optional[SoundEvent]:
    """Obtiene el último evento de sonido grabado (evento actual)

Example: ``microphone.current_event()``

:return: The event, ``SoundEvent('loud')`` or ``SoundEvent('quiet')``."""
    ...

def was_event(event: SoundEvent) -> bool:
    """Comprueba si se ha escuchado un sonido al menos una vez desde la última llamada. (evento anterior)

Example: ``microphone.was_event(SoundEvent.LOUD)``

This call clears the sound history before returning.

:param event: (evento) El evento a comprobar, como ``SoundEvent.LOUD`` o ``SoundEvent.QUIET``
:return: ``True`` if sound was heard at least once since the last call, otherwise ``False``."""
    ...

def is_event(event: SoundEvent) -> bool:
    """Comprueba el evento de sonido más reciente detectado. (evento reciente)

Example: ``microphone.is_event(SoundEvent.LOUD)``

This call does not clear the sound event history.

:param event: (evento) El evento a comprobar, como ``SoundEvent.LOUD`` o ``SoundEvent.QUIET``
:return: ``True`` if sound was the most recent heard, ``False`` otherwise."""
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """Obtiene el historial de eventos de sonido como una tupla. (obtener eventos)

Example: ``microphone.get_events()``

This call clears the sound history before returning.

:return: A tuple of the event history with the most recent event last."""
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """Establece el umbral para un evento de sonido. (configurar límite)

Example: ``microphone.set_threshold(SoundEvent.LOUD, 250)``

A high threshold means the event will only trigger if the sound is very loud (>= 250 in the example).

:param event: (evento) Un evento de sonido, como ``SoundEvent.LOUD`` o ``SoundEvent.QUIET``.
:param value: (valor) El nivel de umbral en el rango 0 - 255."""
    ...

def sound_level() -> int:
    """Obtiene el nivel de presión sonora. (nivel de sonido)

Example: ``microphone.sound_level()``

:return: A representation of the sound pressure level in the range 0 to 255."""
    ...