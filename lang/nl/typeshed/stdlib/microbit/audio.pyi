"""Geluid afspelen met behulp van de micro:bit (importeer ``audio`` voor V1 compatibiliteit)."""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Een ingebouwde geluid, geluids effect of aangepaste audio frames afspelen. (afspelen)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (bron) Een ingebouwde ``Sound`` zoals ``Sound.GIGGLE``, een ``SoundEffect`` of voorbeeldgegevens als een iteratie van ``AudioFrame`` objecten.
:param wait: (wacht) Als ``wait`` ``True``is, wordt deze functie geblokkeerd totdat het geluid is voltooid.
:param pin: Een optioneel argument om de uitvoerpin op te geven kan worden gebruikt om de standaard van ``pin0``te overschrijven. Als we geen geluid willen afspelen, kunnen we ``pin=None`` gebruiken.
:param return_pin: (retourneer pin) Specificeert een differentiële rand connector pin om verbinding te maken met een externe luidspreker in plaats van de grond. Dit wordt genegeerd voor de **V2** herziening."""

def is_playing() -> bool:
    """Controleer of een geluid wordt gespeeld. (speelt af)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Stop het afspelen van de audio.

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Een geluidseffect, bestaande uit een set parameters geconfigureerd via de constructor of attributen."""
    WAVEFORM_SINE: ClassVar[int]
    """De sinusgolf optie gebruikt voor de ``waveform`` parameter. (golfvorm sinus)"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Zaag golf optie gebruikt voor de ``waveform`` parameter. (golfvorm zaagtand)"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """De drie hoeks golf optie gebruikt voor de ``waveform`` parameter. (golfvorm driehoek)"""
    WAVEFORM_SQUARE: ClassVar[int]
    """Blok golf optie die wordt gebruikt voor de parameter ``waveform``. (golfvorm vierkant)"""
    WAVEFORM_NOISE: ClassVar[int]
    """Noise optie gebruikt voor de ``waveform`` parameter. (golfvormig geluid)"""
    SHAPE_LINEAR: ClassVar[int]
    """Lineaire interpolatie optie die wordt gebruikt voor de ``shape`` parameter. (vorm lineair)"""
    SHAPE_CURVE: ClassVar[int]
    """Curve interpolatie optie gebruikt voor de ``shape`` parameter. (vorm curve)"""
    SHAPE_LOG: ClassVar[int]
    """Logaritmische interpolatie optie gebruikt voor de ``shape`` parameter. (vorm log)"""
    FX_NONE: ClassVar[int]
    """Geen effectoptie gebruikt voor de  ``fx`` parameter. (geen fx)"""
    FX_TREMOLO: ClassVar[int]
    """Tremolo effect optie die wordt gebruikt voor de ``fx`` parameter."""
    FX_VIBRATO: ClassVar[int]
    """Vibrato effect optie die wordt gebruikt voor de ``fx`` parameter."""
    FX_WARBLE: ClassVar[int]
    """Warble effect optie die wordt gebruikt voor de ``fx`` parameter ."""
    freq_start: int
    """Start frequentie in Hertz (Hz), een getal tussen ``0`` en ``9999`` (frequentie start)"""
    freq_end: int
    """Eind frequentie in Hertz (Hz), een getal tussen ``0`` en ``9999`` (frequentie einde)"""
    duration: int
    """Duur van het geluid in milliseconden, een getal tussen ``0`` en ``9999`` (Duur)"""
    vol_start: int
    """Start volume waarde, een getal tussen ``0`` en ``255``"""
    vol_end: int
    """Eind volume waarde, een getal tussen ``0`` en ``255`` (vol einde)"""
    waveform: int
    """Type van golfvorm, één van deze waarden: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (willekeurig gegenereerde lawaai) (golfvorm)"""
    fx: int
    """Effect om aan het geluid toe te voegen, een van de volgende waarden: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``of ``FX_NONE``"""
    shape: int
    """Het type van de interpolatie curve tussen de begin- en eind frequenties, verschillende golfvormen hebben verschillende snelheid bij het wijzigen van de frequentie. Een van de volgende waarden: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG`` (vorm)"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Maak een nieuw geluidseffect. (initialiseren)

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: (frequentie start) Start frequentie in Hertz (Hz), een getal tussen ``0`` en ``9999``.
:param freq_end: (frequentie einde) Eind frequentie in Hertz (Hz), een getal tussen ``0`` en ``9999``.
:param duration: (duur) Duur van het geluid in milliseconden, een getal tussen ``0`` en ``9999``.
:param vol_start: Startvolumewaarde, een getal tussen ``0`` en ``255``.
:param vol_end: (vol einde) Eindvolumewaarde, een getal tussen ``0`` en ``255``.
:param waveform: (golfvorm) Type golfvorm, één van deze waarden: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (willekeurig gegenereerde geluid).
:param fx: Effect om het geluid toe te voegen, een van de volgende waarden: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``of ``FX_NONE``.
:param shape: (vorm) Het type van de interpolatie curve tussen de begin- en eind frequenties, verschillende golfvormen hebben verschillende snelheid bij het wijzigen van de frequentie. Een van de volgende waarden: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Maak een kopie van dit ``SoundEffect``. (kopiëer)

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Een ``AudioFrame`` object is een lijst van 32 samples elk een niet-ondertekende byte
(geheel getal tussen 0 en 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Overschrijf de gegevens in deze ``AudioFrame`` met de gegevens van een andere ``AudioFrame`` instantie. (kopieer van)

Example: ``my_frame.copyfrom(source_frame)``

:param other: (overige) ``AudioFrame`` exemplaar van waar de gegevens worden gekopieerd."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...