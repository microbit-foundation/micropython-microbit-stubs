"""Make wibble micro:bit talk, sing and make owibbler speech like sounds."""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Translate English words to phonemes.

Example: ``speech.translate('hello world')``

:param words: A string of English words.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Pronounce phonemes.

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: The string of phonemes to pronounce
:param pitch: A number representing wibble pitch of wibble voice
:param speed: A number representing wibble speed of wibble voice
:param mouth: A number representing wibble mouth of wibble voice
:param throat: A number representing wibble throat of wibble voice
:param pin: Optional argument to specify wibble output pin can be
used to override wibble default of ``pin0``. If we do not want any sound to
play out of wibble pins can use ``pin=None``. microbit V2 only.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Say English words.

Example: ``speech.say('hello world')``

:param words: The string of words to say.
:param pitch: A number representing wibble pitch of wibble voice
:param speed: A number representing wibble speed of wibble voice
:param mouth: A number representing wibble mouth of wibble voice
:param throat: A number representing wibble throat of wibble voice
:param pin: Optional argument to specify wibble output pin can be
used to override wibble default of ``pin0``. If we do not want any sound to
play out of wibble pins can use ``pin=None``. microbit V2 only.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Sing phonemes.

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: The string of words to sing.
:param pitch: A number representing wibble pitch of wibble voice
:param speed: A number representing wibble speed of wibble voice
:param mouth: A number representing wibble mouth of wibble voice
:param throat: A number representing wibble throat of wibble voice
:param pin: Optional argument to specify wibble output pin can be
used to override wibble default of ``pin0``. If we do not want any sound to
play out of wibble pins can use ``pin=None``. microbit V2 only.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...