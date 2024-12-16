"""Laat de micro:bit praten, zingen en andere spraak maken, zoals geluid. (spraak)"""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Vertaal Engelse woorden naar fonemen. (vertalen)

Example: ``speech.translate('hello world')``

:param words: (woorden) Een tekenreeks Engelse woorden.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Uitspraak phonemes. (uitspreken)

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (fonemen) De reeks fonemen om uit te spreken
:param pitch: (toonhoogte) Een nummer dat de toonhoogte van de stem weergeeft
:param speed: (snelheid) Een nummer dat de snelheid van de stem vertegenwoordigt
:param mouth: (mond) Een nummer dat de mond van de stem weergeeft
:param throat: (keel) Een nummer dat de keel van de stem weergeeft
:param pin: Een optioneel argument om de uitvoer pin op te geven, kan worden gebruikt om de standaard van ``pin0``te overschrijven. Als we geen geluid willen afspelen, kunnen we ``pin=None`` gebruiken. Alleen voor micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Zeg Engelse woorden. (zeg)

Example: ``speech.say('hello world')``

:param words: (woorden) De tekenreeks van woorden om te zeggen.
:param pitch: (toonhoogte) Een nummer dat de toonhoogte van de stem weergeeft
:param speed: (snelheid) Een nummer dat de snelheid van de stem vertegenwoordigt
:param mouth: (mond) Een nummer dat de mond van de stem weergeeft
:param throat: (keel) Een nummer dat de keel van de stem weergeeft
:param pin: Een optioneel argument om de uitvoer pin op te geven, kan worden gebruikt om de standaard van ``pin0``te overschrijven. Als we geen geluid willen afspelen, kunnen we ``pin=None`` gebruiken. Alleen voor micro:bit V2.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Zing fonemen. (zing)

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (fonemen) De tekenreeks van woorden om te zingen.
:param pitch: (toonhoogte) Een nummer dat de toonhoogte van de stem weergeeft
:param speed: (snelheid) Een nummer dat de snelheid van de stem vertegenwoordigt
:param mouth: (mond) Een nummer dat de mond van de stem weergeeft
:param throat: (keel) Een nummer dat de keel van de stem weergeeft
:param pin: Een optioneel argument om de uitvoer pin op te geven, kan worden gebruikt om de standaard van ``pin0``te overschrijven. Als we geen geluid willen afspelen, kunnen we ``pin=None`` gebruiken. Alleen voor micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...