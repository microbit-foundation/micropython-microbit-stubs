"""Stiallacha RGB agus RGBW LED atá inseolta ina n-aonar."""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Túsaigh stiall nua de soilse neopicsel a rialaítear trí bhiorán.

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (biorán) An biorán a rialaíonn an stiall neopicsel.
:param n: Líon na neopicsel sa stiall.
:param bpp: Bearta in aghaidh an phicteilín. Maidir le tacaíocht neopicsel RGBW, pas 4 seachas mainneachtain 3 do RGB agus GRB."""
        ...

    def clear(self) -> None:
        """Glan na picteilíní go léir. (soiléir)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Taispeáin na picteilíní. (taispeáin)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Taispeáin na picteilíní (micro:bit V2 amháin). (scríobh)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Dathaigh gach picteilín luach RGB / RGBW ar leith (micro:bit V2 amháin). (líonadh)

Example: ``np.fill((0, 0, 255))``

:param colour: (dath) Tupla den fhad céanna le líon na mbeart in aghaidh an phicteilín (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Socraigh dath picteilín. (socraigh mír)

Example: ``np[0] = (255, 0, 0)``

:param key: (eochair) Uimhir an phicteilín.
:param value: (luach) An dath."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Faigh dath picteilín. (faigh mír)

Example: ``r, g, b = np[0]``

:param key: (eochair) Uimhir an phicteilín.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Faigh fad an stiall picteilín seo.

Example: ``len(np)``"""