"""micro:bit이 말하고 노래부르고 소리를 재생하게 합니다."""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """영단어를 음소로 변환합니다.

Example: ``speech.translate('hello world')``

:param words: 영단어 문자열입니다.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """음소를 발음합니다.

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: 발음할 음소의 문자열
:param pitch: (앞-뒤 기울기) 목소리의 음높이를 표현하는 숫자
:param speed: 목소리의 속도를 표현하는 숫자
:param mouth: 목소리의 입 모양을 표현하는 숫자
:param throat: 목소리의 목 모양을 표현하는 숫자
:param pin: (핀) ``pin0``의 기본값을 덮어쓰고 출력 핀을 특정하는 인자입니다(선택 사항).
핀에서 사운드를 재생하기 싫다면 ``pin=None``을 사용할 수 있습니다. micro:bit V2 전용입니다.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """영어 단어를 말합니다.

Example: ``speech.say('hello world')``

:param words: 말할 단어의 문자열입니다.
:param pitch: (앞-뒤 기울기) 목소리의 음높이를 표현하는 숫자
:param speed: 목소리의 속도를 표현하는 숫자
:param mouth: 목소리의 입 모양을 표현하는 숫자
:param throat: 목소리의 목 모양을 표현하는 숫자
:param pin: (핀) ``pin0``의 기본값을 덮어쓰고 출력 핀을 특정하는 인자입니다(선택 사항).
핀에서 사운드를 재생하기 싫다면 ``pin=None``을 사용할 수 있습니다. micro:bit V2 전용입니다.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """음소를 노래합니다.

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: 노래할 단어 문자열입니다.
:param pitch: (앞-뒤 기울기) 목소리의 음높이를 표현하는 숫자
:param speed: 목소리의 속도를 표현하는 숫자
:param mouth: 목소리의 입 모양을 표현하는 숫자
:param throat: 목소리의 목 모양을 표현하는 숫자
:param pin: (핀) ``pin0``의 기본값을 덮어쓰고 출력 핀을 특정하는 인자입니다(선택 사항).
핀에서 사운드를 재생하기 싫다면 ``pin=None``을 사용할 수 있습니다. micro:bit V2 전용입니다.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...