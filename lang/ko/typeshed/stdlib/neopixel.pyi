"""별도의 주소 지정 가능한 RGB 및 RGBW LED 스트립. (neopixel)"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """핀으로 제어되는 새로운 스트립의 neopixel LED를 시작합니다. (string)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

RGBW neopixels are only supported by micro:bit V2.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (핀) neopixel 스트립을 제어하는 핀.
:param n: (n) 스트립의 neopixel 수.
:param bpp: (bpp) 픽셀 당 바이트. micro:bit V2 RGBW neopixel 지원을 위해서는 RGB 및 GRB의 기본 3 대신 4를 패스해야 합니다."""
        ...

    def clear(self) -> None:
        """모든 픽셀을 지웁니다. (clear)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """픽셀을 표시합니다. (show)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """픽셀을 표시합니다(micro:bit V2 전용). (write)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """모든 픽셀에 주어진 RGB/RGBW 값을 칠합니다. (fill)

Example: ``np.fill((0, 0, 255))``

:param colour: (colour) 픽셀 당 바이트 수(bpp)와 같은 길이의 튜플.

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Set a pixel colour. (setitem)

Example: ``np[0] = (255, 0, 0)``

:param key: (key) 픽셀의 번호.
:param value: (value) 색상."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """픽셀 색상을 불러옵니다. (getitem)

Example: ``r, g, b = np[0]``

:param key: (key) 픽셀의 번호.
:return: The colour tuple."""

    def __len__(self) -> int:
        """이 픽셀 스트립의 길이를 불러옵니다. (len)

Example: ``len(np)``"""