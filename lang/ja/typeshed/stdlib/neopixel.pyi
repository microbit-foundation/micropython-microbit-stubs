"""個別にアドレス可能な RGB/RGBW LED ストリップ。"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """端子を介して制御するネオピクセルLEDの新しいストリップを初期化します。

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: ネオピクセルストリップを制御する端子。
:param n: ストリップ内のネオピクセルの数。
:param bpp: ピクセルあたりのバイト数。RGBW ネオピクセルに対応するには、RGBやGRBのデフォルト値の3ではなく、4 を指定します。"""
        ...

    def clear(self) -> None:
        """すべてのピクセルをクリアします。

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """ピクセルを表示します。

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """ピクセルを表示します（micro:bit V2 のみ）。

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """指定した RGB/RGBW 値をすべてのピクセルに設定します（micro:bit V2 のみ）。

Example: ``np.fill((0, 0, 255))``

:param colour: ピクセルあたりのバイト数（bpp）と同じ長さのタプル。

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """ピクセルの色を設定します。

Example: ``np[0] = (255, 0, 0)``

:param key: ピクセル番号。
:param value: 色。"""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """ピクセルの色を取得します。

Example: ``r, g, b = np[0]``

:param key: ピクセル番号。
:return: The colour tuple."""

    def __len__(self) -> int:
        """このピクセルストリップの長さを取得します。

Example: ``len(np)``"""