"""使 micro:bit 说话、唱歌和发出其他类似语音的声音。 (语音)"""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """把英语单词翻译成音素。 (翻译)

Example: ``speech.translate('hello world')``

:param words: (单词) 一连串英语单词。
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """发出音素的声音。 (发音)

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (音素) 要发音的音素串
:param pitch: (音高) 代表声音音高的数字
:param speed: (速度：) 代表声音速度的数字
:param mouth: (嘴巴) 表示声音口型的数字
:param throat: (喉部) 表示声音喉型的数字
:param pin: (引脚) 可选参数，可用于指定输出引脚来覆盖 ``pin0`` 默认值。
如果不想从引脚上播放任何声音，可以使用 ``pin=None``。仅限micro:bit V2。

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """说英语单词。 (说)

Example: ``speech.say('hello world')``

:param words: (单词) 要说的词串。
:param pitch: (音高) 代表声音音高的数字
:param speed: (速度) 代表声音速度的数字
:param mouth: (嘴部) 表示声音口型的数字
:param throat: (喉部) 表示声音喉型的数字
:param pin: (引脚) 可选参数，可用于指定输出引脚来覆盖 ``pin0`` 默认值。
如果不想从引脚上播放任何声音，可以使用 ``pin=None``。仅限micro:bit V2。

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """唱音素。 (唱歌)

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (音素) 要唱的词串。
:param pitch: (音高) 代表声音音高的数字
:param speed: (速度) 代表声音速度的数字
:param mouth: (嘴部) 表示声音口型的数字
:param throat: (喉部) 表示声音喉型的数字
:param pin: (引脚) 可选参数，可用于指定输出引脚来覆盖 ``pin0`` 默认值。
如果不想从引脚上播放任何声音，可以使用 ``pin=None``。仅限micro:bit V2。

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...