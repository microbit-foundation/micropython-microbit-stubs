"""Meet de versnelling van de micro:bit en herken gebaren. (acceleratiemeter)"""
from typing import Tuple

def get_x() -> int:
    """Krijg de acceleratiemeting in de ``x`` as in milli-g. (krijg x)

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Krijg de acceleratiemeting in de ``y`` as in milli-g. (krijg y)

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Krijg de acceleratiemeter meting in de ``z`` as in milli-g. (krijg z)

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Verkrijg de acceleratiemeter metingen in alle assen tegelijk als een tupel. (krijg waarden)

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Krijg de versnelling meting van alle assen gecombineerd, als een positief getal. Dit is de Pythagorische som van de X, Y en Z assen. (krijg sterkte)

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """Verkrijg de naam van het huidige gebaar. (huidig gebaar)

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Controleer of het benoemde gebaar momenteel actief is. (is gebaren)

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (naam) De naam van het gebaar.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Controleer of het benoemde gebaar actief was sinds het laatste gesprek. (was gebaren)

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (naam) De naam van het gebaar.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Geeft als resultaat een reeks van de gebaren geschiedenis. (verkrijg gebaren)

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Stel het gevoeligheidsbereik van de acceleratiemeter, in g (standaard zwaartekracht), in op de dichtstbijzijnde waarden die door de hardware worden ondersteund, zodat het wordt afgerond op ``2``, ``4`` of ``8`` g. (kies bereik)

Example: ``accelerometer.set_range(8)``

:param value: (waarde) Nieuwe bereik voor de acceleratiemeter, een geheel getal in ``g``."""