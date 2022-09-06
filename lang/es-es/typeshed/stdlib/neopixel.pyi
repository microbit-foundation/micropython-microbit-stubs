"""Tiras de LED RGB y RGBW accesibles individualmente. (neopixel)"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Inicializa una nueva tira de LED NeoPixel controlada a través de un pin. (init)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

RGBW neopixels are only supported by micro:bit V2.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (pin) El pin que controla la tira NeoPixel.
:param n: (n) El número de LED NeoPixel de la tira.
:param bpp: (bpp) Bytes por píxel. Para compatibilidad con NeoPixel RGBW de micro:bit V2, pasa 4 en lugar del valor predeterminado 3 para RGB y GRB."""
        ...

    def clear(self) -> None:
        """Borrar todos los píxeles. (clear)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Muestra los píxeles. (show)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Muestra los píxeles (solo micro:bit V2). (write)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Colorea todos los píxeles con un valor RGB/RGBW dado. (fill)

Example: ``np.fill((0, 0, 255))``

:param colour: (colour) Una tupla de la misma longitud que el número de bytes por píxel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Establece el color de un píxel. (setitem)

Example: ``np[0] = (255, 0, 0)``

:param key: (key) El número de píxel.
:param value: (valor) El color."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Obtiene el color de un píxel. (getitem)

Example: ``r, g, b = np[0]``

:param key: (key) El número de píxel.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Obtiene la longitud de esta tira de píxeles. (len)

Example: ``len(np)``"""