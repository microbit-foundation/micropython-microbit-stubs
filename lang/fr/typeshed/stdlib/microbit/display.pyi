"""Afficher du texte, des images et des animations sur l'écran LED 5×5."""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Récupère la luminosité de la LED à la colonne ``x`` et à la ligne ``y``.

Example: ``display.get_pixel(0, 0)``

:param x: La colonne d'affichage (0..4)
:param y: La ligne d'affichage (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Définit la luminosité de la LED à la colonne ``x`` et à la ligne ``y``.

Example: ``display.set_pixel(0, 0, 9)``

:param x: La colonne d'affichage (0..4)
:param y: La ligne d'affichage (0..4)
:param value: La luminosité entre 0 (éteint) et 9 (lumineux)"""
    ...

def clear() -> None:
    """Régler la luminosité de toutes les LED à 0 (éteintes).

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Afficher des images, des lettres ou des chiffres sur l'affichage LED.

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: Une chaîne de caractères, un nombre, une image ou une liste d'images à afficher.
:param delay: Chaque lettre, chiffre ou image est séparé par un délai de ``delay`` millisecondes.
:param wait: Si ``wait`` est ``True`` cette fonction bloquera jusqu'à la fin de l'animation, sinon l'animation s'effectuera en arrière-plan.
:param loop: Si ``loop`` est ``True``, l'animation se répétera indéfiniment.
:param clear: Si ``clear`` est ``True``, l'affichage sera effacé une fois la séquence terminée.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Faire défiler un nombre ou un texte sur l'affichage LED.

Example: ``display.scroll('micro:bit')``

:param text: La chaîne de caractères à faire défiler. Si ``text`` est un entier ou un nombre décimal, il sera converti en une chaîne avec ``str()``.
:param delay: Le paramètre ``delay`` contrôle la vitesse de défilement du texte.
:param wait: Si ``wait`` est ``True`` cette fonction bloquera jusqu'à la fin de l'animation, sinon l'animation s'effectuera en arrière-plan.
:param loop: Si ``loop`` est ``True``, l'animation se répétera indéfiniment.
:param monospace: Si ``monospace`` est ``True``, tous les caractères utiliseront 5 pixels en largeur, sinon, exactement 1 colonne de pixel vide sera insérée entre chaque caractère lors du défilement.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Allumer l'écran LED.

Example: ``display.on()``"""
    ...

def off() -> None:
    """Eteindre l'écran LED (désactiver l'affichage vous permet de réutiliser les broches GPIO à d'autres fins).

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Vérifier si l'affichage LED est activé.

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Lit le niveau de lumière.

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...