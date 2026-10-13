"""Use a bússola embutida. (bússola)"""

def calibrate() -> None:
    """Inicia o processo de calibração. (calibrar)

Example: ``compass.calibrate()``

An instructive message will be scrolled to the user after which they will need
to rotate the device in order to draw a circle on the LED display."""
    ...

def is_calibrated() -> bool:
    """Verificar se a bússola está calibrada. (Está calibrado)

Example: ``compass.is_calibrated()``

:return: ``True`` if the compass has been successfully calibrated, ``False`` otherwise."""
    ...

def clear_calibration() -> None:
    """Desfaz a calibração, fazendo a bússola não calibrada novamente. (limpar calibração)

Example: ``compass.clear_calibration()``"""
    ...

def get_x() -> int:
    """Obter a força do campo magnético no eixo ``x``. (Obter x)

Example: ``compass.get_x()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_y() -> int:
    """Obter a força do campo magnético no eixo ``y``. (Obter y)

Example: ``compass.get_y()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def get_z() -> int:
    """Obter a força do campo magnético no eixo ``z``. (Obter Z)

Example: ``compass.get_z()``

Call ``calibrate`` first or the results will be inaccurate.

:return: A positive or negative integer in nano tesla representing the magnitude and direction of the field."""
    ...

def heading() -> int:
    """Obter o rumo da bússola. (rumo)

Example: ``compass.heading()``

:return: An integer in the range from 0 to 360, representing the angle in degrees, clockwise, with north as 0."""
    ...

def get_field_strength() -> int:
    """Obtenha a magnitude do campo magnético ao redor do dispositivo. (Obter força do campo)

Example: ``compass.get_field_strength()``

:return: An integer indication of the magnitude of the magnetic field in nano tesla."""
    ...