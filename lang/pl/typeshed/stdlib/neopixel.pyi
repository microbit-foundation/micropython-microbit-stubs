"""Indywidualnie adresowalne paski LED RGB i RGBW."""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Zainicjuj nowy pasek neopikselowych diod LED sterowanych za pomocą pinu.

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: Pin kontrolujący pasek neopikseli.
:param n: Liczba neopikseli w pasku.
:param bpp: Bajty na piksel. W przypadku obsługi neopikseli RGBW należy przekazać 4 zamiast domyślnych 3 dla RGB i GRB."""
        ...

    def clear(self) -> None:
        """Wyczyść wszystkie piksele.

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Pokaż piksele.

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Pokaż piksele (tylko micro:bit V2).

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Pokoloruj wszystkie piksele określoną wartością RGB/RGBW (tylko micro:bit V2).

Example: ``np.fill((0, 0, 255))``

:param colour: Krotka o takiej samej długości jak liczba bajtów na piksel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Ustaw kolor pikseli.

Example: ``np[0] = (255, 0, 0)``

:param key: Liczba pikseli.
:param value: Kolor"""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Uzyskaj kolor piksela.

Example: ``r, g, b = np[0]``

:param key: Liczba pikseli.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Uzyskaj długość tego paska pikseli.

Example: ``len(np)``"""