"""Measure the acceleration of the micro:bit and recognise gestures."""
from typing import Tuple

def get_x() -> int:
    """Get the acceleration measurement in the ``x`` axis in milli-g.

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Get the acceleration measurement in the ``y`` axis in milli-g.

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Get the acceleration measurement in the ``z`` axis in milli-g.

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Get the acceleration measurements in all axes at once as a tuple.

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def current_gesture() -> str:
    """Get the name of the current gesture.

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Check if the named gesture is currently active.

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (name) The gesture name.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Check if the named gesture was active since the last call.

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (name) The gesture name.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Return a tuple of the gesture history.

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...