"""This module allows you to play your own sounds. If you are using a micro:bit
**V2**, ``audio`` is also part of the ``microbit`` module.

By default sound output will be via the edge connector on pin 0 and the
:doc:`built-in speaker <speaker>` **V2**. You can connect wired headphones or
a speaker to pin 0 and GND on the edge connector to hear the sounds.
"""

from .microbit import MicroBitDigitalPin, Sound, pin0
from typing import Iterable, Union

def play(
    source: Union[Iterable[AudioFrame], Sound],
    wait: bool = True,
    pin: MicroBitDigitalPin = pin0,
    return_pin: Union[MicroBitDigitalPin, None] = None,
) -> None:
    """Play the source to completion.

    * **source**: ``Sound`` - The ``microbit`` module contains a list of
      built-in sounds that your can pass to ``audio.play()``.

    * **source**: ``AudioFrame`` - The source agrument can also be an iterable
      of ``AudioFrame`` elements as described below.

    * **wait**: If ``wait`` is ``True``, this function will block until the
      source is exhausted.

    * **pin**: An optional argument to specify the output pin can be used to
    override the default of ``pin0``. If we do not want any sound to play
    we can use ``pin=None``.

    * **return_pin**: specifies a differential edge connector pin to connect
      to an external speaker instead of ground. This is ignored for the **V2**
      revision.
    """

def is_playing() -> bool:
    """Return ``True`` if audio is playing, otherwise return ``False``."""
    ...

def stop() -> None:
    """Stops all audio playback."""
    ...

class AudioFrame:
    """An ``AudioFrame`` object is a list of 32 samples each of which is a signed byte
    (whole number between -128 and 127).

    It takes just over 4 ms to play a single frame.
    """

    def __len__(self) -> int: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __getitem__(self, key: int) -> int: ...
