"""Individuell adressierbare RGB- und RGBW-LED-Streifen."""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Initialisiert einen neuen Streifen von Neopixel-LEDs, die über einen Pin gesteuert werden.

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: Der Pin, der den Neopixelstreifen steuert.
:param n: Die Anzahl der Neopixel auf dem Streifen.
:param bpp: Bytes pro Pixel. Für die RGBW Neopixel-Unterstützung, müssen 4 statt der standardmäßigen 3 Bytes pro Pixel für RGB und GRB übergeben werden."""
        ...

    def clear(self) -> None:
        """Löscht alle Pixel.

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Die Pixel anzeigen.

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Pixel anzeigen (nur micro:bit V2) (schreiben)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Färbt alle Pixel mit einem bestimmten RGB/RGBW-Wert (nur micro:bit\xa0V2).

Example: ``np.fill((0, 0, 255))``

:param colour: (Farbe) Ein Tupel mit der gleichen Länge wie die Anzahl der Bytes pro Pixel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Eine Pixelfarbe festlegen.

Example: ``np[0] = (255, 0, 0)``

:param key: Die Pixelnummer.
:param value: (wert) Die Farbe."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Eine Pixelfarbe erfassen.

Example: ``r, g, b = np[0]``

:param key: Die Pixelnummer.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Liefert die Länge des Pixelstreifens.

Example: ``len(np)``"""