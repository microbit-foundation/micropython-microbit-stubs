"""내장된 나침반을 사용합니다. (나침반)"""

def calibrate() -> None:
    """보정 프로세스를 시작합니다.

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """나침반이 보정되었는지 확인합니다.

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """보정을 해제해 나침반을 보정하지 않은 상태로 설정합니다.

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """``x`` 축의 자기장 강도를 불러옵니다.

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """``y`` 축의 자기장 강도를 불러옵니다.

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """``z`` 축의 자기장 강도를 불러옵니다.

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """나침반의 방향을 불러옵니다.

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """장치 주변의 자기장 규모를 불러옵니다.

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...