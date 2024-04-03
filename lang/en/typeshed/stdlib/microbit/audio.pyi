"""Play sounds using the micro:bit (import ``audio`` for V1 compatibility).
"""

from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(
    source: Union[AudioFrame, Iterable[AudioFrame], Sound, SoundEffect],
    wait: bool = True,
    pin: MicroBitDigitalPin = pin0,
    return_pin: Union[MicroBitDigitalPin, None] = None,
) -> None:
    """Play a built-in sound, sound effect or audio samples using ``AudioFrame``.

    Example: ``audio.play(Sound.GIGGLE)``

    :param source: A built-in ``Sound`` such as ``Sound.GIGGLE``, a ``SoundEffect`` or sample data as an ``AudioFrame`` object or an iterable of ``AudioFrame`` objects.
    :param wait: If ``wait`` is ``True``, this function will block until the sound is complete.
    :param pin: An optional argument to specify the output pin can be used to  override the default of ``pin0``. If we do not want any sound to play we can use ``pin=None``.
    :param return_pin: Specifies a differential edge connector pin to connect to an external speaker instead of ground. This is ignored for the **V2** revision.
    """

def is_playing() -> bool:
    """Check whether a sound is playing.

    Example: ``audio.is_playing()``

    :return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def sound_level() -> int:
    """Returns the average intensity of the sound played.

    Example: ``audio.sound_level()``

    :return: A number between 0 and 254, being the average intensity of the sound played from the most recent chunk of data."""
    ...

def stop() -> None:
    """Stop all audio playback.

    Example: ``audio.stop()``
    """
    ...

class SoundEffect:
    """A sound effect, composed by a set of parameters configured via the constructor or attributes."""

    WAVEFORM_SINE: ClassVar[int]
    """Sine wave option used for the ``waveform`` parameter."""

    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Sawtooth wave option used for the ``waveform`` parameter."""

    WAVEFORM_TRIANGLE: ClassVar[int]
    """Triangle wave option used for the ``waveform`` parameter."""

    WAVEFORM_SQUARE: ClassVar[int]
    """Square wave option used for the ``waveform`` parameter."""

    WAVEFORM_NOISE: ClassVar[int]
    """Noise option used for the ``waveform`` parameter."""

    SHAPE_LINEAR: ClassVar[int]
    """Linear interpolation option used for the ``shape`` parameter."""

    SHAPE_CURVE: ClassVar[int]
    """Curve interpolation option used for the ``shape`` parameter."""

    SHAPE_LOG: ClassVar[int]
    """Logarithmic interpolation option used for the ``shape`` parameter."""

    FX_NONE: ClassVar[int]
    """No effect option used for the ``fx`` parameter."""

    FX_TREMOLO: ClassVar[int]
    """Tremolo effect option used for the ``fx`` parameter."""

    FX_VIBRATO: ClassVar[int]
    """Vibrato effect option used for the ``fx`` parameter."""

    FX_WARBLE: ClassVar[int]
    """Warble effect option used for the ``fx`` parameter."""

    freq_start: int
    """Start frequency in Hertz (Hz), a number between ``0`` and ``9999``"""

    freq_end: int
    """End frequency in Hertz (Hz), a number between ``0`` and ``9999``"""

    duration: int
    """Duration of the sound in milliseconds, a number between ``0`` and ``9999``"""

    vol_start: int
    """Start volume value, a number between ``0`` and ``255``"""

    vol_end: int
    """End volume value, a number between ``0`` and ``255``"""

    waveform: int
    """Type of waveform shape, one of these values: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (randomly generated noise)"""

    fx: int
    """Effect to add on the sound, one of the following values: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, or ``FX_NONE``"""

    shape: int
    """The type of the interpolation curve between the start and end frequencies, different wave shapes have different rates of change in frequency. One of the following values: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``"""

    def __init__(
        self,
        freq_start: int = 500,
        freq_end: int = 2500,
        duration: int = 500,
        vol_start: int = 255,
        vol_end: int = 0,
        waveform: int = WAVEFORM_SQUARE,
        fx: int = FX_NONE,
        shape: int = SHAPE_LOG,
    ):
        """Create a new sound effect.

        Example: ``my_effect = SoundEffect(duration=1000)``

        All the parameters are optional, with default values as shown above, and
        they can all be modified via attributes of the same name. For example, we
        can first create an effect ``my_effect = SoundEffect(duration=1000)``,
        and then change its attributes ``my_effect.duration = 500``.

        :param freq_start: Start frequency in Hertz (Hz), a number between ``0`` and ``9999``.
        :param freq_end: End frequency in Hertz (Hz), a number between ``0`` and ``9999``.
        :param duration: Duration of the sound in milliseconds, a number between ``0`` and ``9999``.
        :param vol_start: Start volume value, a number between ``0`` and ``255``.
        :param vol_end: End volume value, a number between ``0`` and ``255``.
        :param waveform: Type of waveform shape, one of these values: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (randomly generated noise).
        :param fx: Effect to add on the sound, one of the following values: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, or ``FX_NONE``.
        :param shape: The type of the interpolation curve between the start and end frequencies, different wave shapes have different rates of change in frequency. One of the following values: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``.
        """
    def copy(self) -> SoundEffect:
        """Create a copy of this ``SoundEffect``.

        Example: ``sound_2 = sound_1.copy()``

        :return: A copy of the SoundEffect.
        """

class AudioFrame:
    """An ``AudioFrame`` object is a list of samples, each of which is an unsigned byte
    (whole number between 0 and 255).

    The number of samples in an AudioFrame will depend on the
    ``rate`` (number of samples per second) and ``duration`` parameters.
    The total number of samples will always be a round up multiple of 32.

    On micro:bit V1 the constructor does not take any arguments,
    and an AudioFrame instance is always 32 bytes.

    For example, playing 32 samples at 7812 Hz takes just over 4 milliseconds
    (1/7812.5 * 32 = 0.004096 = 4096 microseconds).

    Example::

        frame = AudioFrame()
        for i in range(len(frame)):
            frame[i] = 252 - i * 8
    """

    def __init__(
        self,
        duration: int = -1,
        rate: int = 7812
    ):
        """Create a new ``AudioFrame``.

        Example: ``my_recording = AudioFrame(duration=5000)``

        :param duration: Indicates how many milliseconds of audio this instance can store (V2 only).
        :param rate: The sampling rate at which data will be stored via the microphone, or played via the ``audio.play()`` function (V2 only).
        """

    def set_rate(self, sample_rate: int) -> None:
        """Configure the sampling rate associated with the data in the
        ``AudioFrame`` instance (V2 only).

        Example: ``my_frame.set_rate(7812)``

        For recording from the microphone, increasing the sampling rate
        increases the sound quality, but reduces the length of audio it
        can store.

        During playback, increasing the sampling rate speeds up the sound
        and decreasing it slows it down.
        """

    def get_rate(self) -> int:
        """Get the sampling rate associated with the data in the
        ``AudioFrame`` instance (V2 only).

        Example: ``current_rate = my_frame.get_rate()``

         :return: The configured sampling rate for this ``AudioFrame`` instance.
        """

    def copyfrom(self, other: AudioFrame) -> None:
        """Overwrite the data in this ``AudioFrame`` with the data from another ``AudioFrame`` instance.

        Example: ``my_frame.copyfrom(source_frame)``

        :param other: ``AudioFrame`` instance from which to copy the data.
        """
    def __len__(self) -> int: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __getitem__(self, key: int) -> int: ...
    def __add__(self, v: AudioFrame) -> AudioFrame: ...
    def __iadd__(self, v: AudioFrame) -> AudioFrame: ...
    def __sub__(self, v: AudioFrame) -> AudioFrame: ...
    def __isub__(self, v: AudioFrame) -> AudioFrame: ...
    def __mul__(self, v: float) -> AudioFrame: ...
    def __imul__(self, v: float) -> AudioFrame: ...
