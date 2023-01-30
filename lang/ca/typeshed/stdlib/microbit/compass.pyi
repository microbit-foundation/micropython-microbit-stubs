"""Utilitza la brúixola integrada. (brúixola)"""

def calibrate() -> None:
    """Comença el procés de calibració (calibrar)

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Verifica si la brúixola està calibrada. (s'ha calibrat)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Desfà el calibratge, fent que la brúixola torni a estar sense calibració. (esborra la calibració)

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Obté la intensitat del camp magnètic de l'eix ``x`` . (obté x)

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Obté la intensitat del camp magnètic de l'eix ``y`` . (obté y)

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Obté la intensitat del camp magnètic a l'eix ``z``. (obté z)

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Obté l'orientació de la brúixola.

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Obté la magnitud del camp magnètic al voltant del dispositiu. (obté la intensitat del camp)

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...