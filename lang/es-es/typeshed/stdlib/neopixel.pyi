"""Tiras de LED RGB y RGBW accesibles individualmente."""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Inicializa una nueva tira de LED NeoPixel controlada a través de un pin.

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: El pin que controla la tira NeoPixel.
:param n: El número de LED NeoPixel de la tira.
:param bpp: Bytes por píxel. Para compatibilidad de neopíxeles RGBW, pasa 4 en lugar del valor predeterminado de 3 para RGB y GRB."""
        ...

    def clear(self) -> None:
        """Borrar todos los píxeles. (borrar)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Muestra los píxeles. (mostrar)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Muestra los píxeles (solo micro:bit V2). (escribir)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Colorea todos los píxeles con un valor RGB/RGBW dado (solo micro:bit V2). (llenar)

Example: ``np.fill((0, 0, 255))``

:param colour: (color) Una tupla de la misma longitud que el número de bytes por píxel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Establece el color de un píxel. (configurar elemento)

Example: ``np[0] = (255, 0, 0)``

:param key: (clave) El número de píxel.
:param value: (valor) El color."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Obtiene el color de un píxel. (obtener elemento)

Example: ``r, g, b = np[0]``

:param key: (clave) El número de píxel.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Obtiene la longitud de esta tira de píxeles. (lon)

Example: ``len(np)``"""