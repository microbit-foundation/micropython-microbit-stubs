"""可单独寻址的 RGB 和 RGBW LED 灯带。 (neopixel)"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """初始化一条通过一个引脚控制的新 neopixel LED 灯带。 (init)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

RGBW neopixels are only supported by micro:bit V2.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (引脚) 控制 neopixel 灯带的引脚。
:param n: (n) 灯带中 neopixel 灯珠的数量。
:param bpp: (bpp) 每个像素的字节数。对于 RGB 和 GRB 而言，只有将该值设置为 4 而不是默认值 3，micro:bit V2 RGBW neopixel 才能支持。"""
        ...

    def clear(self) -> None:
        """清除所有像素。 (clear)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """显示像素。 (show)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """显示像素（仅限 micro:bit V2）。 (write)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """
用给定的 RGB/RGBW 值为所有像素着色。 (fill)

Example: ``np.fill((0, 0, 255))``

:param colour: (colour) 长度与每像素字节数 (bpp) 相同的元组。

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """设置像素颜色 (setitem)

Example: ``np[0] = (255, 0, 0)``

:param key: (key) 像素数。
:param value: (value) 颜色。"""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """获取像素颜色。 (getitem)

Example: ``r, g, b = np[0]``

:param key: (key) 像素数。
:return: The colour tuple."""

    def __len__(self) -> int:
        """获取此像素条的长度。 (len)

Example: ``len(np)``"""