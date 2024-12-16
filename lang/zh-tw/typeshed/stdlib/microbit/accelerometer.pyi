"""測量 micro:bit 的加速度並識別手勢。"""
from typing import Tuple

def get_x() -> int:
    """取得 ``x`` 軸上的加速度測量值 (以毫克為單位)。

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """取得 ``y`` 軸上的加速度測量值 (以毫克為單位)。

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """取得 ``z`` 軸上的加速度測量值 (以毫克為單位)。

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """一次取得所有軸上的加速度測量值做為元組。

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Get the acceleration measurement of all axes combined, as a positive integer. This is the Pythagorean sum of the X, Y and Z axes.

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """取得目前手勢的名稱。

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """檢查命名的手勢目前是否處於活動狀態。

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: 手勢名稱。
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """檢查命名手勢自上次呼叫後是否處於活動狀態。

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: 手勢名稱。
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """傳回手勢歷史紀錄的元組。

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Set the accelerometer sensitivity range, in g (standard gravity), to the closest values supported by the hardware, so it rounds to either ``2``, ``4``, or ``8`` g.

Example: ``accelerometer.set_range(8)``

:param value: New range for the accelerometer, an integer in ``g``."""