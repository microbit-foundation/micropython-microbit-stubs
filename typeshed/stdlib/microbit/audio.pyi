"""Play sounds using the micro:bit (import ``audio`` for V1 compatibility).
"""

from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import Iterable, Union

def play(
    source: Union[Iterable[AudioFrame], Sound],
    wait: bool = True,
    pin: MicroBitDigitalPin = pin0,
    return_pin: Union[MicroBitDigitalPin, None] = None,
) -> None:
    """Play a built-in sound or custom audio frames.``.

    Example: ``audio.play(Sound.GIGGLE)``

    :param source: A built-in ``Sound`` such as ``Sound.GIGGLE`` or sample data as an iterable of ``AudioFrame`` objects.
    :param wait: If ``wait`` is ``True``, this function will block until the sound is complete.
    :param pin: An optional argument to specify the output pin can be used to  override the default of ``pin0``. If we do not want any sound to play we can use ``pin=None``.
    :param return_pin: Specifies a differential edge connector pin to connect to an external speaker instead of ground. This is ignored for the **V2** revision.
    """

def is_playing() -> bool:
    """Check whether a sound is playing.

    Example: ``audio.is_playing()``

    :return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Stop all audio playback.
    
    Example: ``audio.stop()``
    """
    ...

class AudioFrame:
    """An ``AudioFrame`` object is a list of 32 samples each of which is a unsigned byte
    (whole number between 0 and 255).

    It takes just over 4 ms to play a single frame.

    Example::

        frame = AudioFrame()
        for i in range(len(frame)):
          frame[i] = 252 - i * 8
    """

    def __len__(self) -> int: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __getitem__(self, key: int) -> int: ...
