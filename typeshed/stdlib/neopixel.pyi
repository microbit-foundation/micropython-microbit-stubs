"""Individually addressable RGB and RGBW LED strips.
"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:
    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int = 3) -> None:
        """
        Initialise a new strip of neopixel LEDs controlled via a pin.

        RGBW neopixels are only supported by micro:bit V2.

        See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

        :param pin: The pin controlling the neopixel strip.
        :param n: The number of neopixels in the strip.
        :param bpp: Bytes per pixel. For micro:bit V2 RGBW neopixel support, pass ``4`` rather than the default of ``3`` for RGB and GRB.
        """
        ...
    def clear(self) -> None:
        """Clear all the pixels."""
        ...
    def show(self) -> None:
        """Show the pixels.

        Must be called for any updates to become visible.
        """
        ...
    def write(self) -> None:
        """Show the pixels (microbit V2 only).

        Must be called for any updates to become visible.

        Equivalent to ``show``.
        """
        ...
    def fill(self, colour: Tuple[int, ...]) -> None:
        """Colour all pixels a given RGB/RGBW value.

        :param colour: A tuple of the same length as the number of bytes per pixel (bpp).

        For example ``fill((0,0,255))``. Use in conjunction with ``show()`` to update the neopixels.
        """
        ...
    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None: ...
    def __getitem__(self, key: int) -> Tuple[int, ...]: ...
    def __len__(self) -> int: ...
