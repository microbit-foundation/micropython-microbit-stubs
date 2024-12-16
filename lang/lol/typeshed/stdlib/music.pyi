"""crwdns330448:0crwdne330448:0 (crwdns330446:0crwdne330446:0)"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""crwdns330452:0crwdne330452:0 (crwdns330450:0crwdne330450:0)"""
ENTERTAINER: Tuple[str, ...]
"""crwdns330456:0crwdne330456:0 (crwdns330454:0crwdne330454:0)"""
PRELUDE: Tuple[str, ...]
"""crwdns330460:0crwdne330460:0 (crwdns330458:0crwdne330458:0)"""
ODE: Tuple[str, ...]
"""crwdns330464:0crwdne330464:0 (crwdns330462:0crwdne330462:0)"""
NYAN: Tuple[str, ...]
"""crwdns330468:0crwdne330468:0 (crwdns330466:0crwdne330466:0)

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""crwdns330472:0crwdne330472:0 (crwdns330470:0crwdne330470:0)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""crwdns330476:0crwdne330476:0 (crwdns330474:0crwdne330474:0)"""
BLUES: Tuple[str, ...]
"""crwdns330480:0crwdne330480:0 (crwdns330478:0crwdne330478:0)"""
BIRTHDAY: Tuple[str, ...]
"""crwdns330484:0crwdne330484:0 (crwdns330482:0crwdne330482:0)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""crwdns330488:0crwdne330488:0 (crwdns330486:0crwdne330486:0)"""
FUNERAL: Tuple[str, ...]
"""crwdns330492:0crwdne330492:0 (crwdns330490:0crwdne330490:0)"""
PUNCHLINE: Tuple[str, ...]
"""crwdns330496:0crwdne330496:0 (crwdns330494:0crwdne330494:0)"""
PYTHON: Tuple[str, ...]
"""crwdns330500:0crwdne330500:0 (crwdns330498:0crwdne330498:0)"""
BADDY: Tuple[str, ...]
"""crwdns330504:0crwdne330504:0 (crwdns330502:0crwdne330502:0)"""
CHASE: Tuple[str, ...]
"""crwdns330508:0crwdne330508:0 (crwdns330506:0crwdne330506:0)"""
BA_DING: Tuple[str, ...]
"""crwdns330512:0crwdne330512:0 (crwdns330510:0crwdne330510:0)"""
WAWAWAWAA: Tuple[str, ...]
"""crwdns330516:0crwdne330516:0 (crwdns330514:0crwdne330514:0)"""
JUMP_UP: Tuple[str, ...]
"""crwdns330520:0crwdne330520:0 (crwdns330518:0crwdne330518:0)"""
JUMP_DOWN: Tuple[str, ...]
"""crwdns330524:0crwdne330524:0 (crwdns330522:0crwdne330522:0)"""
POWER_UP: Tuple[str, ...]
"""crwdns330528:0crwdne330528:0 (crwdns330526:0crwdne330526:0)"""
POWER_DOWN: Tuple[str, ...]
"""crwdns330532:0crwdne330532:0 (crwdns330530:0crwdne330530:0)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """crwdns330536:0crwdne330536:0 (crwdns330534:0crwdne330534:0)

Example: ``music.set_tempo(bpm=120)``

:param ticks: (crwdns330542:0crwdne330542:0) crwdns330544:0crwdne330544:0
:param bpm: (crwdns330538:0crwdne330538:0) crwdns330540:0crwdne330540:0

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """crwdns330548:0``(ticks, bpm)``crwdne330548:0 (crwdns330546:0crwdne330546:0)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """crwdns330552:0crwdne330552:0 (crwdns330550:0crwdne330550:0)

Example: ``music.play(music.NYAN)``

:param music: (crwdns330558:0crwdne330558:0) crwdns330560:0crwdne330560:0
:param pin: (crwdns330562:0crwdne330562:0) crwdns330564:0``pin0``crwdnd330564:0``None``crwdne330564:0
:param wait: (crwdns330566:0crwdne330566:0) crwdns330568:0``wait``crwdnd330568:0``True``crwdne330568:0
:param loop: (crwdns330554:0crwdne330554:0) crwdns330556:0``loop``crwdnd330556:0``True``crwdnd330556:0``stop``crwdne330556:0

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """crwdns330572:0crwdne330572:0 (crwdns330570:0crwdne330570:0)

Example: ``music.pitch(185, 1000)``

:param frequency: (crwdns330578:0crwdne330578:0) crwdns330580:0crwdne330580:0
:param duration: (crwdns330574:0crwdne330574:0) crwdns330576:0``stop``crwdne330576:0
:param pin: (crwdns330582:0crwdne330582:0) crwdns330584:0``pin0``crwdne330584:0
:param wait: (crwdns330586:0crwdne330586:0) crwdns330588:0``wait``crwdnd330588:0``True``crwdne330588:0

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """crwdns330592:0crwdne330592:0 (crwdns330590:0crwdne330590:0)

Example: ``music.stop()``

:param pin: (crwdns330594:0crwdne330594:0) crwdns330596:0``music.stop(pin1)``crwdne330596:0"""

def reset() -> None:
    """crwdns330600:0crwdne330600:0 (crwdns330598:0crwdne330598:0)

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...