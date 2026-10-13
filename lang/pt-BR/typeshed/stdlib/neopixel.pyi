"""Fitas de LED RGB e RGBW endereçáveis individualmente."""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Inicializar uma nova faixa de LEDs neopixel controlada por um pino. (iniciar)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

To support RGBW neopixels, a third argument can be passed to
``NeoPixel`` to indicate the number of bytes per pixel (``bpp``).
For RGBW, this is is 4 rather than the default of 3 for RGB and GRB.

Each pixel is addressed by a position (starting from 0). Neopixels are
given RGB (red, green, blue) / RGBW (red, green, blue, white) values
between 0-255 as a tuple. For example, in RGB, ``(255,255,255)`` is
white. In RGBW, ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (alfinete) O pino que controla a faixa de neopixels.
:param n: O número de neopixels na faixa.
:param bpp: Bytes por pixel. Para suporte a neopixel RGBW, passe 4 em vez do padrão 3 para RGB e GRB."""
        ...

    def clear(self) -> None:
        """Limpe todos os pixels. (limpar)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Mostre os pixels. (mostrar)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Mostrar os pixels (apenas para micro:bit V2). (escrever)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Colorir todos os pixels com um determinado valor RGB/RGBW (apenas micro:bit V2). (Completar)

Example: ``np.fill((0, 0, 255))``

:param colour: (cor) Uma tupla do mesmo comprimento que o número de bytes por pixel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Definir a cor do pixel. (definir item)

Example: ``np[0] = (255, 0, 0)``

:param key: (chave) O número do pixel.
:param value: (Valor) A cor."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Obter a cor do pixel. (obter item)

Example: ``r, g, b = np[0]``

:param key: (chave) O número do pixel.
:return: The colour tuple."""

    def __len__(self) -> int:
        """Obter o comprimento desta faixa de pixels.

Example: ``len(np)``"""