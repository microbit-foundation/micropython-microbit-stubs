"""Bringe den micro:bit zum Sprechen, singen und dazu, andere sprachähnliche Geräusche zu machen."""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Übersetzt englische Wörter in Sprache.

Example: ``speech.translate('hello world')``

:param words: (Wörter) Ein String englischer Wörter.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Spricht Laute aus.

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (Phoneme) Die auszusprechende Laut als Zeichenkette.
:param pitch: (Tonhöhe) Eine Zahl, die die Tonhöhe der Stimme angibt.
:param speed: (tempo) Eine Zahl, die die Geschwindigkeit der Stimme angibt.
:param mouth: (Mund) Eine Zahl, die den Mund der Stimme repräsentiert.
:param throat: (klang) Eine Zahl, die den Klang der Stimme angibt.
:param pin: Optionales Argument, um den Ausgangspin anzugeben, kann verwendet werden, um den Standardwert von ``pin0`` zu überschreiben. Wenn wir keinen Ton über die Pins abspielen wollen, können wir ``pin=None`` verwenden. nur micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Sage englische Wörter (sage)

Example: ``speech.say('hello world')``

:param words: (Wörter) Der zu sagene String
:param pitch: (Tonhöhe) Eine Zahl, die die Tonhöhe der Stimme angibt.
:param speed: (tempo) Eine Zahl, die die Geschwindigkeit der Stimme angibt.
:param mouth: (Mund) Eine Zahl, die den Mund der Stimme repräsentiert.
:param throat: (klang) Eine Zahl, die den Klang der Stimme angibt.
:param pin: Optionales Argument, um den Ausgangspin anzugeben, kann verwendet werden, um den Standardwert von ``pin0`` zu überschreiben. Wenn wir keinen Ton über die Pins abspielen wollen, können wir ``pin=None`` verwenden. nur micro:bit V2.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Singt Laute.

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (Phoneme) Der zu singende String.
:param pitch: (Tonhöhe) Eine Zahl, die die Tonhöhe der Stimme angibt.
:param speed: (tempo) Eine Zahl, die die Geschwindigkeit der Stimme angibt.
:param mouth: (Mund) Eine Zahl, die den Mund der Stimme repräsentiert.
:param throat: (klang) Eine Zahl, die den Klang der Stimme angibt.
:param pin: Optionales Argument, um den Ausgangspin anzugeben, kann verwendet werden, um den Standardwert von ``pin0`` zu überschreiben. Wenn wir keinen Ton über die Pins abspielen wollen, können wir ``pin=None`` verwenden. nur micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...