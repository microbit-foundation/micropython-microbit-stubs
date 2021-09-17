"""This is the ``music`` module and you can use it to create and play melodies.
By default sound output will be via the edge connector on pin 0 and the
:doc:`built-in speaker <speaker>` **V2**. You can connect wired headphones or
a speaker to pin 0 and GND on the edge connector to hear the sound:
"""
from typing import Tuple, Union, List

from .microbit import MicroBitDigitalPin, pin0

DADADADUM: Tuple[str, ...]
ENTERTAINER: Tuple[str, ...]
PRELUDE: Tuple[str, ...]
ODE: Tuple[str, ...]
NYAN: Tuple[str, ...]
RINGTONE: Tuple[str, ...]
FUNK: Tuple[str, ...]
BLUES: Tuple[str, ...]
BIRTHDAY: Tuple[str, ...]
WEDDING: Tuple[str, ...]
FUNERAL: Tuple[str, ...]
PUNCHLINE: Tuple[str, ...]
PYTHON: Tuple[str, ...]
BADDY: Tuple[str, ...]
CHASE: Tuple[str, ...]
BA_DING: Tuple[str, ...]
WAWAWAWAA: Tuple[str, ...]
JUMP_UP: Tuple[str, ...]
JUMP_DOWN: Tuple[str, ...]
POWER_UP: Tuple[str, ...]
POWER_DOWN: Tuple[str, ...]

def set_tempo(ticks: int = ..., bpm: int = ...) -> None:
    """
    Sets the approximate tempo for playback.

    A number of ticks (expressed as an integer) constitute a beat.
    Each beat is to be played at a certain frequency per minute
    (expressed as the more familiar BPM - beats per minute -
     also as an integer).

    Suggested default values allow the following useful behaviour:

        music.set_tempo() - reset the tempo to default of ticks = 4, bpm = 120
        music.set_tempo(ticks=8) - change the “definition” of a beat
        music.set_tempo(bpm=180) - just change the tempo

    To work out the length of a tick in milliseconds is very simple arithmetic:
    60000/bpm/ticks_per_beat . For the default values that’s
    60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds.
    """
    ...

def get_tempo() -> Tuple[int, int]:
    """
    Gets the current tempo as a tuple of integers: (ticks, bpm).
    """
    ...

def play(
    music: Union[str, List[str], Tuple[str, ...]],
    pin: MicroBitDigitalPin = ...,
    wait: bool = True,
    loop: bool = False,
) -> None:
    """Plays ``music`` containing the musical DSL defined above.

    If ``music`` is a string it is expected to be a single note such as,
    ``'c1:4'``.

    If ``music`` is specified as a list of notes (as defined in the section on
    the musical DSL, above) then they are played one after the other to perform
    a melody.

    In both cases, the ``duration`` and ``octave`` values are reset to
    their defaults before the music (whatever it may be) is played.

    An optional argument to specify the output pin can be used to override the
    default of ``microbit.pin0``. If we do not want any sound to play we can
    use ``pin=None``.

    If ``wait`` is set to ``True``, this function is blocking.

    If ``loop`` is set to ``True``, the tune repeats until ``stop`` is called
    (see below) or the blocking call is interrupted.
    """
    ...

def pitch(
    frequency: int,
    duration: int = -1,
    pin: MicroBitDigitalPin = pin0,
    wait: bool = True,
) -> None:
    """Plays a pitch at the integer frequency given for the specified number of
    milliseconds. For example, if the frequency is set to 440 and the length to
    1000 then we hear a standard concert A for one second.

    Note that you can only play one pitch on one pin at any one time.

    An optional argument to specify the output pin can be used to override the
    default of ``microbit.pin0``. If we do not want any sound to play out of
    the pins we can use ``pin=None``.

    If ``wait`` is set to ``True``, this function is blocking.

    If ``duration`` is negative the pitch is played continuously until either
    the blocking call is interrupted or, in the case of a background call, a
    new frequency is set or ``stop`` is called (see below).
    """
    ...

def stop(pin: MicroBitDigitalPin = pin0) -> None:
    """Stops all music playback on the built-in speaker and any pin outputting
    sound. An optional argument can be provided to specify a pin, eg.
    ``music.stop(pin1)``.
    """

def reset() -> None:
    """Resets the state of the following attributes in the following way:

    * ``ticks = 4``
    * ``bpm = 120``
    * ``duration = 4``
    * ``octave = 4``
    """
    ...
