"""讓 micro:bit 說話、唱歌和發出類似聲音的其他語音。"""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """將英語單字翻譯成音素。

Example: ``speech.translate('hello world')``

:param words: 英文單字字串。
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """發出音素的聲音。

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: 發音的音素字串
:param pitch: (間距) 一個代表聲音音高的數字
:param speed: 一個代表聲音速度的數字
:param mouth: 一個代表聲音口型的數字
:param throat: 一個代表聲音喉型的數字
:param pin: (引腳) 指定輸出引腳的可選引數，可用於覆寫預設值 ``pin0``。
如果我們不想從引腳上播放任何聲音，可以使用 ``pin=None``。僅限 micro:bit。

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """說英語單字。

Example: ``speech.say('hello world')``

:param words: 要說的一串詞。
:param pitch: (間距) 一個代表聲音音高的數字
:param speed: 一個代表聲音速度的數字
:param mouth: 一個代表聲音口型的數字
:param throat: 一個代表聲音喉型的數字
:param pin: (引腳) 指定輸出引腳的可選引數可用於覆寫預設值 ``pin0``。
如果我們無意從引腳上播放任何聲音，可以使用 ``pin=None``。僅限 micro:bit。

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """唱出音素。

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: 要唱的一串詞。
:param pitch: (間距) 一個代表聲音音高的數字
:param speed: 一個代表聲音速度的數字
:param mouth: 一個代表聲音口型的數字
:param throat: 一個代表聲音喉型的數字
:param pin: (引腳) 指定輸出引腳的可選引數，可用於覆寫預設值 ``pin0``。
如果我們不想從引腳上播放任何聲音，可以使用 ``pin=None``。僅限 micro:bit。

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...