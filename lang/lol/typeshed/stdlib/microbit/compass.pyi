"""crwdns330004:0crwdne330004:0 (crwdns330002:0crwdne330002:0)"""

def calibrate() -> None:
    """crwdns330008:0crwdne330008:0 (crwdns330006:0crwdne330006:0)

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """crwdns330012:0crwdne330012:0 (crwdns330010:0crwdne330010:0)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """crwdns330016:0crwdne330016:0 (crwdns330014:0crwdne330014:0)

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """crwdns330020:0``x``crwdne330020:0 (crwdns330018:0crwdne330018:0)

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """crwdns330024:0``y``crwdne330024:0 (crwdns330022:0crwdne330022:0)

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """crwdns330028:0``z``crwdne330028:0 (crwdns330026:0crwdne330026:0)

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """crwdns330032:0crwdne330032:0 (crwdns330030:0crwdne330030:0)

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """crwdns330036:0crwdne330036:0 (crwdns330034:0crwdne330034:0)

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...