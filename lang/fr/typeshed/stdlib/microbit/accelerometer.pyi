"""Mesurer l'accélération du micro:bit et reconnaitre des mouvements."""
from typing import Tuple

def get_x() -> int:
    """Récupérer la mesure de l'accélération dans l'axe ``x`` en milli-g.

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Récupérer la mesure de l'accélération dans l'axe ``y`` en milli-g.

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Récupérer la mesure de l'accélération dans l'axe ``z`` en milli-g.

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Récupérer en une fois les mesures d'accélération dans tous les axes sous forme d'un tuple.

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Obtenir la mesure de l'accélération de tous les axes combinés, sous la forme d'un nombre entier positif. C'est la somme pythagoricienne des axes X, Y et Z.

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """Récupérer le nom du geste actuel.

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Vérifier si le geste nommé est actif en ce moment.

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: Le nom du geste.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Vérifier si le geste nommé a été actif depuis le dernier appel.

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: Le nom du geste.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Renvoyer un tuple de l'historique des gestes.

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Définir la plage de sensibilité de l'accéléromètre, en g (gravité standard), à la valeur la plus proche supportée par le matériel, l'arrondi se fait soit à ``2``, ``4``, ou ``8`` g.

Example: ``accelerometer.set_range(8)``

:param value: Nouvelle plage pour l'accéléromètre, un entier en ``g``."""