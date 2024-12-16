"""Zmierz przyspieszenie micro:bita i rozpoznawaj gesty."""
from typing import Tuple

def get_x() -> int:
    """Uzyskaj pomiar przyspieszenia na osi ``x`` w mili-g.

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Uzyskaj pomiar przyspieszenia na osi ``y`` w mili-g.

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Uzyskaj pomiar przyspieszenia na osi ``z`` w mili-g.

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Uzyskaj pomiary przyspieszenia na wszystkich osiach jednocześnie, jako krotkę.

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Uzyskaj pomiar przyspieszenia wszystkich osi łącznie jako dodatnią liczbę całkowitą. Jest to suma pitagorejska osi X, Y i Z.

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """Pobierz nazwę aktualnego gestu.

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Sprawdź, czy nazwany gest jest aktualnie aktywny.

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: Nazwa gestu.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Sprawdź, czy nazwany gest był aktywny od ostatniego połączenia.

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: Nazwa gestu.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Zwróć krotkę historii gestów.

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Ustaw zakres czułości akcelerometru w g (standardowa grawitacja) na najbliższe wartości obsługiwane przez sprzęt tak, aby zaokrąglał się do ``2``, ``4`` lub ``8`` g.

Example: ``accelerometer.set_range(8)``

:param value: Nowy zakres dla akcelerometru, liczba całkowita w ``g``."""