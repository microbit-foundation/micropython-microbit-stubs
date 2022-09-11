"""Utiliser la boussole intégrée."""

def calibrate() -> None:
    """Démarrer le processus d'étalonnage.

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Vérifier si la boussole est étalonnée.

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Annule l'étalonnage, la boussole est ainsi à nouveau non-étalonnée.

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Obtenir la force du champ magnétique sur l'axe ``x``.

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Obtenir la force du champ magnétique sur l'axe ``y``.

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Obtenir la force du champ magnétique sur l'axe ``z``.

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Obtenir le cap de la boussole.

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Récupère la magnitude du champ magnétique autour de l'appareil.

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...