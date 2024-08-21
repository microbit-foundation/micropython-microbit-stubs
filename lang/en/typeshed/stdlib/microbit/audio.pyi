"""Play sounds using the micro:bit (import ``audio`` for V1 compatibility).
"""

from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Optional, Union

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
    """Returns the sound pressure level produced by audio currently being played.

    Example: ``audio.sound_level()``

    :return: A representation of the output sound pressure level in the range 0 to 255."""
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


class AudioRecording:
    """The ``AudioRecording`` object contains audio data and the sampling rate
    associated to it (V2 only).

    The size of the internal buffer will depend on the ``rate``
    (number of samples per second) and ``duration`` parameters.
    The larger these values are, the more memory that will be used.

    When an ``AudioRecording`` is used to record data from the microphone,
    a higher sampling rate produces better sound quality,
    but it also uses more memory.

    During playback, increasing the sampling rate speeds up the sound
    and decreasing the sample rate slows it down.
    
    The data inside an ``AudioRecording`` is not easy to modify, so the
    ``AudioTrack`` class is provided to help access the audio data like a list.
    The method ``AudioRecording.track()`` can be used to create an ``AudioTrack``,
    and its arguments ``start_ms`` and ``end_ms`` can be used to slice portions
    of the data.
    """

    def __init__(
        self,
        duration: int = -1,
        rate: int = 11_000
    ):
        """Create a new ``AudioRecording``.

        Example: ``my_recording = AudioRecording(duration=5000)``

        :param duration: Indicates how many milliseconds of audio this instance can store.
        :param rate: The sampling rate at which data will be stored via the microphone, or played via the ``audio.play()`` function.
        """

    def copy(self) -> None:
        """Create a copy of the ``AudioRecording``.

        Example: ``copy = my_recording.copy()``

        :return: A copy of the ``AudioRecording``.
        """

    def track(self, start_ms: int = 0, end_ms: int = -1) -> AudioTrack:
        """Create an ``AudioTrack`` instance from a portion of the data in this ``AudioRecording`` instance.

        Example: ``first_second = my_recording.track(0, 1000)``

        :param start_ms: (default=0) Where to start of the track in milliseconds.
        :param end_ms: (default=-1) The end of the track in milliseconds. If the default value of ``-1`` is provided it will end the track at the end of the AudioRecording.
        :return: An ``AudioTrack`` backed by the sample data between ``start_ms`` and ``end_ms``.
        """

class AudioTrack:
    """ The ``AudioTrack`` object points to the data provided by the input buffer,
    which can be an ``AudioRecording``, another ``AudioTrack``,
    or a buffer-like object like a ``bytearray`` (V2 only).
    """

    def __init__(
        self,
        buffer: Union[bytearray, AudioRecording, AudioTrack],
        rate: Optional[int] = None
    ):
        """Create a new ``AudioTrack``.

        When the input buffer has an associated rate (e.g. an ``AudioRecording``
        or ``AudioTrack``), the rate is copied. If the buffer object does not have
        a rate, the default value of 11_000 is used.

        Example: ``my_track = AudioTrack(bytearray(4096))``

        An ``AudioTrack`` can be created from an ``AudioRecording``, another
        ``AudioTrack``, or a ``bytearray`` and individual bytes can be accessed and
        modified like elements in a list::

            my_track = AudioTrack(bytearray(100))
            # Create a square wave
            half_length = len(my_track) // 2
            for i in range(half_length):
                my_track[i] = 255
            for i in range(half_length, len(my_track)):
                my_track[i] = 0

        Or smaller AudioTracks can be created using slices, useful to send them
        via radio or serial::

            recording = microphone.record(duration=2000)
            track = AudioTrack(recording)
            packet_size = 32
            for i in range(0, len(track), packet_size):
                radio.send_bytes(track[i:i+packet_size])

        :param buffer: The buffer containing the audio data.
        :param rate: (default=None) The sampling rate at which data will be stored via the microphone, or played via the ``audio.play()`` function. 
        """

    def set_rate(self, sample_rate: int) -> None:
        """Configure the sampling rate associated with the data in the
        ``AudioTrack`` instance.


        Changes to an ``AudioTrack`` rate won't affect the original source rate,
        so multiple instances pointing to the same buffer can have different
        rates and the original buffer rate would stay unmodified.

        Example: ``my_track.set_rate(22_000)``
        """

    def get_rate(self) -> int:
        """Get the sampling rate associated with the data in the
        ``AudioRecording`` instance.

        Example: ``current_rate = my_track.get_rate()``

         :return: The configured sample rate.
        """


    def __len__(self) -> int: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __getitem__(self, key: int) -> int: ...
    def __add__(self, v: AudioTrack) -> AudioTrack: ...
    def __iadd__(self, v: AudioTrack) -> AudioTrack: ...
    def __sub__(self, v: AudioTrack) -> AudioTrack: ...
    def __isub__(self, v: AudioTrack) -> AudioTrack: ...
    def __mul__(self, v: float) -> AudioTrack: ...
    def __imul__(self, v: float) -> AudioTrack: ...


class AudioFrame:
    """An ``AudioFrame`` object is a list of 32 samples each of which is a unsigned byte
    (whole number between 0 and 255).

    It takes just over 4 ms to play a single frame.

    Example::

        frame = AudioFrame()
        for i in range(len(frame)):
            frame[i] = 252 - i * 8
    """

    def copyfrom(self, other: AudioFrame) -> None:
        """Overwrite the data in this ``AudioFrame`` with the data from another ``AudioFrame`` instance.

        Example: ``my_frame.copyfrom(source_frame)``

        :param other: ``AudioFrame`` instance from which to copy the data.
        """
    def __len__(self) -> int: ...
    def __setitem__(self, key: int, value: int) -> None: ...
    def __getitem__(self, key: int) -> int: ...