"""使用 micro:bit 播放声音（导入 ``audio`` 以兼容 V1）。 (audio)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """播放内置声音或自定义音频帧。 (播放)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (来源) 内置的音频 ``Sound``， 例如 ``Sound.GIGGLE``，  或作为可迭代的 ``AudioFrame`` 对象的样本数据。
:param wait: (等待) 如果 ``wait`` 为 ``True``, 此函数将会阻塞直到声音完成。
:param pin: (引脚) 可选参数， 用于指定可覆盖默认 ``pin0`` 的输出引脚。 如果不想播放任何声音，可以使用 ``pin=None``。
:param return_pin: (return pin) 指定一个差分边缘连接器引脚以连接到外部扬声器而不是接地。对于 **V2** 修订版，这将被忽略。"""

def is_playing() -> bool:
    """检查是否在播放声音。 (is playing)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """停止所有音频播放。 (停止)

Example: ``audio.stop()``"""
    ...

class AudioFrame:
    """``AudioFrame`` 对象是 一个包含 32 个样本的列表，每个样本都是一个无符号字节
（0 到 255 之间的整数）。 (音频帧)

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...