"""Töne mit dem micro:bit abspielen (Importiere ``audio`` für V1-Kompatibilität). (Audio)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Wiedergeben eines eingebauten Sounds, Soundeffekts oder benutzerdefinierten Aufnahme .

Example: ``audio.play(Sound.GIGGLE)``

:param source: (Quelle) Ein eingebauter ``Sound`` wie ``Sound.GIGGLE``, ein ``SoundEffect`` oder Beispieldaten als Teil eines ``AudioFrame`` Objekts.
:param wait: Wenn ``wait`` ``True`` ist, wird diese Funktion blockiert, bis der Klang abgeschlossen ist.
:param pin: Ein optionales Argument für den Ausgabepin kann angegeben werden, um die Standardeinstellung von ``pin0``zu überschreiben. Wenn kein Ton wiedergegeben werden soll, kann ``pin=None`` verwendet werden.
:param return_pin: Bestimmt einen Pin, mit dem der externen Lautsprecher anstatt mit Ground verbunden wird. Dies wird bei der **V2** Revision ignoriert."""

def is_playing() -> bool:
    """Überprüft, ob ein Ton abgespielt wird. (spielt gerade)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Stoppt jede Audio-Wiedergabe. (Stop)

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Ein Soundeffekt, zusammengestellt aus einer Reihe von Parametern, die über den Konstruktor oder durch Attribute konfiguriert werden."""
    WAVEFORM_SINE: ClassVar[int]
    """Sinuswelle als Parameter für ``waveform``. (Sinuswelle)"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Sägezahnkurve als Parameter für ``waveform``. (Sägezahnkurve)"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """Dreiecksignal als Parameter für ``waveform``. (Dreiecksignal)"""
    WAVEFORM_SQUARE: ClassVar[int]
    """Rechtecksignal als Parameter für ``waveform``. (Rechtecksignal)"""
    WAVEFORM_NOISE: ClassVar[int]
    """Rauschsignal als Parameter für ``waveform``. (Rauschsignal)"""
    SHAPE_LINEAR: ClassVar[int]
    """Lineare Interpolation als Parameter für ``shape``. (lineare Interpolation)"""
    SHAPE_CURVE: ClassVar[int]
    """Kurven-Interpolation als Parameter für ``shape``. (geschwungene Kurve)"""
    SHAPE_LOG: ClassVar[int]
    """Logarithmische Interpolation als Parameter für ``shape``. (logarithmische Interpolation)"""
    FX_NONE: ClassVar[int]
    """Kein Effekt für ``fx`` verwendet. (kein fx)"""
    FX_TREMOLO: ClassVar[int]
    """Tremelo-Effekt als Parameter für ``fx``. (fx Tremolo)"""
    FX_VIBRATO: ClassVar[int]
    """Vibrato-Effekt als Parameter für ``fx``. (fx Vibrato)"""
    FX_WARBLE: ClassVar[int]
    """Triller-Effekt als Parameter für ``fx``. (fx Trillereffekt)"""
    freq_start: int
    """Startfrequenz in Hertz (Hz), eine Zahl zwischen ``0`` und ``9999`` (Startfrequenz)"""
    freq_end: int
    """Endfrequenz in Hertz (Hz), eine Zahl zwischen ``0`` und ``9999`` (Endfrequenz)"""
    duration: int
    """Dauer des Klangs in Millisekunden, eine Zahl zwischen ``0`` und ``9999`` (Dauer)"""
    vol_start: int
    """Startlautstärke, eine Zahl zwischen ``0`` und ``255`` (vol Start)"""
    vol_end: int
    """Endlautstärke, eine Nummer zwischen ``0`` und ``255`` (vol Ende)"""
    waveform: int
    """Typ der Sinuswelle, einer dieser Werte: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (zufällig generiertes Geräusch)"""
    fx: int
    """Effekt, der dem Sound hinzugefügt werden soll. Mögliche Werte: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE`` oder ``FX_NONE``"""
    shape: int
    """Die Art der Interpolationskurve zwischen der Anfangs- und der Endfrequenz. Verschiedene Wellenformen haben unterschiedliche Frequenzänderungsraten. In Frage kommende Werte: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Erstellt einen neuen Soundeffekt.

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: (Startfrequenz) Startfrequenz in Hertz (Hz), eine Zahl zwischen ``0`` und ``9999``.
:param freq_end: (Endfrequenz) Endfrequenz in Hertz (Hz), eine Zahl zwischen ``0`` und ``9999``.
:param duration: (Dauer) Dauer des Tons in Millisekunden, eine Zahl zwischen ``0`` und ``9999``.
:param vol_start: (vol Start) Startlautstärke, eine Zahl zwischen ``0`` und ``255``.
:param vol_end: (vol Ende) Endlautstärke, eine Nummer zwischen ``0`` und ``255``.
:param waveform: Typ der Sinuswelle, einer dieser Werte: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (zufällig generiertes Geräusch).
:param fx: Effekt, der dem Sound hinzugefügt werden soll, in Frage kommende Werte: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, oder ``FX_NONE``.
:param shape: Die Art der Interpolationskurve zwischen der Anfangs- und der Endfrequenz. Verschiedene Wellenformen haben unterschiedliche Frequenzänderungsraten. In Frage kommende Werte: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Erstellt eine Kopie dieses ``SoundEffect``. (kopieren)

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Ein ``AudioFrame``-Objekt ist eine Liste von 32 Samples, von denen jedes ein vorzeichenloses Byte ist 
(ganze Zahl zwischen 0 und 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Überschreibt die Daten in diesem ``AudioFrame`` mit den Daten einer anderen ``AudioFrame``-Instanz.

Example: ``my_frame.copyfrom(source_frame)``

:param other: ``AudioFrame`` Instanz von der die Daten kopiert werden sollen."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...