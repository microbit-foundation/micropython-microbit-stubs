"""Bandes LED RGB et RGBW individuellement adressables. (neopixel)"""
from .microbit import MicroBitDigitalPin
from typing import Tuple

class NeoPixel:

    def __init__(self, pin: MicroBitDigitalPin, n: int, bpp: int=3) -> None:
        """Initialiser une nouvelle bande de LEDs neopixel contrôlée via une broche. (init)

Example: ``np = neopixel.NeoPixel(pin0, 8)``

RGBW neopixels are only supported by micro:bit V2.

See `the online docs <https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html>`_ for warnings and other advice.

:param pin: (broche) La broche qui contrôle la bande neopixel.
:param n: (n) Le nombre de neopixels sur la bande.
:param bpp: (bpp) Octets par pixel. Pour le support du neopixel RGBW microbit V2, passez 4 plutôt que la valeur par défaut de 3 pour RGB et GRB."""
        ...

    def clear(self) -> None:
        """Effacer tous les pixels. (clear)

Example: ``np.clear()``"""
        ...

    def show(self) -> None:
        """Afficher les pixels. (show)

Example: ``np.show()``

Must be called for any updates to become visible."""
        ...

    def write(self) -> None:
        """Afficher les pixels (micro:bit V2 uniquement). (write)

Example: ``np.write()``

Must be called for any updates to become visible.

Equivalent to ``show``."""
        ...

    def fill(self, colour: Tuple[int, ...]) -> None:
        """Colorer tous les pixels d'une valeur RGB/RGBW donnée. (fill)

Example: ``np.fill((0, 0, 255))``

:param colour: (colour) Un tuple de la même longueur que le nombre d'octets par pixel (bpp).

Use in conjunction with ``show()`` to update the neopixels."""
        ...

    def __setitem__(self, key: int, value: Tuple[int, ...]) -> None:
        """Définit une couleur de pixel. (setitem)

Example: ``np[0] = (255, 0, 0)``

:param key: (key) Le numéro du pixel
:param value: (value) La couleur."""

    def __getitem__(self, key: int) -> Tuple[int, ...]:
        """Récupère la couleur d'un pixel (getitem)

Example: ``r, g, b = np[0]``

:param key: (key) Le numéro du pixel
:return: The colour tuple."""

    def __len__(self) -> int:
        """Récupère la longueur de cette bande de pixels. (len)

Example: ``len(np)``"""