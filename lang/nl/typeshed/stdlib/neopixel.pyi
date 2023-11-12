"""Individueel adresseerbare RGB en RGBW LED-strips."""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Initialiseer een nieuwe strip van neopixel LED's beheerd via een pin. (initialiseren)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: De pin regelt de neopixelstrook.
:param n: Het aantal neopixels in de strip.
:param bpp: Bytes per pixel. Voor ondersteuning van RGBW neopixels geeft je 4 aan in plaats van de standaardwaarde van 3 voor RGB en GRB."""
        ...

    def clear(self) -> None:
        """Verwijder alle pixels. (wissen)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Toon de pixels. (toon)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Toon de pixels (alleen micro:bit V2). (schrijven)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Kleur alle pixels een bepaalde RGB/RGBW waarde (alleen micro:bit V2). (opvullen)

Example: ``np.fill((0, 0, 255))``

:param colour: (kleur) Een tuple van dezelfde lengte als het aantal bytes per pixel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Stel een pixelkleur in.

Example: ``np[0] = (255, 0, 0)``

:param key: (sleutel) Het pixelnummer.
:param value: (waarde) De kleur."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Krijg een pixelkleur.

Example: ``r, g, b = np[0]``

:param key: (sleutel) Het pixelnummer.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Haal de lengte op van deze pixelstrip.

Example: ``len(np)``"""