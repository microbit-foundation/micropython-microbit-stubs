"""crwdns330604:0crwdne330604:0 (crwdns330602:0crwdne330602:0)"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """crwdns330608:0crwdne330608:0 (crwdns330606:0crwdne330606:0)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (crwdns330618:0crwdne330618:0) crwdns330620:0crwdne330620:0
:param n: (crwdns330614:0crwdne330614:0) crwdns330616:0crwdne330616:0
:param bpp: (crwdns330610:0crwdne330610:0) crwdns355240:0crwdne355240:0"""
        ...

    def clear(self) -> None:
        """crwdns330624:0crwdne330624:0 (crwdns330622:0crwdne330622:0)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """crwdns330628:0crwdne330628:0 (crwdns330626:0crwdne330626:0)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """crwdns330632:0crwdne330632:0 (crwdns330630:0crwdne330630:0)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """crwdns330636:0crwdne330636:0 (crwdns330634:0crwdne330634:0)

Example: ``np.fill((0, 0, 255))``

:param colour: (crwdns330638:0crwdne330638:0) crwdns330640:0crwdne330640:0

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """crwdns330644:0crwdne330644:0 (crwdns330642:0crwdne330642:0)

Example: ``np[0] = (255, 0, 0)``

:param key: (crwdns330646:0crwdne330646:0) crwdns330648:0crwdne330648:0
:param value: (crwdns330650:0crwdne330650:0) crwdns330652:0crwdne330652:0"""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """crwdns330656:0crwdne330656:0 (crwdns330654:0crwdne330654:0)

Example: ``r, g, b = np[0]``

:param key: (crwdns330658:0crwdne330658:0) crwdns330660:0crwdne330660:0
:return: The colour tuple."""

    def __len__(self) -> int:
        """crwdns330664:0crwdne330664:0 (crwdns330662:0crwdne330662:0)

Example: ``len(np)``"""