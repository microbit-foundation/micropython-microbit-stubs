"""测量 micro:bit 的加速度并识别手势。 (accelerometer)"""
from typing import Tuple

def get_x() -> int:
    """获取 ``x`` 轴上的加速度测量值（以milli-g为单位）。 (get x)

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """获取 ``y`` 轴上的加速度测量值（以milli-g为单位）。 (get y)

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """获取 ``z`` 轴上的加速度测量值（以milli-g为单位）。 (get z)

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """一次获取所有轴上的加速度测量值作为元组。 (get values)

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def current_gesture() -> str:
    """获取当前手势的名称。 (current gesture)

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """检查命名手势当前是否处于活动状态。 (is gesture)

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (name) 手势名称。
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """检查命名手势自上次调用后是否处于活动状态。 (was gesture)

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (name) 手势名称。
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """返回手势历史的元组。 (get gestures)

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...