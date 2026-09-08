"""Mostrar texto, imágenes y animaciones en la pantalla LED de 5 × 5. (pantalla)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Obtiene el brillo del LED que hay en la columna ``x`` y fila ``y``. (obtener píxel)

Example: ``display.get_pixel(0, 0)``

:param x: La columna de la pantalla (0..4)
:param y: La fila de la pantalla (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Establece el brillo del LED que hay en la columna ``x`` y fila ``y``. (configurar píxel)

Example: ``display.set_pixel(0, 0, 9)``

:param x: La columna de la pantalla (0..4)
:param y: La fila de la pantalla (0..4)
:param value: (valor) El brillo entre 0 (apagado) y 9 (brillante)"""
    ...

def clear() -> None:
    """Ajusta el brillo de todos los LED a 0 (apagado). (borrar)

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Muestra imágenes, letras o dígitos en la pantalla LED. (mostrar)

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: (imagen) Una cadena, número, imagen o lista de imágenes para mostrar.
:param delay: (retardo) Cada letra, dígito o imagen se muestra con ``delay`` milisegundos de retardo entre ellos.
:param wait: (esperar) Si ``wait`` es ``True`` (verdadero), la función se bloqueará hasta que finalice la animación; de lo contrario, la animación se ejecutará en segundo plano.
:param loop: (bucle) Si ``loop`` es ``True`` (verdadero), la animación se repetirá para siempre.
:param clear: (borrar) Si ``clear`` es ``True`` (verdadero), la pantalla se borrará una vez que la secuencia haya terminado.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Desplaza un número o texto por la pantalla LED. (desplazar)

Example: ``display.scroll('micro:bit')``

:param text: (texto) La cadena a desplazar. Si ``text`` es un entero o de coma flotante, primero se convertirá a cadena usando ``str()``.
:param delay: (retardo) El parámetro ``delay`` controla la velocidad de desplazamiento del texto.
:param wait: (esperar) Si ``wait`` es ``True`` (verdadero), la función se bloqueará hasta que finalice la animación; de lo contrario, la animación se ejecutará en segundo plano.
:param loop: (bucle) Si ``loop`` es ``True`` (verdadero), la animación se repetirá para siempre.
:param monospace: Si ``monospace`` es ``True`` (verdadero), todos los caracteres ocuparán columnas de 5 píxeles de ancho; de lo contrario, habrá exactamente 1 columna de píxeles vacíos entre cada carácter a medida que se desplazan.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Enciende la pantalla LED. (encendido)

Example: ``display.on()``"""
    ...

def off() -> None:
    """Apaga la pantalla LED (desactivar la pantalla te permite reutilizar los pines GPIO para otros fines). (apagado)

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Comprueba si la pantalla LED está activada. (está encendido)

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Lee el nivel de luz. (leer nivel de luz)

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...