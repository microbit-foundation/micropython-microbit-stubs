"""Hacer que el micro:bit hable, cante y haga otros sonidos parecidos a la voz. (habla)"""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Traducir palabras en inglés a fonemas. (traducir)

Example: ``speech.translate('hello world')``

:param words: (palabras) Una cadena de palabras en inglés.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Pronunciar fonemas. (pronunciar)

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (fonemas) La cadena de fonemas a pronunciar
:param pitch: (tono) Un número que representa el tono de la voz
:param speed: (velocidad) Un número que representa la velocidad de la voz
:param mouth: (boca) Un número que representa la boca de la voz
:param throat: (garganta) Un número que representa la garganta de la voz
:param pin: Se puede usar un argumento opcional para especificar el pin de salida, reemplazando el valor predeterminado de ``pin0``.
Si no queremos que se reproduzca ningún sonido, podemos usar ``pin=None``. Solo para el micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Dice palabras en inglés. (decir)

Example: ``speech.say('hello world')``

:param words: (palabras) La cadena de palabras a decir.
:param pitch: (tono) Un número que representa el tono de la voz
:param speed: (velocidad) Un número que representa la velocidad de la voz
:param mouth: (boca) Un número que representa la boca de la voz
:param throat: (garganta) Un número que representa la garganta de la voz
:param pin: Se puede usar un argumento opcional para especificar el pin de salida, reemplazando el valor predeterminado de ``pin0``.
Si no queremos que se reproduzca ningún sonido, podemos usar ``pin=None``. Solo para el micro:bit V2.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Canta fonemas. (cantar)

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (fonemas) La cadena de palabras a cantar.
:param pitch: (tono) Un número que representa el tono de la voz
:param speed: (velocidad) Un número que representa la velocidad de la voz
:param mouth: (boca) Un número que representa la boca de la voz
:param throat: (garganta) Un número que representa la garganta de la voz
:param pin: Se puede usar un argumento opcional para especificar el pin de salida, reemplazando el valor predeterminado de ``pin0``.
Si no queremos que se reproduzca ningún sonido, podemos usar ``pin=None``. Solo para el micro:bit V2.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...