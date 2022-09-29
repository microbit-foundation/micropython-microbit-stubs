"""micro:bitの加速度測定とジェスチャー認識をします。"""
from typing import Tuple

def get_x() -> int:
    """``x`` 軸の加速度測定値をミリg単位で取得します。

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """``y`` 軸の加速度測定値をミリg単位で取得します。

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """``z`` 軸の加速度測定値をミリg単位で取得します。

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """すべての軸の加速度測定値をタプルとして一度に取得します。

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """すべての軸を合成した加速度測定値を正の整数値で得ます。これは X軸、Y軸、Z軸のピタゴラス和になります。

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """現在のジェスチャーの名前を取得します。

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """指定した名前のジェスチャーが現在アクティブであるかどうかを確認します。

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: ジェスチャー名。
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """直前の呼び出し以降に、指定した名前のジェスチャーがアクティブになったかどうかを確認します。

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: ジェスチャー名。
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """ジェスチャー履歴のタプルを返します。

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """加速度センサーの感度範囲を g (標準重力)で設定します。設定値は、ハードウェアがサポートする最も近い値、すなわち ``2``、``4``、``8`` g のいずれかに丸められます。

Example: ``accelerometer.set_range(8)``

:param value: 加速度センサーの新しい感度範囲。``g`` 単位の整数値で指定します。"""