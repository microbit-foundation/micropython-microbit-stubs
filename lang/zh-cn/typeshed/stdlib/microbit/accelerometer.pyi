"""测量 micro:bit 的加速度并识别手势。 (加速度传感器)"""
from typing import Tuple

def get_x() -> int:
    """获取 ``x`` 轴上的加速度测量值（以 milli-g 为单位）。

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """获取 ``y`` 轴上的加速度测量值（以 milli-g 为单位）。

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """获取 ``z`` 轴上的加速度测量值（以 milli-g 为单位）。

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """一次获取所有轴上的加速度测量值作为元组。

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """以正整数形式获取所有轴组合的加速度测量值。这是 X、Y 和 Z 轴的毕达哥拉斯（Pythagorean）和。 (获取强度)

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """获取当前手势的名称。

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """检查命名手势当前是否处于活动状态。

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: 手势名称。
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """检查命名手势自上次调用后是否处于活动状态。

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: 手势名称。
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """返回手势历史的元组。

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """将加速度计灵敏度范围（以 g（标准重力）为单位）设置为硬件支持的最接近的值，因此它会取近似值为 ``2``、``4`` 或 ``8`` g。 (设置范围)

Example: ``accelerometer.set_range(8)``

:param value: 加速度计的新范围，``g`` 中的整数。"""