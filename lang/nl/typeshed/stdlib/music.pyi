"""Maak en speel melodieën. (muziek)"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Melodie: de opening naar Beethoven's 5e Symfonie in C minor."""
ENTERTAINER: Tuple[str, ...]
"""Melody: het openingsfragment van Scott Joplin’s Ragtime classic “The Entertainer”."""
PRELUDE: Tuple[str, ...]
"""Melodie: de opening van de eerste prelude in C Major van J.S.Bach's 48 Preludes en Fugues."""
ODE: Tuple[str, ...]
"""Melodie: het thema "Ode aan Joy" van Beethoven zijn negende Symfonie in D-klein."""
NYAN: Tuple[str, ...]
"""Melodie: het Nyan Cat thema (http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Melodie: iets dat klinkt als een beltoon van een mobiele telefoon. (beltoon)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Melodie: een grappige bas lijn voor geheime agenten en criminele meesterbreinen."""
BLUES: Tuple[str, ...]
"""Melodie: een boogie-woogie 12-bar blues wandel bas. (Blues)"""
BIRTHDAY: Tuple[str, ...]
"""Melodie: “Happy Birthday to You…” (verjaardag)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melodie: het bruidskoor van de opera van Wagner “Lohengrin”. (bruiloft)"""
FUNERAL: Tuple[str, ...]
"""Melody: de “begrafenismars” die ook bekend staat als Frédéric Chopin’s Piano Sonata No. 2 in B♭ minor, Op. 35. (begrafenis)"""
PUNCHLINE: Tuple[str, ...]
"""Melodie: een grappig fragment dat aangeeft dat er een grap is gemaakt. (clou)"""
PYTHON: Tuple[str, ...]
"""Melodie: John Philip Sousa's mars "Liberty Bell", ook bekend als het thema voor "Monty Python's Flying Circus" (waarnaar de programmeertaal Python is vernoemd)."""
BADDY: Tuple[str, ...]
"""Melodie: stomme filmtijdperk de binnenkomst van een boef. (boef)"""
CHASE: Tuple[str, ...]
"""Melodie: stille film tijdperk achtervolgings-scène. (achtervolgen)"""
BA_DING: Tuple[str, ...]
"""Melodie: een kort signaal om aan te geven dat er iets is gebeurd."""
WAWAWAWAA: Tuple[str, ...]
"""Melody: een zeer trieste trombone."""
JUMP_UP: Tuple[str, ...]
"""Melody: voor gebruik in een spel om opwaartse beweging aan te geven. (spring omhoog)"""
JUMP_DOWN: Tuple[str, ...]
"""Melody: voor gebruik in een spel, om neerwaartse beweging aan te geven. (spring omlaag)"""
POWER_UP: Tuple[str, ...]
"""Melodie: een fanfare die aantoont dat een prestatie ontgrendeld is. (opstarten)"""
POWER_DOWN: Tuple[str, ...]
"""Melody: een droevige fanfare om aan te geven dat een prestatie verloren is gegaan. (afsluiten)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Stelt het geschatte tempo in voor het afspelen. (kies tempo)

Example: ``music.set_tempo(bpm=120)``

:param ticks: (tikken) Het aantal tikken in een beat.
:param bpm: Een geheel getal dat het aantal beats per minuut bepaalt.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Haalt het huidige tempo op als een heel geheel getal: ``(ticks, bpm)``. (krijg tempo)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Speelt muziek af. (afspelen)

Example: ``music.play(music.NYAN)``

:param music: (muziek) muziek opgegeven in `a special notation <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_
:param pin: de uitvoer pin voor gebruik met een externe luidspreker (standaard ``pin0``), ``None`` voor geen geluid.
:param wait: (wacht) Als ``wait`` is ingesteld op ``True``wordt deze functie geblokkeerd.
:param loop: Als ``loop`` is ingesteld op ``True``herhaalt de melodie tot ``stop`` wordt opgeroepen of wordt de blokkerende oproep word onderbroken.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Speel een noot. (toonhoogte)

Example: ``music.pitch(185, 1000)``

:param frequency: (frequentie) Een integere frequentie
:param duration: (Duur) Een milliseconde duur. Als negatief dan gaat het geluid door tot de volgende oproep of een oproep tot ``stop``.
:param pin: Optionele uitvoer pin (standaard ``pin0``).
:param wait: (wacht) Als ``wait`` is ingesteld op ``True``wordt deze functie geblokkeerd.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Stopt alle muziek op de ingebouwde luidspreker en elke pin die geluid uitzendt.

Example: ``music.stop()``

:param pin: Een optioneel argument kan worden opgegeven om een pin op te geven, bijvoorbeeld ``music.stop(pin1)``."""

def reset() -> None:
    """Reset ticks, bpm, duur en octaven naar hun standaardwaarden.

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...