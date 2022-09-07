"""micro:bit に話をさせ、歌わせ、その他の音声のようなサウンドを作らせます。 (speech)"""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """英単語の並びを音素に変換します。 (translate)

Example: ``speech.translate('hello world')``

:param words: (words) 英単語の並びの文字列。
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """音素を発声します。 (pronounce)

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (phonemes) 発音する音素の文字列
:param pitch: (pitch) 音声のピッチを表す数値
:param speed: (speed) 音声の速度を表す数値
:param mouth: (mouth) 音声の口の動きを表す数値
:param throat: (throat) 音声の喉の動きを表す数値
:param pin: (ピン) 出力端子をデフォルトの ``pin0`` から変えるためのオプション引数。
音を鳴らしたくない場合は ``pin=None`` を指定します。
micro:bit V2 のみで使えます。

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """英単語の並びを発声します。 (say)

Example: ``speech.say('hello world')``

:param words: (words) 発声する言葉の文字列。
:param pitch: (pitch) 音声のピッチを表す数値
:param speed: (speed) 音声の速度を表す数値
:param mouth: (mouth) 音声の口の動きを表す数値
:param throat: (throat) 音声の喉の動きを表す数値
:param pin: (ピン) 出力端子をデフォルトの ``pin0`` から変えるためのオプション引数。
音を鳴らしたくない場合は ``pin=None`` を指定します。
micro:bit V2 のみで使えます。

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """音素を歌います。 (sing)

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (phonemes) 歌う言葉の文字列。
:param pitch: (pitch) 音声のピッチを表す数値
:param speed: (speed) 音声の速度を表す数値
:param mouth: (mouth) 音声の口の動きを表す数値
:param throat: (throat) 音声の喉の動きを表す数値
:param pin: (ピン) 出力端子をデフォルトの ``pin0`` から変えるためのオプション引数。
音を鳴らしたくない場合は ``pin=None`` を指定します。
micro:bit V2 のみで使えます。

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...