"""可獨立尋址的 RGB 和 RGBW LED 燈條。"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """初始化透過引腳控制的 NeoPixel LED 燈條。

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (引腳) 控制 NeoPixel 燈條的引腳。
:param n: 燈條中的 NeoPixel 數。
:param bpp: 各像素位元組數。對於 RGBW neopixel 支援，傳遞 4 而不是 RGB 和 GRB 的預設值 3。"""
        ...

    def clear(self) -> None:
        """清除所有像素。

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """顯示像素。

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """顯示像素 (僅限 micro:bit V2)。

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """用特定 RGB/RGBW 值為所有像素著色 (僅限 micro:bit V2)。

Example: ``np.fill((0, 0, 255))``

:param colour: 長度與每像素位元組數 (bpp) 相同的元組。

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """設定像素顏色。

Example: ``np[0] = (255, 0, 0)``

:param key: 像素編號。
:param value: 顏色。"""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """取得像素顏色。

Example: ``r, g, b = np[0]``

:param key: 像素編號。
:return: The colour tuple."""

    def __len__(self) -> int:
        """取得此像素燈條的長度。

Example: ``len(np)``"""