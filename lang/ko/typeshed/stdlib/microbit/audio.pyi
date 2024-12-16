"""micro:bit을 활용해 소리를 재생합니다(V1 호환을 위해서는 ``audio``를 가져오세요)."""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Play a built-in sound, sound effect or custom audio frames.

Example: ``audio.play(Sound.GIGGLE)``

:param source: A built-in ``Sound`` such as ``Sound.GIGGLE``, a ``SoundEffect`` or sample data as an iterable of ``AudioFrame`` objects.
:param wait: ``wait``이 ``True``인 경우 사운드 재생이 완료될 때까지 이 함수가 차단됩니다.
:param pin: (핀) ``pin0``의 기본값을 덮어쓰는 데 사용할 출력 핀을 특정하는 인자입니다(선택 사항). 사운드를 재생하고 싶지 않다면 ``pin=None``을 사용할 수 있습니다.
:param return_pin: 접지 대신 외부 스피커에 연결할 차동 엣지 커넥터 핀을 특정합니다. **V2** 수정 버전에서는 무시합니다."""

def is_playing() -> bool:
    """소리가 재생 중인지 체크합니다.

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """모든 오디오 플레이백을 중지합니다.

Example: ``audio.stop()``"""
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

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Create a new sound effect. (string)

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
:param shape: The type of the interpolation curve between the start and end frequencies, different wave shapes have different rates of change in frequency. One of the following values: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Create a copy of this ``SoundEffect``.

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """``AudioFrame`` 오브젝트는 부호 없는 바이트 샘플 32개의 리스트입니다(0에서 255 사이의 모든 숫자).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Overwrite the data in this ``AudioFrame`` with the data from another ``AudioFrame`` instance.

Example: ``my_frame.copyfrom(source_frame)``

:param other: ``AudioFrame`` instance from which to copy the data."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...