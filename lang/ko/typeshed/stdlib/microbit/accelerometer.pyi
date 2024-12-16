"""micro:bit의 가속도를 측정하고 제스쳐를 인식합니다."""
from typing import Tuple

def get_x() -> int:
    """``x`` 축의 가속도 측정값을 milli-g로 불러옵니다.

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """``y`` 축의 가속도 측정값을 milli-g로 불러옵니다.

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """``z`` 축의 가속도 측정값을 milli-g로 불러옵니다.

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """한 번에 모든 축의 가속도 측정값을 튜플로 불러옵니다.

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Get the acceleration measurement of all axes combined, as a positive integer. This is the Pythagorean sum of the X, Y and Z axes.

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """현재 제스처의 이름을 불러옵니다.

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """해당 이름의 제스처가 현재 활성화 상태인지 확인합니다.

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: 제스쳐 이름.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """해당 이름의 제스처가 마지막 호출 이후로 활성화된 적이 있는지 확인합니다.

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: 제스처 이름입니다.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """제스처 기록의 튜플을 반환합니다.

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