"""개별 주소를 지정할 수 있는 RGB 및 RGBW LED 스트립입니다."""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """핀으로 제어되는 새로운 스트립의 네오픽셀 LED를 시작합니다. (string)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (핀) 네오픽셀 스트립을 제어하는 핀입니다.
:param n: 스트립의 네오픽셀 수입니다.
:param bpp: 픽셀당 바이트입니다. RGBW 네오픽셀 지원을 위해서는 RGB 및 GRB의 기본값 3 대신 4를 패스해야 합니다."""
        ...

    def clear(self) -> None:
        """모든 픽셀을 지웁니다.

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """픽셀을 표시합니다.

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """픽셀을 표시합니다(micro:bit V2 전용).

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """모든 픽셀에 주어진 RGB/RGBW 값을 칠합니다(micro:bit V2 전용).

Example: ``np.fill((0, 0, 255))``

:param colour: 픽셀 당 바이트 수(bpp)와 같은 길이의 튜플입니다.

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """픽셀 색상을 설정합니다.

Example: ``np[0] = (255, 0, 0)``

:param key: 픽셀 번호입니다.
:param value: 색상입니다."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """픽셀 색상을 불러옵니다.

Example: ``r, g, b = np[0]``

:param key: 픽셀 번호입니다.
:return: The colour tuple."""

    def __len__(self) -> int:
        """이 픽셀 스트립의 길이를 불러옵니다.

Example: ``len(np)``"""