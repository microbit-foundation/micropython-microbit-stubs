"""Jouer des sons en utilisant le micro:bit (importer ``audio`` pour compatibilité V1). (audio)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Jouer un son intégré ou des frames audio personnalisées. (play)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (source) Un ``son`` intégré tel que ``Sound.GIGGLE`` ou un échantillon de données en tant qu'itérable d'objets ``AudioFrame``.
:param wait: (wait) Si ``wait`` est ``True``, cette fonction bloquera jusqu'à ce que le son soit terminé.
:param pin: (broche) Un argument optionnel pour spécifier la broche de sortie, peut être utilisé pour remplacer la valeur par défaut ``pin0``. Si nous ne voulons pas que le son soit joué, il est possible d'utiliser ``pin=None``.
:param return_pin: (return pin) Spécifie une broche de connecteur de bord différentiel à connecter à un haut-parleur externe au lieu de la masse. Ceci est ignoré dans la révision **V2**."""

def is_playing() -> bool:
    """Vérifier si un son est en train d'être joué. (is playing)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Arrêter toute lecture audio. (stop)

Example: ``audio.stop()``"""
    ...

class AudioFrame:
    """Un objet ``AudioFrame`` est une liste de 32 échantillons, chacun d'eux étant un octet non signé
(nombre entier entre 0 et 255). (audioframe)

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...