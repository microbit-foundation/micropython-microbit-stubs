"""使用 micro:bit 播放聲音 (匯入 ``audio`` 與 V1 相容)。"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Play a built-in sound, sound effect or custom audio frames.

Example: ``audio.play(Sound.GIGGLE)``

:param source: A built-in ``Sound`` such as ``Sound.GIGGLE``, a ``SoundEffect`` or sample data as an iterable of ``AudioFrame`` objects.
:param wait: 如果 ``wait`` 為 ``True``，此函式將會封鎖，直到聲音完成。
:param pin: (引腳) 指定輸出引腳的可選引數，可用於覆寫預設值 ``pin0``。如果我們不想播放任何聲音，我們可以使用 ``pin=None``。
:param return_pin: 指定差分邊緣連接器引腳，以連接到外部揚聲器而不是接地。在 **V2** 修訂版中，這將會被忽略。"""

def is_playing() -> bool:
    """檢查是否正在播放聲音。

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """停止所有音訊播放。

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
:param shape: The type of the interpolation curve between the start and end frequencies, different wave shapes have different rates of change in frequency. One of the following values: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Create a copy of this ``SoundEffect``.

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """``AudioFrame`` 物件是 32 個樣本的列表，每個樣本都是一個無符號位元組 (0 到 255 之間的整數)。

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