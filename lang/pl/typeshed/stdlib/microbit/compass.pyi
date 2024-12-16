"""Użyj wbudowanego kompasu."""

def calibrate() -> None:
    """Rozpoczyna proces kalibracji.

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Sprawdź, czy kompas jest skalibrowany.

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Cofnij kalibrację, czyniąc kompas ponownie niekalibrowanym.

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Uzyskaj natężenie pola magnetycznego na osi ``x``.

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Uzyskaj natężenie pola magnetycznego na osi ``y``.

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Uzyskaj natężenie pola magnetycznego na osi ``z``.

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Pobierz kierunek kompasu.

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Uzyskaj wielkość pola magnetycznego wokół urządzenia.

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...