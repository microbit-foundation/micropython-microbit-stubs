"""Erstelle und spiele Lieder. (Musik)"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Melodie: Der Anfang von Beethovens 5. Symphonie in c-Moll. (dadadadaam)"""
ENTERTAINER: Tuple[str, ...]
"""Melodie: Die ersten Takte des Ragtime-Klassikers „The Entertainer“ von Scott Joplin. (Entertainer)"""
PRELUDE: Tuple[str, ...]
"""Melodie: Beginn des ersten Präludiums in C-Dur der 48 Präludien und Fugen von J.S. Bach."""
ODE: Tuple[str, ...]
"""Melodie: Die „Ode an die Freude“ von Beethovens neunter Symphonie in d-Moll. (Ode)"""
NYAN: Tuple[str, ...]
"""Melodie: Nyan-Katze (http://www.nyan.cat/). (Nyan)

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Melodie: Etwas, das wie ein Handy-Klingelton klingt. (Klingelton)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Melodie: eine funkige Basslinie für Geheimagenten und Superschurken. (Funk)"""
BLUES: Tuple[str, ...]
"""Melodie: ein 12-taktiger Boogie-Woogie-Blues mit Walking Bass. (Blues)"""
BIRTHDAY: Tuple[str, ...]
"""Melodie: „Alles Gute zum Geburtstag\xa0…“ (Geburtstag)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melodie: der Hochzeitschor aus Wagners Oper „Lohengrin“. (Hochzeit)"""
FUNERAL: Tuple[str, ...]
"""Melodie: Der „Trauermarsch“, auch bekannt als Frédéric Chopins Klaviersonate Nr. 2 in b-Moll, op. 35. (Beerdigung)"""
PUNCHLINE: Tuple[str, ...]
"""Melodie: ein lustiges Fragment, das anzeigt, dass ein Scherz gemacht worden ist."""
PYTHON: Tuple[str, ...]
"""Melodie: John Philip Sousas Marsch „Liberty Bell“, auch bekannt als die Titelmusik von „Monty Python's Flying Circus“ (nach dem die Programmiersprache Python benannt ist)."""
BADDY: Tuple[str, ...]
"""Melodie: Auftritt eines Stummfilm-Bösewichts."""
CHASE: Tuple[str, ...]
"""Melodie: Stummfilm-Verfolgungsszene."""
BA_DING: Tuple[str, ...]
"""Melodie: ein kurzes Signal, um anzuzeigen, dass etwas passiert ist."""
WAWAWAWAA: Tuple[str, ...]
"""Melody: Eine sehr traurige Posaune."""
JUMP_UP: Tuple[str, ...]
"""Melodie: zur Verwendung in einem Spiel, um eine Aufwärtsbewegung zu untermalen."""
JUMP_DOWN: Tuple[str, ...]
"""Melodie: zur Verwendung in einem Spiel, um eine Abwärtsbewegung zu untermalen."""
POWER_UP: Tuple[str, ...]
"""Melodie: eine Fanfare, die einen Erfolg anzeigt oder dass etwas freigeschalten wurde."""
POWER_DOWN: Tuple[str, ...]
"""Melodie: eine traurige Fanfare, wenn etwas nicht geklappt hat."""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Legt das ungefähre Tempo für die Wiedergabe fest.

Example: ``music.set_tempo(bpm=120)``

:param ticks: Die Anzahl der Ticks in einem Beat.
:param bpm: Ein Integerwert, der die Beats pro Minute angibt.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Gibt das aktuelle Tempo als Tupel von Integerwerten zurück: ``(ticks, bpm)``.

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Spielt Musik.

Example: ``music.play(music.NYAN)``

:param music: (Musik) Musik, die in `einer speziellen Notation <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_ angegeben ist
:param pin: der Ausgangspin zur Verwendung mit einem externen Lautsprecher (Voreinstellung ``pin0``), ``None`` für keinen Ton.
:param wait: Wenn ``wait`` auf ``True`` gesetzt ist, stoppt diese Funktion die weitere Codeausführung.
:param loop: Wenn ``loop`` auf ``True`` gesetzt ist, wird die Melodie wiederholt, bis ``stop`` aufgerufen oder der blockierende Aufruf unterbrochen wird.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Musiknoten spielen (Tonhöhe)

Example: ``music.pitch(185, 1000)``

:param frequency: (Frequenz) Eine ganzzahlige Frequenz
:param duration: (Dauer) Eine Dauer in Millisekunden. Bei negativem Wert erhält man bis zum nächsten Aufruf oder einem Aufruf von ``stop`` einen Dauerton.
:param pin: Optionaler Ausgabepin (Standard ``pin0``).
:param wait: Wenn ``wait`` auf ``True`` gesetzt ist, stoppt diese Funktion die weitere Codeausführung.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Stoppt die Musikwiedergabe über den eingebauten Lautsprecher sowie jeden Pin, der Sound ausgibt.

Example: ``music.stop()``

:param pin: Ein optionales Argument kann zur Angabe eines Pins angegeben werden, z. B. ``music.stop(pin1)``."""

def reset() -> None:
    """Setzt Ticks, bpm, Dauer und Oktave auf ihre Standardwerte zurück. (zurücksetzen)

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...