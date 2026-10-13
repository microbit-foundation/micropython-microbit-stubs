"""Mostrar texto, imagens e animações na tela de LED 5\xa0×\xa05. (exibir)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Obtenha o brilho do LED na coluna ``x`` e na linha ``y``. (Configurar píxel)

Example: ``display.get_pixel(0, 0)``

:param x: A coluna de exibição (0..4)
:param y: A linha de exibição (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Definir o brilho do LED na coluna ``x`` e na linha ``y``. (Configurar píxel)

Example: ``display.set_pixel(0, 0, 9)``

:param x: A coluna de exibição (0..4)
:param y: A linha de exibição (0..4)
:param value: (Valor) O brilho entre 0 (desligado) e 9 (claro)"""
    ...

def clear() -> None:
    """Definir o brilho de todos os LEDs para 0 (desligado). (limpar)

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Mostrar imagens, letras ou dígitos na tela de LED. (mostrar)

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: (imagem) Uma sequência, número, imagem ou lista de imagens a serem exibidas.
:param delay: (atraso) Cada letra, dígito ou imagem é mostrada com milissegundos de ``delay`` entre eles.
:param wait: Se ``wait`` for ``True``, esta função irá bloquear até que a animação termine, caso contrário, a animação acontecerá em segundo plano.
:param loop: (laço) Se ``loop`` for ``True``, a animação irá repetir para sempre.
:param clear: (limpar) Se ``clear`` for ``True``, a tela será limpa após a sequência ter terminado.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Rola um número ou texto na tela de LED. (rolar)

Example: ``display.scroll('micro:bit')``

:param text: (texto) A sequência para rolar. Se ``text`` é um número inteiro ou flutuante, primeiro será convertido em uma sequência usando ``str()``.
:param delay: (atraso) O parâmetro de ``delay`` controla a rapidez com que o texto está rolando.
:param wait: Se ``wait`` for ``True``, esta função irá bloquear até que a animação termine, caso contrário, a animação acontecerá em segundo plano.
:param loop: (laço) Se ``loop`` for ``True``, a animação irá repetir para sempre.
:param monospace: (Mono espaçado) Se ``monospace`` for ``True``, todos os caracteres levarão 5 colunas de largura, caso contrário, haverá exatamente 1 coluna em branco entre cada caractere enquanto rolam.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Liga a tela de LED. (ligado)

Example: ``display.on()``"""
    ...

def off() -> None:
    """Desliga a tela de LED (desabilitar a tela permite que você reutilize os pinos de GPIO para outros fins). (desligado)

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Verifique se a tela de LED está habilitada. (Está ligado)

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Ler o nível de luz. (Ler nível de luz)

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...