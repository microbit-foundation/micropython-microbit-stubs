"""This module makes the micro:bit talk, sing and make other speech like sounds.
By default sound output will be via the edge connector on pin 0 and the
:doc:`built-in speaker <speaker>` **V2**. You can connect wired headphones or
a speaker to pin 0 and GND on the edge connector to hear the sound:

.. note::

    This work is based upon the amazing reverse engineering efforts of
    Sebastian Macke based upon an old text-to-speech (TTS) program called SAM
    (Software Automated Mouth) originally released in 1982 for the
    Commodore 64. The result is a small C library that we have adopted and
    adapted for the micro:bit. You can find out more from
    `his homepage <http://simulationcorner.net/index.php?page=sam>`_. Much of
    the information in this document was gleaned from the original user's
    manual which can be found
    `here <http://www.apple-iigs.info/newdoc/sam.pdf>`_.

The speech synthesiser can produce around 2.5 seconds worth of sound from up to
255 characters of textual input.

To access this module you need to::

    import speech
"""

from typeshed.stdlib.microbit import MicroBitAnalogDigitalPin, pin0


def translate(words: str) -> str:
    """Given English words in the string ``words``, return a string containing
    a best guess at the appropriate phonemes to pronounce. The output is
    generated from this
    `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

    This function should be used to generate a first approximation of phonemes
    that can be further hand-edited to improve accuracy, inflection and
    emphasis.
    """
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72,
              mouth: int=128, throat: int=128, 
              pin: MicroBitAnalogDigitalPin = pin0) -> None:
    """Pronounce the phonemes in the string ``phonemes``. See below for details of
    how to use phonemes to finely control the output of the speech synthesiser.
    Override the optional pitch, speed, mouth and throat settings to change the
    timbre (quality) of the voice.

    For micro:bit **V2** an optional argument to specify the output pin can be
    used to override the default of ``pin0``. If we do not want any sound to
    play out of the pins can use ``pin=None``.
    """
    ...

def say(words: str, pitch: int=64, speed: int=72,
              mouth: int=128, throat: int=128, pin: MicroBitAnalogDigitalPin=pin0) -> None:
    """Say the English words in the string ``words``. The result is semi-accurate
    for English. Override the optional pitch, speed, mouth and throat
    settings to change the timbre (quality) of the voice. This is a short-hand
    equivalent of: ``speech.pronounce(speech.translate(words))``
    """
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72,
              mouth: int=128, throat: int=128, pin: MicroBitAnalogDigitalPin=pin0) -> None:
    """Sing the phonemes contained in the string ``phonemes``. Changing the pitch
    and duration of the note is described below. Override the optional pitch,
    speed, mouth and throat settings to change the timbre (quality) of the
    voice.
    """
    ...