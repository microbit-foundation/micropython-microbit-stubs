"""測量 micro:bit 的加速度並識別手勢。 (加速度感測器)"""
from typing import Tuple

def get_x() -> int:
    """取得 ``x`` 軸上的加速度測量值（以毫克為單位）。 (取得 x)

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """取得 ``y`` 軸上的加速度測量值（以毫克為單位）。 (取得 y)

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """取得 ``z`` 軸上的加速度測量值（以毫克為單位）。 (取得 z)

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """一次獲取所有軸上的加速度測量值作為元組。 (取得數值)

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def current_gesture() -> str:
    """取得目前手勢的名稱。 (目前手勢)

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """檢查命名手勢當前是否處於活動狀態。 (is 手勢)

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (名稱) 手勢名稱
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """檢查命名手勢自上次通話後是否處於活動狀態。 (was 手勢)

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (名稱) 手勢名稱
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """傳回手勢歷史紀錄的元組。 (取得手勢)

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...