"""Jouer des sons en utilisant le micro:bit (importer ``audio`` pour compatibilité V1)."""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Jouer un son intégré, un effet sonore ou des frames audio personnalisées.

Example: ``audio.play(Sound.GIGGLE)``

:param source: Un ``Sound`` intégré tel que ``Sound.GIGGLE``, un ``SoundEffect`` ou un échantillon de données sous la forme d'un itérable d'objets ``AudioFrame``.
:param wait: Si ``wait`` est ``True``, cette fonction bloquera jusqu'à ce que le son soit terminé.
:param pin: (broche) Un argument optionnel pour spécifier la broche de sortie, peut être utilisé pour remplacer la valeur par défaut ``pin0``. Si nous ne voulons pas que le son soit joué, il est possible d'utiliser ``pin=None``.
:param return_pin: Spécifie une broche de connecteur de bord différentiel à connecter à un haut-parleur externe au lieu de la masse. Ceci est ignoré dans la révision **V2**."""

def is_playing() -> bool:
    """Vérifier si un son est en train d'être joué.

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Arrêter toute lecture audio.

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Un effet sonore, composé d'un ensemble de paramètres configurés via le constructeur ou les attributs."""
    WAVEFORM_SINE: ClassVar[int]
    """Option d'onde sinusoïdale utilisée pour le paramètre ``waveform``."""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Optionde forme d'onde en dent de scie utilisée pour le paramètre ``waveform``."""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """Option d'onde triangulaire utilisée pour le paramètre ``waveform``."""
    WAVEFORM_SQUARE: ClassVar[int]
    """Option d'onde carrée utilisée pour le paramètre ``waveform``."""
    WAVEFORM_NOISE: ClassVar[int]
    """Option d'onde de bruit utilisée pour le paramètre ``waveform``."""
    SHAPE_LINEAR: ClassVar[int]
    """Option d'interpolation linéaire utilisée pour le paramètre ``shape``."""
    SHAPE_CURVE: ClassVar[int]
    """Option d'interpolation courbe utilisée pour le paramètre ``shape``."""
    SHAPE_LOG: ClassVar[int]
    """Option d'interpolation logarithmique utilisée pour le paramètre ``shape``."""
    FX_NONE: ClassVar[int]
    """Option sans effet utilisée pour le paramètre ``fx``."""
    FX_TREMOLO: ClassVar[int]
    """Option d'effet tremolo utilisée pour le paramètre ``fx``."""
    FX_VIBRATO: ClassVar[int]
    """Option d'effet vibrato utilisée pour le paramètre ``fx``."""
    FX_WARBLE: ClassVar[int]
    """Option d'effet de Warble utilisée pour le paramètre ``fx``."""
    freq_start: int
    """Fréquence de départ en Hertz (Hz), un nombre compris entre ``0`` et ``9999``"""
    freq_end: int
    """Fréquence de fin en Hertz (Hz), un nombre compris entre ``0`` et ``9999``"""
    duration: int
    """Durée du son en millisecondes, un nombre compris entre ``0`` et ``9999``"""
    vol_start: int
    """Valeur du volume de départ, un nombre compris entre ``0`` et ``255``"""
    vol_end: int
    """Valeur du volume à la fin, un nombre compris entre ``0`` et ``255``"""
    waveform: int
    """Type de forme d'onde, une de ces valeurs : ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (bruit généré aléatoirement)"""
    fx: int
    """Effet à ajouter au son, l'une des valeurs suivantes : ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, ou ``FX_NONE``"""
    shape: int
    """Le type de la courbe d'interpolation entre les fréquences de début et de fin, les différentes formes d'onde ont des taux de variation de fréquence différents. L'une des valeurs suivantes : ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Créer un nouvel effet sonore.

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: Fréquence de départ en Hertz (Hz), un nombre compris entre ``0`` et ``9999``.
:param freq_end: Fréquence de fin en Hertz (Hz), un nombre compris entre ``0`` et ``9999``.
:param duration: Durée du son en millisecondes, un nombre compris entre ``0`` et ``9999``.
:param vol_start: Valeur du volume de départ, un nombre compris entre ``0`` et ``255``.
:param vol_end: Valeur du volume à la fin, un nombre compris entre ``0`` et ``255``.
:param waveform: Type de forme d'onde, une de ces valeurs : ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (bruit généré aléatoirement).
:param fx: Effet à ajouter au son, l'une des valeurs suivantes : ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, ou ``FX_NONE``.
:param shape: Le type de la courbe d'interpolation entre les fréquences de début et de fin, les différentes formes d'onde ont des taux de variation de fréquence différents. L'une des valeurs suivantes : ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Créer une copie de ce ``SoundEffect``.

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Un objet ``AudioFrame`` est une liste de 32 échantillons, chacun d'eux étant un octet non signé
(nombre entier entre 0 et 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Écraser les données de ce ``AudioFrame`` avec les données d'une autre instance ``AudioFrame``.

Example: ``my_frame.copyfrom(source_frame)``

:param other: Instance ``AudioFrame`` à partir de laquelle copier les données."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...