"""Usar la brújula incorporada. (brujula)"""

def calibrate() -> None:
    """Inicia el proceso de calibración. (calibrate)

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Comprueba si la brújula está calibrada. (is calibrated)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Deshace la calibración, haciendo que la brújula esté otra vez sin calibrar. (clear calibration)

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Obtiene la fuerza del campo magnético en el eje ``x``. (get x)

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Obtiene la fuerza del campo magnético en el eje ``y``. (get y)

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Obtiene la fuerza del campo magnético en el eje ``z``. (get z)

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Obtiene el rumbo de la brújula. (heading)

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Obtiene la magnitud del campo magnético alrededor del dispositivo. (get field strength)

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...