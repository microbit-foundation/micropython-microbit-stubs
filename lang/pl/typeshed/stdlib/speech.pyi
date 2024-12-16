"""Spraw, by micro:bit mówił, śpiewał i tworzył inne dźwięki podobne do mowy."""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Tłumacz angielskie słowa na fonemy.

Example: ``speech.translate('hello world')``

:param words: Łańcuch słów angielskich.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Wymów fonemy.

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: Łańcuch fonemów do wymówienia
:param pitch: Liczba reprezentująca wysokość głosu
:param speed: Liczba reprezentująca szybkość głosu
:param mouth: Liczba reprezentująca usta głosu
:param throat: Liczba reprezentująca gardło głosu
:param pin: Opcjonalny argument do określenia pinu wyjściowego może być użyty do nadpisania domyślnej wartości ``pin0``.
Jeśli nie chcemy, aby jakikolwiek dźwięk wydobywał się z pinów, możemy użyć ``pin=None``. Tylko micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Powiedz angielskie słowa.

Example: ``speech.say('hello world')``

:param words: Łańcuch słów do powiedzenia.
:param pitch: Liczba reprezentująca wysokość głosu
:param speed: Liczba reprezentująca szybkość głosu
:param mouth: Liczba reprezentująca usta głosu
:param throat: Liczba reprezentująca gardło głosu
:param pin: Opcjonalny argument do określenia pinu wyjściowego może być użyty do nadpisania domyślnej wartości ``pin0``.
Jeśli nie chcemy, aby jakikolwiek dźwięk wydobywał się z pinów, możemy użyć ``pin=None``. Tylko micro:bit V2.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Zaśpiewaj fonemy.

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: Łańcuch słów do zaśpiewania.
:param pitch: Liczba reprezentująca wysokość głosu
:param speed: Liczba reprezentująca szybkość głosu
:param mouth: Liczba reprezentująca usta głosu
:param throat: Liczba reprezentująca gardło głosu
:param pin: Opcjonalny argument do określenia pinu wyjściowego może być użyty do nadpisania domyślnej wartości ``pin0``.
Jeśli nie chcemy, aby jakikolwiek dźwięk wydobywał się z pinów, możemy użyć ``pin=None``. Tylko micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...