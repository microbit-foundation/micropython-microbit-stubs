"""Bain úsáid as an compás tógtha. (compás)"""

def calibrate() -> None:
    """Tosaíonn seo an próiseas calabrúcháin. (calabrú)

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Seiceáil go bhfuil an compás calabraithe. (atá calabraithe)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Cealaigh an calabrú, rud a fhágann go bhfuil an compás neamhráite arís. (calabrú soiléir)

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Faigh neart an réimse mhaighnéadaigh ar an ais ``x`` . (faigh x)

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Faigh neart an réimse mhaighnéadaigh ar an ais ``y`` . (faigh y)

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Faigh neart an réimse mhaighnéadaigh ar an ais ``z`` . (faigh z)

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Faigh ceannteideal an chompáis. (ceannteideal)

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Faigh méid an réimse maighnéadach timpeall an ghléis.

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...