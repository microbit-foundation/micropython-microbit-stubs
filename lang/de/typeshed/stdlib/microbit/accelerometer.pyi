"""Messen Sie die Beschleunigung des micro:bit und erkennen Sie Gesten. (Beschleunigungssensor)"""
from typing import Tuple

def get_x() -> int:
    """Erhalte die Beschleunigungsmessung in der ``x`` -Achse in Milli-g.

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Erhalte die Beschleunigungsmessung in der ``y`` -Achse in Milli-g.

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Erhalte die Beschleunigungsmessung in der ``z`` -Achse in Milli-g.

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Erhalte die Beschleunigungsmessung in allen Achsen auf einmal als Tupel.

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Erhalte die Beschleunigungsmessung aller Achsen als positive Ganzzahl. Dies ist die euklidische Summe der x-, y- und z-Achsen.

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """Erhalte den Namen der aktuellen Geste. (derzeitige Geste)

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Überprüft, ob die benannte Geste derzeit aktiv ist. (ist Geste)

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: Der Name der Geste.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Überprüft, ob die benannte Geste seit dem letzten Aufruf aktiv war. (war Geste)

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: Der Name der Geste.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Gibt ein Tupel der vergangenen Gesten zurück.

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Legt den Bereich des Beschleunigungsmessers in g (Fallbeschleunigung) auf den nächstgelegenen Wert fest, welcher von der Hardware unterstützt wird. Diese sind ``2``, ``4``oder ``8`` g. (Bereich einstellen)

Example: ``accelerometer.set_range(8)``

:param value: (wert) Neuer Bereich für den Beschleunigungssensor, eine Ganzzahl in ``g``."""