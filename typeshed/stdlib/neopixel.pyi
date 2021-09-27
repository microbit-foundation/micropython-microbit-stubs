"""
The ``neopixel`` module lets you use NeoPixel (WS2812) individually addressable
RGB and RGBW **V2** LED strips with the micro:bit. Note to use the ``neopixel`` module, you
need to import it separately with::

    import neopixel

.. note::

    From our tests, the Microbit NeoPixel module can drive up to around 256
    NeoPixels. Anything above that and you may experience weird bugs and
    issues. The micro:bit can only supply 90mA **V1** or 190mA **V2**  to
    external devices,larger numbers of NeoPixels require an external power
    supply with common ground.

    NeoPixels are designed to work at 5V, but luckily they still function using
    the 3V supply of the BBC micro:bit. Please note that the micro:bit edge
    connector should not be connected to anything supplying 5V.

NeoPixels are fun strips of multi-coloured programmable LEDs. This module
contains everything to plug them into a micro:bit and create funky displays,
art and games.

To connect a strip of neopixels you'll need to attach the micro:bit as shown
below (assuming you want to drive the pixels from pin 0 - you can connect
neopixels to pins 1 and 2 too). The label on the crocodile clip tells you where
to attach the other end on the neopixel strip. The VDD pin may be labelled
as something else on some variants of neopixels - for example "V+". In some
cases it may be called "+5V" and it is only safe to use this if you have no
other 5V devices connected.

.. warning::

    Do not use the 3v connector on the micro:bit to power any more than 8
    Neopixels at a time.

    If you wish to use more than 8 Neopixels, you must use a separate 3v-5v
    power supply for the Neopixel power pin.
"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:
    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int = 3 -> None:
        """
        Initialise a new strip of ``n`` number of neopixel LEDs controlled via pin
        ``pin``. The **V2** micro:bit can also support RGBW neopixels, so a third
        argument can be passed to ``NeoPixel`` to indicate the number of bytes per
        pixel (bpp). For RGBW, this is is ``4`` rather than the default of ``3`` for
        RGB and GRB.
        """
        ...
    def clear(self) -> None:
        """
        Clear all the pixels.
        """
        ...
    def show(self) -> None:
        """
        Show the pixels. Must be called for any updates to become visible.
        """
        ...
    def write(self) -> None:
        """
        **V2** Show the pixels. Must be called for any updates to become visible.

        Equivalent to ``show``.
        """
        ...
    def fill(self, colour: Tuple[int, ...]) -> None:
        """
        **V2** Colour all pixels a given RGB/RGBW value. The `colour` argument
        should be a tuple of the same length as the number of bytes per pixel
        (bpp). For example ``fill((0,0,255))``. Use in conjunction with
        ``show()`` to update the Neopixels.
        """
        ...
    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None: ...
    def __getitem__(self, key: int) -> Tuple[int, ...]: ...
    def __len__(self) -> int: ...
