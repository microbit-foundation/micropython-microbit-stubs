"""Reprodueix sons amb la micro:bit (importa ``audio`` per a la compatibilitat amb V1). (àudio)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Reprodueix un so incorporat, un efecte de só o marcs d'àudio personalitzats.

Example: ``audio.play(Sound.GIGGLE)``

:param source: (origen) Un objecte de ``Sound`` incorporat com ``Sound.GIGGLE``, un ``SoundEffect`` o una data de mostra com un iterable de ``AudioFrame`` .
:param wait: (espera) Si ``wait`` és ``True``, aquesta funció es bloquejarà fins que s'acabi el so.
:param pin: Es pot utilitzar un argument opcional per especificar el pin de sortida per anul·lar el valor predeterminat de ``pin0``. Si no vols que es reprodueixi cap so, pots utilitzar ``pin=None``.
:param return_pin: (retorna el pin) Especifica un pin diferent del connector d'expansió per connectar-lo a un altaveu extern en lloc de posar a terra. Això s'ignora per a la revisió **V2**."""

def is_playing() -> bool:
    """Verifica si s'està reproduint un so. (està reproduint)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Atura tota la reproducció d'àudio. (atura)

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Un efecte sonor, compost per un conjunt de paràmetres configurats via el constructor o atributs."""
    WAVEFORM_SINE: ClassVar[int]
    """Opció d'ona sinusoidal pel paràmetre ``waveform``. (forma d'ona sinusoidal)"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Opció d'ona de dent de serra pel paràmetre ``waveform``. (forma d'ona de dent de serra)"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """Opció d'ona triangular pel paràmetre ``waveform``. (forma d'ona triangular)"""
    WAVEFORM_SQUARE: ClassVar[int]
    """Opció d'ona quadrada pel paràmetre ``waveform``. (forma d'ona quadrada)"""
    WAVEFORM_NOISE: ClassVar[int]
    """Opció d'ona de soroll pel paràmetre ``waveform``. (forma d'ona de soroll)"""
    SHAPE_LINEAR: ClassVar[int]
    """Opció d'ona lineal pel paràmetre ``shape``. (forma lineal)"""
    SHAPE_CURVE: ClassVar[int]
    """Opció d'interpolació de corba usada pel paràmetre ``shape``. (forma de corba)"""
    SHAPE_LOG: ClassVar[int]
    """Opció d'interpolació logarítmica utilitzada pel paràmetre ``shape``. (forma logarítmica)"""
    FX_NONE: ClassVar[int]
    """Opció de cap efecte utilitzat pel paràmetre ``fx``. (fx cap)"""
    FX_TREMOLO: ClassVar[int]
    """Opció d'efecte trèmolo utilitzat pel paràmetre ``fx``. (fx trémolo)"""
    FX_VIBRATO: ClassVar[int]
    """Opció d'efecte vibrato utilitzat pel paràmetre ``fx``."""
    FX_WARBLE: ClassVar[int]
    """Opció d'efecte gorjeu utilitzat pel paràmetre ``fx``. (Efecte gorjeu)"""
    freq_start: int
    """Freqüència inicial en Hertz (Hz), un nombre entre ``0`` i ``9999`` (freqüència inicial)"""
    freq_end: int
    """Freqüència final en Hertz (Hz), un nombre entre ``0`` i ``9999`` (frequència final)"""
    duration: int
    """Durada del so en mil·lisegons, un nombre entre ``0`` and ``9999`` (Durada - duració)"""
    vol_start: int
    """Volum inicial, un nombre entre ``0`` and ``255`` (volum inicial)"""
    vol_end: int
    """Valor del volum final, un nombre entre ``0`` and ``255`` (volum final)"""
    waveform: int
    """Tipus de forma d'ona, un d'aquest valors: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (randomly generated noise) (forma d'ona)"""
    fx: int
    """Efecte a afegir al so, un dels següents valors: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, or ``FX_NONE`` (efecte)"""
    shape: int
    """El tipus de corba d'interpolació entre les freqüències inicial i final, diferents formes d'ona tenen diferents ràtios de canvi en la freqüència. Un dels següents valors: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG`` (forma)"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Crea un efecte de so nou. (inicial)

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: (freqüència inicial) Freqüència inicial en Hertz (Hz), un nombre entre ``0`` i ``9999``.
:param freq_end: (frequència final) Freqüència final en Hertz (Hz), un nombre entre ``0`` i ``9999``.
:param duration: (Durada - duració) Duració del so en mil·lisegons, un nombre entre ``0`` i ``9999``.
:param vol_start: (volum inicial) Valor del volum inicial, un nombre entre ``0`` i ``255``.
:param vol_end: (volum final) Valor del volum final, un nombre entre ``0`` i ``255``.
:param waveform: (forma d'ona) Tipus de forma d'ona, un d'aquests valors: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (soroll generat aleatòriament).
:param fx: (efecte) Efecte a afegir al so, un del següents valors: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, or ``FX_NONE``.
:param shape: (forma) El tipus de corba d'interpolació entre les freqüències inicial i final, diferents formes d'ona tenen diferents ràtios de canvi en la freqüència. Un dels següents valors: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``"""

    def copy(self) -> SoundEffect:
        """Crea una còpia d'aquest ``SoundEffect``. (còpia)

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Un objecte ``AudioFrame`` és una llista de 32 mostres cadascuna de les quals és un byte sense signar
(nombre enter entre 0 i 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Sobreposa les dades d'aquest ``AudioFrame`` amb les dades d'una altra instància ``AudioFrame`` . (copia desde)

Example: ``my_frame.copyfrom(source_frame)``

:param other: (altre) ``AudioFrame`` instància de la qual copiar les dades."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...