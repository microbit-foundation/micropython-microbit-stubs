"""Cintes LED RGB i RGBW adreçables individualment."""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Inicialitza una nova tira de LED de neopixel controlada mitjançant un pin.

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: El pin que controla la tira de neopíxels.
:param n: El nombre de neopíxels de la tira.
:param bpp: Bytes per píxel. Per al suport del neopixel RGBW , passa 4 en lloc dels 3 per defecte per a RGB i GRB."""
        ...

    def clear(self) -> None:
        """Esborra tots els píxels.

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """mostra els píxels.

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Mostra els píxels (només micro:bit V2) (escriu)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Acoloreix tots els píxels amb un valor RGB/RGBW determinat (només micro:bit V2). (omple)

Example: ``np.fill((0, 0, 255))``

:param colour: (color) Una tupla de la mateixa longitud que el nombre de bytes per píxel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Estableix un color de píxel.

Example: ``np[0] = (255, 0, 0)``

:param key: El nombre de píxels.
:param value: (valor) El color."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Obté un color de píxel.

Example: ``r, g, b = np[0]``

:param key: El nombre de píxels.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Obté la longitud d'aquesta cinta de píxels.

Example: ``len(np)``"""