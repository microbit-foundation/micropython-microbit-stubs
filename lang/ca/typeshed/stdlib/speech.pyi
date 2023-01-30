"""Fes que la micro:bit parli, canti i fer altres expressions com els sons."""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Tradueix paraules angleses a fonemes. (tradueix)

Example: ``speech.translate('hello world')``

:param words: (paraules) Una cadena de paraules angleses.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Pronuncia fonemes. (pronuncia)

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (fonemes) La cadena de fonemes a pronunciar
:param pitch: (to) Un nombre que representa la freqüència de la veu
:param speed: (velocitat) Un nombre que representa la velocitat de la veu
:param mouth: (boca) Un nombre que representa la boca de la veu
:param throat: Un nombre que representa la gola de la veu
:param pin: L'argument opcional per especificar el pin de sortida es pot utilitzar per anul·lar el valor predeterminat de ``pin0``.
Si no vols que es reprodueixi cap so en els pins, podts utilitzar ``pin=None``. Només micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Digues paraules en anglès.

Example: ``speech.say('hello world')``

:param words: (paraules) La cadena de paraules a dir.
:param pitch: (to) Un nombre que representa la freqüència de la veu
:param speed: (velocitat) Un nombre que representa la velocitat de la veu
:param mouth: (boca) Un nombre que representa la boca de la veu
:param throat: Un nombre que representa la gola de la veu
:param pin: L'argument opcional per especificar el pin de sortida es pot utilitzar per anul·lar el valor predeterminat del ``pin0``.
Si no vols que es reprodueixi cap so en els pins, pots utilitzar ``pin=None``. Només micro:bit V2.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Cantar fonemes.

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (fonemes) La cadena de paraules a cantar.
:param pitch: (to) Un nombre que representa la freqüència de la veu
:param speed: (velocitat) Un nombre que representa la velocitat de la veu
:param mouth: (boca) Un nombre que representa la boca de la veu
:param throat: Un nombre que representa la gola de la veu
:param pin: L'argument opcional per especificar el pin de sortida es pot utilitzar per anul·lar el valor predeterminat de ``pin0``.
Si no vols que es reprodueixi cap so en els pins, podts utilitzar ``pin=None``. Només micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...