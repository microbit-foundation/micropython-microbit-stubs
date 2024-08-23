"""crwdns330892:0crwdne330892:0 (crwdns330890:0crwdne330890:0)"""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """crwdns330896:0crwdne330896:0 (crwdns330894:0crwdne330894:0)

Example: ``speech.translate('hello world')``

:param words: (crwdns330898:0crwdne330898:0) crwdns330900:0crwdne330900:0
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """crwdns330904:0crwdne330904:0 (crwdns330902:0crwdne330902:0)

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (crwdns330910:0crwdne330910:0) crwdns330912:0crwdne330912:0
:param pitch: (crwdns330918:0crwdne330918:0) crwdns330920:0crwdne330920:0
:param speed: (crwdns330922:0crwdne330922:0) crwdns330924:0crwdne330924:0
:param mouth: (crwdns330906:0crwdne330906:0) crwdns330908:0crwdne330908:0
:param throat: (crwdns330926:0crwdne330926:0) crwdns330928:0crwdne330928:0
:param pin: (crwdns330914:0crwdne330914:0) crwdns330916:0``pin0``crwdne330916:0

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """crwdns330932:0crwdne330932:0 (crwdns330930:0crwdne330930:0)

Example: ``speech.say('hello world')``

:param words: (crwdns330954:0crwdne330954:0) crwdns330956:0crwdne330956:0
:param pitch: (crwdns330942:0crwdne330942:0) crwdns330944:0crwdne330944:0
:param speed: (crwdns330946:0crwdne330946:0) crwdns330948:0crwdne330948:0
:param mouth: (crwdns330934:0crwdne330934:0) crwdns330936:0crwdne330936:0
:param throat: (crwdns330950:0crwdne330950:0) crwdns330952:0crwdne330952:0
:param pin: (crwdns330938:0crwdne330938:0) crwdns330940:0``pin0``crwdne330940:0

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """crwdns330960:0crwdne330960:0 (crwdns330958:0crwdne330958:0)

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (crwdns330966:0crwdne330966:0) crwdns330968:0crwdne330968:0
:param pitch: (crwdns330974:0crwdne330974:0) crwdns330976:0crwdne330976:0
:param speed: (crwdns330978:0crwdne330978:0) crwdns330980:0crwdne330980:0
:param mouth: (crwdns330962:0crwdne330962:0) crwdns330964:0crwdne330964:0
:param throat: (crwdns330982:0crwdne330982:0) crwdns330984:0crwdne330984:0
:param pin: (crwdns330970:0crwdne330970:0) crwdns330972:0``pin0``crwdne330972:0

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...