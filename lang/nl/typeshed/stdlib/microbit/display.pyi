"""Tekst, afbeeldingen en animaties weergeven op het 5×5 LED-weergave."""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Krijg de helderheid van de LED in kolom ``x`` en rij ``y``. (verkrijg pixel)

Example: ``display.get_pixel(0, 0)``

:param x: (х) De weergavekolom (0..4)
:param y: De weergave rij (0.4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Stel de helderheid van de LED in op kolom ``x`` en rij ``y``. (pixel instellen)

Example: ``display.set_pixel(0, 0, 9)``

:param x: (х) De weergavekolom (0..4)
:param y: De weergave rij (0.4)
:param value: (waarde) De helderheid tussen 0 (uit) en 9 (helderst)"""
    ...

def clear() -> None:
    """Stel de helderheid van alle LED's in op 0 (uit). (wissen)

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Toont afbeeldingen, letters of cijfers op het LED-scherm. (toon)

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: (afbeelding) Een string, nummer, afbeelding of lijst van weer te geven afbeeldingen.
:param delay: (vertraging) Elke letter, cijfer of afbeelding wordt weergegeven met ``delay`` milliseconden tussen hen.
:param wait: (wacht) Als ``wait`` ``True``is, blokkeert deze functie totdat de animatie is voltooid, anders gebeurt de animatie op de achtergrond.
:param loop: Als ``loop`` ``True``is, zal de animatie voor altijd herhalen.
:param clear: (wissen) Als ``clear`` ``True``is, wordt het scherm gewist nadat de reeks is voltooid.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Scrolt een nummer of tekst op het LED display (scrollen)

Example: ``display.scroll('micro:bit')``

:param text: (tekst) De tekenreeks om te scrollen. Als ``text`` een geheel getal of float is, wordt het eerst geconverteerd naar een tekenreeks met behulp van ``str()``.
:param delay: (vertraging) De parameter ``delay`` bepaalt hoe snel de tekst scrolt.
:param wait: (wacht) Als ``wait`` ``True``is, blokkeert deze functie totdat de animatie is voltooid, anders gebeurt de animatie op de achtergrond.
:param loop: Als ``loop`` ``True``is, zal de animatie voor altijd herhalen.
:param monospace: Als ``monospace`` ``True`` is, nemen de tekens allemaal 5 pixel kolommen in de breedte in beslag, anders staat er precies 1 lege pixelkolom tussen elk teken terwijl ze scrollen.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Schakel het LED display in. (aan)

Example: ``display.on()``"""
    ...

def off() -> None:
    """Het uitschakelen van het LED display (uitschakelen van het scherm geeft je de mogelijkheid om de GPIO-pinnen opnieuw te gebruiken voor andere doeleinden). (uit)

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Controleer of de LED-weergave is ingeschakeld. (staat aan)

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Lees het licht niveau. (lees licht niveau)

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...