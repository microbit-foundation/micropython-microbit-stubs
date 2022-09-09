"""使用內建指南針。 (羅盤)"""

def calibrate() -> None:
    """開始校準程序。 (calibrate)

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """檢查指南針是否已校準。 (is calibrated)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """撤消校準，使指南針再次未校準。 (clear calibration)

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """取得 ``x`` 軸上的磁場強度。 (get x)

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """取得 ``y`` 軸上的磁場強度。 (get y)

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """取得 ``z`` 軸上的磁場強度。 (get z)

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """取得指南針方向。 (heading)

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """獲取裝置周圍磁場的大小。 (get field strength)

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...