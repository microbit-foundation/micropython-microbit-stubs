"""Play sounds using the micro:bit (import ``audio`` for V1 compatibility).
"""

from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Optional, Union

def play(
    source: Union[Iterable[AudioFrame], Sound, SoundEffect],
    wait: bool = True,
    pin: MicroBitDigitalPin = pin0,
    return_pin: Union[MicroBitDigitalPin, None] = None,
) -> None:
    """Play a built-in sound, sound effect or custom audio frames.

    Example: ``audio.play(Sound.GIGGLE)``

    :param source: A built-in ``Sound`` such as ``Sound.GIGGLE``, a ``SoundEffect`` or sample data as an iterable of ``AudioFrame`` objects.
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

class SoundEffect:
    """A sound effect, composed by a set of parameters configured via the constructor or attributes."""

    WAVE_SINE: ClassVar[int]
    """Sine wave option used for the ``wave`` parameter."""

    WAVE_SAWTOOTH: ClassVar[int]
    """Sawtooth wave option used for the ``wave`` parameter."""

    WAVE_TRIANGLE: ClassVar[int]
    """Triangle wave option used for the ``wave`` parameter."""

    WAVE_SQUARE: ClassVar[int]
    """Square wave option used for the ``wave`` parameter."""

    WAVE_NOISE: ClassVar[int]
    """Noise option used for the ``wave`` parameter."""

    SHAPE_LINEAR: ClassVar[int]
    """Linear interpolation option used for the ``shape`` parameter."""

    SHAPE_CURVE: ClassVar[int]
    """Curve interpolation option used for the ``shape`` parameter."""

    SHAPE_LOG: ClassVar[int]
    """Logarithmic interpolation option used for the ``shape`` parameter."""

    FX_NONE: None
    """No effect option used for the ``fx`` parameter."""

    FX_TREMOLO: ClassVar[int]
    """Tremelo effect option used for the ``fx`` parameter."""

    FX_VIBRATO: ClassVar[int]
    """Vibrato effect option used for the ``fx`` parameter."""

    FX_WARBLE: ClassVar[int]
    """Warble effect option used for the ``fx`` parameter."""

    freq_start: int
    """Start frequency in Hertz (Hz)"""

    freq_end: int
    """End frequency in Hertz (Hz)"""

    duration: int
    """Duration of the sound (ms), eg: ``500``"""

    vol_start: int
    """Start volume value, range 0-255, eg: ``120``"""

    vol_end: int
    """End volume value, range 0-255, eg: ``255``"""

    wave: int
    """Type of wave shape, one of these values: ``WAVE_SINE``, ``WAVE_SAWTOOTH``, ``WAVE_TRIANGLE``, ``WAVE_SQUARE``, ``WAVE_NOISE`` (randomly generated noise)."""

    fx: int
    """Effect to add on the sound, one of the following values: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, or ``None``."""

    shape: int
    """The type of the interpolation curve between the start and end frequencies, different wave shapes have different rates of change in frequency. One of the following values: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def __init__(
        self,
        preset: Optional[Union[SoundEffect, str]] = None,
        *,
        freq_start: Optional[int] = None,
        freq_end: Optional[int] = None,
        duration: Optional[int] = None,
        vol_start: Optional[int] = None,
        vol_end: Optional[int] = None,
        wave: Optional[int] = None,
        fx: Optional[int] = None,
        shape: Optional[int] = None
    ):
        """Create a new sound effect.

        All the parameters are optional, with default values listed below, and
        they can all be modified via attributes of the same name. For example, we
        can first create an effect ``my_effect = SoundEffect(duration=1000)``,
        and then change its attributes ``my_effect.duration = 500``.

        :param preset: Optional existing SoundEffect instance to use as a base, its values are cloned in the new instance, and any additional arguments provided overwrite the base values
        :param freq_start: Start frequency in Hertz (Hz), default: ``500``
        :param freq_end: End frequency in Hertz (Hz), default: ``2500``
        :param duration: Duration of the sound (ms), default: ``500``
        :param vol_start: Start volume value, range 0-255, default: ``255``
        :param vol_end: End volume value, range 0-255, default: ``255``
        :param wave: Type of wave shape, one of these values: ``WAVE_SINE``, ``WAVE_SAWTOOTH``, ``WAVE_TRIANGLE``, ``WAVE_SQUARE``, ``WAVE_NOISE`` (randomly generated noise).
        :param fx: Effect to add on the sound, one of the following values: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, or ``None``.
        :param shape: The type of the interpolation curve between the start and end frequencies, different wave shapes have different rates of change in frequency. One of the following values: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``.
        """
