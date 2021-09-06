"""This object lets you access the built-in microphone available on the
micro:bit **V2**. It can be used to respond to sound. The microphone input
is located on the front of the board alongside a microphone activity LED,
which is lit when the microphone is in use.
"""

from typing import Tuple
from . import SoundEvent


def current_event() -> SoundEvent:
    """
    * **return**: the name of the last recorded sound event,
    ``SoundEvent('loud')`` or ``SoundEvent('quiet')``.
    """
    ...

def was_event(event: SoundEvent) -> bool:
    """
    * **event**: a sound event,  such as ``SoundEvent.LOUD`` or
      ``SoundEvent.QUIET``.
    * **return**: ``true`` if sound was heard at least once since the last
      call, otherwise ``false``. ``was_event()`` also clears the sound
      event history before returning.
    """
    ...

def is_event(event):
    """
    * **event**: a sound event,  such as ``SoundEvent.LOUD`` or
      ``SoundEvent.QUIET``.
    * **return**: ``true`` if sound event is the most recent since the last
      call, otherwise ``false``. It does not clear the sound event history.
    """
    ...

def get_events() -> Tuple[SoundEvent, ...]:
    """
    * **return**: a tuple of the event history. The most recent is listed last.
      ``get_events()`` also clears the sound event history before returning.
    """
    ...

def set_threshold(event: SoundEvent, value: int) -> None:
    """
    * **event**: a sound event, such as ``SoundEvent.LOUD`` or
      ``SoundEvent.QUIET``.

    * **value**: The threshold level in the range 0-255. For example,
      ``set_threshold(SoundEvent.LOUD, 250)`` will only trigger if the sound is
      very loud (>= 250).
    """
    ...

def sound_level() -> int:
    """
    * **return**: a representation of the sound pressure level in the range 0 to
      255.
    """
    ...
