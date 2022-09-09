"""可獨立尋址的 RGB 和 RGBW LED 燈條。 (neopixel)"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """初始化透過引腳控制的 NeoPixel LED 燈條。 (init)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

RGBW neopixels are only supported by micro:bit V2.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (引腳) 控制 NeoPixel 燈條的引腳。
:param n: (n) 燈條中的 NeoPixel 數。
:param bpp: (bpp) 各像素位元組數。 對於 micro:bit V2 RGBW neopixel 支持，傳遞 4 而不是 RGB 和 GRB 的預設值 3。"""
        ...

    def clear(self) -> None:
        """清除所有像素。 (clear)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """顯示像素。 (show)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """顯示像素 (僅限 micro:bit V2)。 (write)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """用特定 RGB/RGBW 值為所有像素著色。 (fill)

Example: ``np.fill((0, 0, 255))``

:param colour: (colour) 長度與每像素位元組數 (bpp) 相同的元組。

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """設定像素顏色。 (setitem)

Example: ``np[0] = (255, 0, 0)``

:param key: (key) 像素編號。
:param value: (value) 顏色。"""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """取得像素顏色。 (getitem)

Example: ``r, g, b = np[0]``

:param key: (key) 像素編號。
:return: The colour tuple."""

    def __len__(self) -> int:
        """取得此像素燈條的長度。 (len)

Example: ``len(np)``"""