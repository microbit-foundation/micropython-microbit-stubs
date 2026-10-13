"""Faz o micro:bit falar, cantar e emitir outros sons semelhantes à fala. (discurso)"""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Traduzir palavras em inglês para fonemas. (traduzir)

Example: ``speech.translate('hello world')``

:param words: (palavras) Uma sequência de palavras em inglês.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Pronunciar fonemas. (pronúncia)

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (fonemas) A sequência de fonemas a ser pronunciada.
:param pitch: (inclinação) Um número que representa o tom da voz.
:param speed: (velocidade) Um número que representa a velocidade da voz.
:param mouth: (boca) Um número representando a boca da voz.
:param throat: (garganta) Um número que representa a garganta da voz.
:param pin: (alfinete) Argumento opcional para especificar o pino de saída, podendo substituir o padrão de ``pin0``.  
Se não desejarmos que nenhum som seja reproduzido pelos pinos, podemos usar ``pin=None``. Somente para micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Dizer palavras em inglês. (dizer)

Example: ``speech.say('hello world')``

:param words: (palavras) A sequência de palavras a ser dita.
:param pitch: (inclinação) Um número que representa o tom da voz.
:param speed: (velocidade) Um número que representa a velocidade da voz.
:param mouth: (boca) Um número representando a boca da voz.
:param throat: (garganta) Um número que representa a garganta da voz.
:param pin: (alfinete) Argumento opcional para especificar o pino de saída, podendo substituir o padrão de ``pin0``.  
Se não desejarmos que nenhum som seja reproduzido pelos pinos, podemos usar ``pin=None``. Somente para micro:bit V2.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Cante fonemas. (cantar)

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (fonemas) A sequência de palavras a ser cantada.
:param pitch: (inclinação) Um número que representa o tom da voz.
:param speed: (velocidade) Um número que representa a velocidade da voz.
:param mouth: (boca) Um número representando a boca da voz.
:param throat: (garganta) Um número que representa a garganta da voz.
:param pin: (alfinete) Argumento opcional para especificar o pino de saída, podendo substituir o padrão de ``pin0``.  
Se não desejarmos que nenhum som seja reproduzido pelos pinos, podemos usar ``pin=None``. Somente para micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...