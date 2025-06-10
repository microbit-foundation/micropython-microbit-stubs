"""Tomhais luasghéarú an micro:bit agus aithin gothaí. (luasmhéadar)"""
from typing import Tuple

def get_x() -> int:
    """Faigh an tomhas luasghéaraithe san ais ``x`` i milli-g. (faigh x)

Example: ``accelerometer.get_x()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_y() -> int:
    """Faigh an tomhas luasghéaraithe san ais ``y`` i milli-g. (faigh y)

Example: ``accelerometer.get_y()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_z() -> int:
    """Faigh an tomhas luasghéaraithe san ais ``z`` i milli-g. (faigh z)

Example: ``accelerometer.get_z()``

:return: A positive or negative integer depending on direction in the range +/- 2000mg."""
    ...

def get_values() -> Tuple[int, int, int]:
    """Faigh na tomhais luasghéaraithe i ngach aiseanna ag an am céanna mar tuple. (faigh luachanna)

Example: ``x, y, z = accelerometer.get_values()``

:return: a three-element tuple of integers ordered as X, Y, Z, each value a positive or negative integer depending on direction in the range +/- 2000mg"""
    ...

def get_strength() -> int:
    """Faigh tomhas luasghéaraithe na n-aiseanna go léir le chéile, mar shlánuimhir dhearfach. Is é seo suim Pythagorean na n-aiseanna X, Y agus Z. (faigh neart)

Example: ``accelerometer.get_strength()``

:return: The combined acceleration strength of all the axes, in milli-g."""
    ...

def current_gesture() -> str:
    """Faigh ainm an chomhartha reatha. (gotha \u200b\u200breatha)

Example: ``accelerometer.current_gesture()``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:return: The current gesture"""
    ...

def is_gesture(name: str) -> bool:
    """Seiceáil an bhfuil an comhartha ainmnithe gníomhach faoi láthair. (is gotha)

Example: ``accelerometer.is_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (ainm) An t-ainm gotha.
:return: ``True`` if the gesture is active, ``False`` otherwise."""
    ...

def was_gesture(name: str) -> bool:
    """Seiceáil an raibh an comhartha ainmnithe gníomhach ón nglao deireanach. (bhí gotha)

Example: ``accelerometer.was_gesture('shake')``

MicroPython understands the following gesture names: ``"up"``, ``"down"``,
``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``,
``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``. Gestures are always
represented as strings.

:param name: (ainm) Ainm an ghluaiseachta.
:return: ``True`` if the gesture was active since the last call, ``False`` otherwise."""

def get_gestures() -> Tuple[str, ...]:
    """Tabhair ar ais tuple de stair na gothaí. (faigh gothaí)

Example: ``accelerometer.get_gestures()``

Clears the gesture history before returning.

Gestures are not updated in the background so there needs to be constant
calls to some accelerometer method to do the gesture detection. Usually
gestures can be detected using a loop with a small :func:`microbit.sleep` delay.

:return: The history as a tuple, most recent last."""
    ...

def set_range(value: int) -> None:
    """Socraigh an raon íogaireachta luasmhéadair, i g (domhantarraingt chaighdeánach), go dtí na luachanna is gaire a dtacaíonn na crua-earraí leo, agus mar sin cruinníonn sé le ``2``, ``4``, nó ``8`` g. (socraigh raon)

Example: ``accelerometer.set_range(8)``

:param value: (luach) Raon nua don luasmhéadar, slánuimhir i ``g``."""