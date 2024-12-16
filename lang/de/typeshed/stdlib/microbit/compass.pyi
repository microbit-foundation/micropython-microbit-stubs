"""Benutze den eingebauten Kompass. (Kompass)"""

def calibrate() -> None:
    """Startet den Kalibrierungsprozess.

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Überprüft, dass der Kompass kalibriert ist. (ist kalibriert)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Setzt die Kalibrierung zurück, sodass der Kompass nicht mehr kalibriert ist.

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Liefert die Magnetfeldstärke der ``x``-Achse.

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Liefert die Magnetfeldstärke der ``y``-Achse.

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Liefert die Magnetfeldstärke der ``z``-Achse.

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Ermittelt die Kompassrichtung. (Ausrichtung)

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Ermittelt die Größe des Magnetfelds um das Gerät herum.

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...