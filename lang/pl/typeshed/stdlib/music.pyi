"""Twórz i graj w melodie."""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Melodia: otwarcie 5. symfonii Beethovena w C minor"""
ENTERTAINER: Tuple[str, ...]
"""Melodia: fragment otwierający klasyczny Scott Joplin Ragtime "The Entertainer"."""
PRELUDE: Tuple[str, ...]
"""Melodia: otwarcie pierwszego Preludium w C Major, 48 preludiów i Fug J.S.Bacha."""
ODE: Tuple[str, ...]
"""Melodia: motyw Ody do radości z 9. Symfonii Beethovena w D minor."""
NYAN: Tuple[str, ...]
"""Melodia: motyw Nyan Kot (http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Melodia: coś, co brzmi jak dzwonek telefonu komórkowego.

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Melody: funkowa linia basu dla tajnych agentów i geniuszy kryminalnych."""
BLUES: Tuple[str, ...]
"""Melodia: 12-taktowy bluesowy chodzący bas w stylu boogie-woogie."""
BIRTHDAY: Tuple[str, ...]
"""Melodia: "Wszystkiego najlepszego…"

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melodia: chór panny młodej z opery Wagnera „Lohengrin”. (ślub)"""
FUNERAL: Tuple[str, ...]
"""Melodia: »Marsz pogrzebowy« znany jako Sonata Fortepianowa No. 2 w B♭ minor, Op. 35 Fryderyka Chopina. (pogrzeb)"""
PUNCHLINE: Tuple[str, ...]
"""Melodia: zabawny fragment oznaczający, że zażartowano."""
PYTHON: Tuple[str, ...]
"""Melodia: Marsz John Philip Sousa „Liberty Bell” aka, motyw „Monty Python Flating Circus” (po którym nazwano język programowania Pythona)."""
BADDY: Tuple[str, ...]
"""Melodia: wejście złego człowieka do ery kina niemego."""
CHASE: Tuple[str, ...]
"""Melodia: scena pościgu z epoki kina niemego."""
BA_DING: Tuple[str, ...]
"""Melodia: krótki sygnał informujący, że coś się wydarzyło."""
WAWAWAWAA: Tuple[str, ...]
"""Melodia: bardzo smutny puzon."""
JUMP_UP: Tuple[str, ...]
"""Melodia: do użytku w grze, wskazujący ruch w górę."""
JUMP_DOWN: Tuple[str, ...]
"""Melodia: do użytku w grze, wskazujący ruch w górę."""
POWER_UP: Tuple[str, ...]
"""Melodia: fanfara oznaczająca odblokowanie osiągnięcia."""
POWER_DOWN: Tuple[str, ...]
"""Melodia: smutna fanfara oznaczająca utracenie osiągnięcia."""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Ustawia przybliżone tempo dla odtwarzania.

Example: ``music.set_tempo(bpm=120)``

:param ticks: Liczba taktów składających się na uderzenie.
:param bpm: Liczba całkowita określająca liczbę uderzeń na minutę.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Pobiera bieżące tempo jako parę liczb całkowitych: ``(ticks, bpm)``.

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Odtwarzaj muzykę.

Example: ``music.play(music.NYAN)``

:param music: muzyka określona w `specjalnej notacji <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_
:param pin: pin wyjściowy do użycia z zewnętrznym głośnikiem (domyślnie ``pin0``), ``None`` dla braku dźwięku.
:param wait: Jeśli ``wait`` jest ustawiony na ``True``, ta funkcja jest blokowana.
:param loop: Jeśli ``loop`` jest ustawiony na ``True``, melodia powtarza się, aż ``stop`` jest wywołana lub połączenie blokujące zostanie przerwane.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Zagraj nutę.

Example: ``music.pitch(185, 1000)``

:param frequency: Częstotliwość całkowitoliczbowa
:param duration: Czas trwania w milisekundach. Jeśli ujemny, to dźwięk jest ciągły aż do następnego połączenia lub połączenia z ``stop``.
:param pin: Opcjonalny pin wyjściowy (domyślny ``pin0``).
:param wait: Jeśli ``wait`` jest ustawiony na ``True``, ta funkcja jest blokowana.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Zatrzymuje odtwarzanie muzyki na wbudowanym głośniku i jakimkolwiek pinie wyjściowym dźwięku.

Example: ``music.stop()``

:param pin: Opcjonalny argument może być podany do określenia pinu, np. ``music.stop(pin1)``."""

def reset() -> None:
    """Resetuje takty, bpm, czas trwania i oktawę do ich wartości domyślnych.

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...