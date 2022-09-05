"""使用内置的指南针。 (compass)"""

def calibrate() -> None:
    """开始校准过程。 (calibrate)

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """检查指南针是否已校准。 (is calibrated)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """取消校准，将指南针恢复到未校准状态。 (clear calibration)

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """获取 ``x`` 轴上的磁场强度。 (get x)

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """获取 ``y`` 轴上的磁场强度。 (get y)

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """获取 ``z`` 轴上的磁场强度。 (get z)

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """获取指南针指向。 (heading)

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """获取设备周围磁场的强度。 (get field strength)

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...