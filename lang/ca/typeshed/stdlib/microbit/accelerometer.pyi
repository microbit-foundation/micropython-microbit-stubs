"""Mesura l'acceleració de la micro:bit i reconeix els gestos. (acceleròmetre)"""
from typing import Tuple

def get_x() -> int:
    """Obté la mesura de l'acceleració a l'eix ``x`` en mili-g. (obté x)

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Obté la mesura de l'acceleració a l'eix ``y`` en mili-g. (obté y)

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Obté la mesura de l'acceleració a l'eix ``z`` en mili-g. (obté z)

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Obté les mesures d'acceleració en tots els eixos alhora com una tupla. (obté valors)

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Obté la mesura de l'acceleració de tots els eixos combinats, com un nombre enter positiu. Aquest serà la suma Pitagòrica dels eixos X, Y i Z. (obté la força)

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """Obté el nom del gest actual. (El gest actual)

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Comprova si el gest nomenat està actiu actualment.

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (nom) El nom del gest
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Comprova si el gest nomenat ha estat actiu des de l'última crida.

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (nom) El nom del gest
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Retorna una tupla de l'historial de gestos. (obté gestos)

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Estableix l'interval de la sensibilitat de l'acceleròmetre, en g (gravetat estàndard), al valor més proper acceptat pel maquinari, arrodonit a ``2``, ``4``, o ``8``

Example: ``accelerometer.set_range(8)``

:param value: (valor) Nou interval per a l'acceleròmetre, un nombre enter a ``g``."""