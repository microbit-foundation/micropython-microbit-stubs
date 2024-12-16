"""Mostra text, imatges i animacions a la pantalla LED 5×5. (pantalla)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Obté la brillantor del LED a la columna ``x`` i la fila ``y``. (obté píxel)

Example: ``display.get_pixel(0, 0)``

:param x: La columna de la pantalla (0...4)
:param y: La fila de la pantalla (0...4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Estableix la brillantor del LED a la columna ``x`` i la fila ``y``. (estableix píxel)

Example: ``display.set_pixel(0, 0, 9)``

:param x: La columna de la pantalla (0...4)
:param y: La fila de la pantalla (0...4)
:param value: (valor) La brillantor entre 0 (apagat) i 9 (brillant)"""
    ...

def clear() -> None:
    """Estableix la brillantor de tots els leds a 0 (apagat).

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Mostra imatges, lletres o dígits en la pantalla LED. (mostra)

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: (imatge) Una cadena, un nombre, una imatge o una llista d'imatges per mostrar.
:param delay: (retard) Cada lletra, dígit o imatge es mostra amb un ``delay`` mil·lisegons entre ells.
:param wait: (espera) Si ``wait`` és ``True``, aquesta funció es bloquejarà fins que s'acabi l'animació, en cas contrari, l'animació passarà en segon pla.
:param loop: (bucle) Si el ``loop`` és ``True``, l'animació es repetirà per sempre.
:param clear: Si ``clear`` és ``True``, la pantalla s'esborrarà un cop finalitzada la seqüència.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Desplaça un número o text per la pantalla LED.

Example: ``display.scroll('micro:bit')``

:param text: La cadena per a desplaçar. Si ``text`` és un nombre enter o flotant, primer es converteix en una cadena mitjançant ``str()``.
:param delay: (retard) El paràmetre ``delay`` controla la rapidesa amb què es desplaça el text.
:param wait: (espera) Si ``wait`` és ``True``, aquesta funció es bloquejarà fins que s'acabi l'animació, en cas contrari, l'animació passarà en segon pla.
:param loop: (bucle) Si el ``loop`` és ``True``, l'animació es repetirà per sempre.
:param monospace: Si ``monospace`` és ``True``, tots els caràcters ocuparan 5 columnes de píxels d'amplada, en cas contrari, hi haurà exactament 1 columna de píxels en blanc entre cada caràcter mentre es desplacen.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Encén la pantalla LED.

Example: ``display.on()``"""
    ...

def off() -> None:
    """Apaga la pantalla LED (desactivar la pantalla et permet reutilitzar els pins GPIO per a altres finalitats).

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Comprova si la pantalla LED està habilitada.

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Llegeix el nivell de llum. (llegir el nivell de llum)

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...