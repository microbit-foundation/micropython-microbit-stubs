"""使用 micro:bit 播放声音（导入 ``audio`` 以兼容 V1）。 (音频)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """播放内置声音、音效或自定义音频帧。 (播放)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (来源) 内置的 ``Sound``，例如 ``Sound.GIGGLE``、``SoundEffect`` 或作为 ``AudioFrame`` 的可迭代对象的样本数据。
:param wait: (等待) 如果 ``wait`` 为 ``True``, 此函数将会阻塞直到声音完成。
:param pin: (引脚) 可选参数， 用于指定可覆盖默认 ``pin0`` 的输出引脚。 如果不想播放任何声音，可以使用 ``pin=None``。
:param return_pin: 指定一个差分边缘连接器引脚以连接到外部扬声器而不是接地。对于 **V2** 修订版，这将被忽略。"""

def is_playing() -> bool:
    """检查是否在播放声音。

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """停止所有音频播放。 (停止)

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """一种音效，由一组通过构造函数或属性配置的参数组成。 (音效)"""
    WAVEFORM_SINE: ClassVar[int]
    """用于 ``waveform`` 参数的正弦波选项。 (波形正弦)"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """用于 ``waveform`` 参数的锯齿波选项。 (波形锯齿)"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """用于 ``waveform`` 参数的三角波选项。 (波形三角)"""
    WAVEFORM_SQUARE: ClassVar[int]
    """用于 ``waveform`` 参数的方波选项。 (方波)"""
    WAVEFORM_NOISE: ClassVar[int]
    """用于 ``waveform`` 参数的噪声选项。 (波形噪声)"""
    SHAPE_LINEAR: ClassVar[int]
    """用于 ``shape`` 参数的线性插值选项。 (形状线性)"""
    SHAPE_CURVE: ClassVar[int]
    """用于 ``shape`` 参数的曲线插值选项。 (形状曲线)"""
    SHAPE_LOG: ClassVar[int]
    """用于 ``shape`` 参数的对数插值选项。 (形状日志)"""
    FX_NONE: ClassVar[int]
    """没有用于 ``fx`` 参数的效果选项。 (fx 无)"""
    FX_TREMOLO: ClassVar[int]
    """用于 ``fx`` 参数的音量颤音效果选项。 (fx 音量颤音)"""
    FX_VIBRATO: ClassVar[int]
    """用于 ``fx`` 参数的音高颤音效果选项。 (fx 音高颤音)"""
    FX_WARBLE: ClassVar[int]
    """用于 ``fx`` 参数的柔和颤音效果选项。 (fx 柔和颤音)"""
    freq_start: int
    """开始频率用 Hertz (Hz) 表示, 是一个 ``0`` 和 ``9999`` 之间的数字 (开始频率)"""
    freq_end: int
    """结束频率用 Hertz (Hz) 表示, 是一个 ``0`` 和 ``9999`` 之间的数字 (结束频率)"""
    duration: int
    """声音持续时间，以毫秒计， 是一个 ``0`` 和 ``9999`` 之间的数字 (持续)"""
    vol_start: int
    """开始音量值，是一个 ``0`` 和 ``255`` 之间的数字 (开始音量值)"""
    vol_end: int
    """结束音量值，是一个 ``0`` 和 ``255`` 之间的数字 (结束音量值)"""
    waveform: int
    """波形类型，是下列值之一： ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (随机生成噪音) (波形)"""
    fx: int
    """对声音添加效果，下列值之一： ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, 或 ``FX_NONE``"""
    shape: int
    """开始频率和结束频率之间的内插曲线类型，不同波形的频率变化速率不同。 以下值之一: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG`` (形状)"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """创建新的音效。

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: (开始频率) 开始频率用 Hertz (Hz) 表示, 是一个 ``0`` 和 ``9999`` 之间的数字.
:param freq_end: (结束频率) 结束频率用 Hertz (Hz) 表示, 是一个 ``0`` 和 ``9999`` 之间的数字.
:param duration: (持续) 声音持续时间，以毫秒计， 是一个 ``0`` 和 ``9999`` 之间的数字.
:param vol_start: (开始音量值) 开始音量值，是一个 ``0`` 和 ``255`` 之间的数字.
:param vol_end: (结束音量值) 结束音量值，是一个 ``0`` 和 ``255`` 之间的数字.
:param waveform: (波形) 波形类型，是下列值之一： ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (随机生成噪音).
:param fx: 对声音添加效果，下列值之一： ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, 或 ``FX_NONE``.
:param shape: (形状) 开始频率和结束频率之间的内插曲线类型，不同波形的频率变化速度不同。 以下值之一: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """创建此 ``SoundEffect`` 的副本。 (复制)

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """``AudioFrame`` 对象是 一个包含 32 个样本的列表，每个样本都是一个无符号字节
（0 到 255 之间的整数）。 (音频帧)

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """用其他 ``AudioFrame`` 实例中的数据覆盖此 ``AudioFrame`` 中的数据。 (复制)

Example: ``my_frame.copyfrom(source_frame)``

:param other: (其他) 从 ``AudioFrame`` 实例中复制数据。"""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...