"""crwdns329920:0crwdne329920:0 (crwdns329918:0crwdne329918:0)"""
from typing import Tuple

def get_x() -> int:
    """crwdns329924:0``x``crwdne329924:0 (crwdns329922:0crwdne329922:0)

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """crwdns329928:0``y``crwdne329928:0 (crwdns329926:0crwdne329926:0)

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """crwdns329932:0``z``crwdne329932:0 (crwdns329930:0crwdne329930:0)

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """crwdns329936:0crwdne329936:0 (crwdns329934:0crwdne329934:0)

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """crwdns335824:0crwdne335824:0 (crwdns335822:0crwdne335822:0)

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """crwdns329940:0crwdne329940:0 (crwdns329938:0crwdne329938:0)

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """crwdns329944:0crwdne329944:0 (crwdns329942:0crwdne329942:0)

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (crwdns329946:0crwdne329946:0) crwdns329948:0crwdne329948:0
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """crwdns329952:0crwdne329952:0 (crwdns329950:0crwdne329950:0)

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (crwdns329954:0crwdne329954:0) crwdns329956:0crwdne329956:0
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """crwdns329960:0crwdne329960:0 (crwdns329958:0crwdne329958:0)

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """crwdns335828:0``2``crwdnd335828:0``4``crwdnd335828:0``8``crwdne335828:0 (crwdns335826:0crwdne335826:0)

Example: ``accelerometer.set_range(8)``

:param value: (crwdns335830:0crwdne335830:0) crwdns335832:0``g``crwdne335832:0"""