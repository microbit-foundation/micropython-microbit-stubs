"""Créer et jouer des mélodies."""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Mélodie : l'ouverture de la 5e symphonie en do mineur de Beethoven."""
ENTERTAINER: Tuple[str, ...]
"""Mélodie : le fragment d'ouverture du classique de ragtime "The Entertainer" de Scott Joplin."""
PRELUDE: Tuple[str, ...]
"""Mélodie : le prélude et fugue en ut majeur (BWV 846) de Jean-Sébastien Bach."""
ODE: Tuple[str, ...]
"""Mélodie : le thème de l'"Ode à la joie" de la 9e symphonie en ré mineur de Beethoven."""
NYAN: Tuple[str, ...]
"""Mélodie : le thème de Nyan Cat (http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Mélodie : son qui ressemble à une sonnerie de téléphone mobile.

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Mélodie : une ligne de basse funky pour les agents secrets et les cerveaux criminels."""
BLUES: Tuple[str, ...]
"""Mélodie : une walking bass blues de boogie-woogie à 12 mesures."""
BIRTHDAY: Tuple[str, ...]
"""Mélodie : « Joyeux anniversaire…»

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Mélodie : la marche nuptiale de l'opéra "Lohengrin" de Wagner."""
FUNERAL: Tuple[str, ...]
"""Mélodie : la "marche funèbre " aussi connue sous le nom de Sonate pour piano n° 2 en B♭ mineur, opus 35 de Frédéric Chopin."""
PUNCHLINE: Tuple[str, ...]
"""Mélodie : un extrait amusant qui signifie qu'une blague a été faite."""
PYTHON: Tuple[str, ...]
"""Mélodie : La marche "Liberty Bell" de John Philip Sousa, alias le thème du "Monty Python's Flying Circus" (qui a donné son nom au langage de programmation Python)."""
BADDY: Tuple[str, ...]
"""Mélodie\xa0: entrée d'un méchant à l'époque des films muets."""
CHASE: Tuple[str, ...]
"""Mélodie : scène de poursuite à l'époque du film muet."""
BA_DING: Tuple[str, ...]
"""Mélodie : un signal court pour indiquer que quelque chose s'est produit."""
WAWAWAWAA: Tuple[str, ...]
"""Mélodie : un trombone très triste."""
JUMP_UP: Tuple[str, ...]
"""Mélodie\xa0: pour une utilisation dans un jeu, indiquant un mouvement vers le haut."""
JUMP_DOWN: Tuple[str, ...]
"""Mélodie\xa0: pour une utilisation dans un jeu, indiquant un mouvement vers le bas."""
POWER_UP: Tuple[str, ...]
"""Mélodie : une fanfare pour indiquer un succès débloqué."""
POWER_DOWN: Tuple[str, ...]
"""Mélodie : une fanfare triste pour indiquer un succès manqué."""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Définir le tempo approximatif pour la lecture.

Example: ``music.set_tempo(bpm=120)``

:param ticks: Le nombre de ticks constituant un battement.
:param bpm: Un entier déterminant le nombre de battements par minute.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Récupérer le tempo actuel sous la forme d'un tuple d'entiers : ``(ticks, bpm)``.

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Jouer de la musique.

Example: ``music.play(music.NYAN)``

:param music: musique spécifiée dans `une notation spéciale <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_
:param pin: (broche) la broche de sortie à utiliser avec un haut-parleur externe (par défaut ``pin0``), ``None`` pour aucun son.
:param wait: Si ``wait`` est défini à ``True``, cette fonction est bloquante.
:param loop: Si ``loop`` est défini à ``True``, la mélodie se répète jusqu'à ce que ``stop`` soit appelé, ou que l'appel bloquant soit interrompu.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Jouer une note. (tangage)

Example: ``music.pitch(185, 1000)``

:param frequency: (fréquence) Une fréquence entière
:param duration: Une durée en milliseconde. Si la valeur est négative alors le son sera continu jusqu'au prochain appel, ou jusqu'à un appel à ``stop``.
:param pin: (broche) Broche de sortie optionnelle (par défaut ``pin0``).
:param wait: Si ``wait`` est défini à ``True``, cette fonction est bloquante.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Met fin à toute lecture de musique sur le haut-parleur intégré et à tout son en sortie sur la broche.

Example: ``music.stop()``

:param pin: (broche) Un argument optionnel peut être spécifié pour indiquer une broche, par exemple ``music.stop(pin1)``."""

def reset() -> None:
    """Réinitialiser les ticks, bpm, durée et octave à leurs valeurs par défaut.

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...