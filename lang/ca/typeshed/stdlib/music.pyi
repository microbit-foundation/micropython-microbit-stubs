"""Crea i toca melodies. (música)"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Melodia: l'obertura de la cinquena simfonia de Beethoven en Do menor."""
ENTERTAINER: Tuple[str, ...]
"""Melodia: el fragment inicial del clàssic  Ragtime de Scott Joplin "The Entertainer"."""
PRELUDE: Tuple[str, ...]
"""Melodia: obertura del primer Preludi en Do Major dels 48 Preludis i Fugues de J.S. Bach. (preludi)"""
ODE: Tuple[str, ...]
"""Melodia: el tema "Oda a l'alegria" de la 9a simfonia en Re menor de Beethoven. (oda)"""
NYAN: Tuple[str, ...]
"""Melodia: el tema Nyan Cat (http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Melodia: quelcom que sona com un to de trucada de telèfon mòbil. (to de trucada)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Melodia: una línia de baix funky per a agents secrets i cervells criminals."""
BLUES: Tuple[str, ...]
"""Melodia: un  blues walking bass boogie-woogie de dotze compassos."""
BIRTHDAY: Tuple[str, ...]
"""Melodia:  “Feliç aniversari…” (aniversari)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melodia: el cor nupcial de l'òpera Lohengrin de Wagner. (casament)"""
FUNERAL: Tuple[str, ...]
"""Melodia: la “marxa fúnebre” com es coneix  la Sonata per a piano No 2. en Si bemoll menor Op. 35 de Frédéric Chopin ."""
PUNCHLINE: Tuple[str, ...]
"""Melodia: un fragment divertit que significa que s'ha fet una broma."""
PYTHON: Tuple[str, ...]
"""Melodia: la marxa de John Philip Sousa "Liberty Bell", també conegut com, el tema de "Monty Python's Flying Circus" (a partir de la qual s'anomena el llenguatge de programació Python)."""
BADDY: Tuple[str, ...]
"""Melodia: entrada d'un dolent a l'era del cinema mut. (dolent)"""
CHASE: Tuple[str, ...]
"""Melodia: escena de persecució de l'era del cinema mut. (persecució)"""
BA_DING: Tuple[str, ...]
"""Melodia: senyal breu per indicar que alguna cosa ha passat."""
WAWAWAWAA: Tuple[str, ...]
"""Melodia: un trombó molt trist."""
JUMP_UP: Tuple[str, ...]
"""Melodia: per utilitzar-se en un joc, indicant moviment cap amunt. (saltar cap amunt)"""
JUMP_DOWN: Tuple[str, ...]
"""Melodia: per utilitzar en un joc, que indica moviment cap avall. (saltar cap avall)"""
POWER_UP: Tuple[str, ...]
"""Melodia: una fanfàrria per indicar un assoliment desbloquejat. (engegar)"""
POWER_DOWN: Tuple[str, ...]
"""Melodia: una trista fanfàrria per indicar un assoliment perdut. (apagar)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Estableix el tempo aproximat per la reproducció.

Example: ``music.set_tempo(bpm=120)``

:param ticks: El nombre de tics que constitueixen un ritme.
:param bpm: Un nombre enter determinant quantes pulsacions per minut.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Obté el tempo actual com una tupla d'enters:``(ticks, bpm)``. (obté el tempo)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Tocar música

Example: ``music.play(music.NYAN)``

:param music: (música) música especificada en `una notació especial <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_
:param pin: el pin de sortida per utilitzar-lo amb un altaveu extern (``pin0`` per defecte), ``None`` per no fer so.
:param wait: (espera) Si ``wait`` s'estableix en ``True``, aquesta funció està bloquejant.
:param loop: (bucle) Si el ``loop`` s'estableix en ``True``, la melodia es repeteix fins que es crida ``stop`` o s'interromp la trucada de bloqueig.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Toca una nota. (altura del to)

Example: ``music.pitch(185, 1000)``

:param frequency: (freqüència) Una freqüència de nombre enter
:param duration: (Durada - duració) Una duració d'un mil·lisegon. Si és negativa, el so és continu fins a la nova crida o una crida a  ``stop``.
:param pin: Pin de sortida opcional (``pin0`` per defecte).
:param wait: (espera) Si ``wait`` s'estableix en ``True``, aquesta funció està bloquejant.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Atura tota la reproducció de música a l'altaveu integrat i qualsevol so de sortida de pin. (atura)

Example: ``music.stop()``

:param pin: Es pot proporcionar un argument opcional per especificar un pin, per exemple ``music.stop(pin1)``."""

def reset() -> None:
    """Restableix els tics, ppm, duració i octava al seu valor per defecte. (reiniciar)

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...