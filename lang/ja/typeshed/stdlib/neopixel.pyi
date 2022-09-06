"""個別にアドレス可能な RGB/RGBW LED ストリップ。 (neopixel)"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """端子を介して制御するneopixel LEDの新しいストリップを初期化します。 (init)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

RGBW neopixels are only supported by micro:bit V2.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (pin) neopixelストリップを制御する端子。
:param n: (n) ストリップ内のneopixelの数。
:param bpp: (bpp) ピクセルあたりのバイト数。micro:bit V2 の RGBW neopixel に対応するには、RGBやGRBのデフォルト値の3ではなく、4を指定してください。"""
        ...

    def clear(self) -> None:
        """すべてのピクセルをクリアします。 (clear)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """ピクセルを表示します。 (show)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """ピクセルを表示します(micro:bit V2 のみ)。 (write)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """指定したRGB/RGBW値をすべてのピクセルに設定します。 (fill)

Example: ``np.fill((0, 0, 255))``

:param colour: (colour) ピクセルあたりのバイト数(bpp)と同じ長さのタプル。

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """ピクセルの色を設定します。 (setitem)

Example: ``np[0] = (255, 0, 0)``

:param key: (key) ピクセル番号。
:param value: (value) 色。"""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """ピクセルの色を取得します。 (getitem)

Example: ``r, g, b = np[0]``

:param key: (key) ピクセル番号。
:return: The colour tuple."""

    def __len__(self) -> int:
        """このピクセルストリップの長さを取得します。 (len)

Example: ``len(np)``"""