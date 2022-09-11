"""Faites parler ou chanter le micro:bit, ainsi que d'autres sons liés à la parole."""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Traduire les mots anglais en phonèmes.

Example: ``speech.translate('hello world')``

:param words: Une chaîne de caractères de mots anglais.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Prononcer les phonèmes.

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: La chaîne de phonèmes à prononcer
:param pitch: (tangage) Un nombre représentant le ton de la voix
:param speed: Un nombre représentant la vitesse de la voix
:param mouth: Un nombre représentant la bouche de la voix
:param throat: Un nombre représentant la gorge de la voix
:param pin: (broche) Argument optionnel pour spécifier la broche de sortie. Peut être utilisé pour remplacer la valeur par défaut de ``pin0``.
Pour empêcher l'émission d'un son via les broches, il est possible d'utiliser ``pin=None``. micro:bit V2 seulement.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Dire des mots anglais.

Example: ``speech.say('hello world')``

:param words: La chaîne de mots à dire.
:param pitch: (tangage) Un nombre représentant le ton de la voix
:param speed: Un nombre représentant la vitesse de la voix
:param mouth: Un nombre représentant la bouche de la voix
:param throat: Un nombre représentant la gorge de la voix
:param pin: (broche) Argument optionnel pour spécifier la broche de sortie. Peut être utilisé pour remplacer la valeur par défaut de ``pin0``.
Pour empêcher l'émission d'un son via les broches, il est possible d'utiliser ``pin=None``. micro:bit V2 seulement.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Chanter des phonèmes.

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: La chaîne de mots à chanter.
:param pitch: (tangage) Un nombre représentant le ton de la voix
:param speed: Un nombre représentant la vitesse de la voix
:param mouth: Un nombre représentant la bouche de la voix
:param throat: Un nombre représentant la gorge de la voix
:param pin: (broche) Argument optionnel pour spécifier la broche de sortie. Peut être utilisé pour remplacer la valeur par défaut de ``pin0``.
Pour empêcher l'émission d'un son via les broches, il est possible d'utiliser ``pin=None``. micro:bit V2 seulement.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...