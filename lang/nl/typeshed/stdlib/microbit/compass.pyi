"""Gebruik het ingebouwde kompas. (kompas)"""

def calibrate() -> None:
    """Start het kalibratieproces. (Kalibreren)

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Controleer of het kompas is gekalibreerd. (gekalibreerd)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Kalibratie ongedaan maken, waardoor het kompas weer losgemaakt wordt. (kalibratie wissen)

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Krijg de magnetische veldsterkte op de ``x`` as. (krijg x)

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Krijg de magnetische veldsterkte op de ``y`` as. (krijg y)

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Krijg de magnetische veldsterkte op de ``z`` as. (krijg z)

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Haal de kompaskop op. (kop)

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Krijg de magnitude van het magnetische veld rond het apparaat. (krijg veldsterkte)

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...