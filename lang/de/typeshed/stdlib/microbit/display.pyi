"""Texte, Bilder und Animationen auf dem 5x5 LED-Display anzeigen. (Display)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Ermittelt die Helligkeit der LED in Spalte ``x`` und Zeile ``y``.

Example: ``display.get_pixel(0, 0)``

:param x: Die Anzeige-Spalte (0..4)
:param y: Die Anzeigezeile (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Stellt die Helligkeit der LED in Spalte ``x`` und Zeile ``y`` ein.

Example: ``display.set_pixel(0, 0, 9)``

:param x: Die Anzeige-Spalte (0..4)
:param y: Die Anzeigezeile (0..4)
:param value: Die Helligkeit zwischen 0 (aus) und 9 (am hellsten)"""
    ...

def clear() -> None:
    """Setzt die Helligkeit aller LEDs auf 0 (aus).

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Zeigt Bilder, Buchstaben oder Ziffern auf der LED-Anzeige an.

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: Eine Zeichenkette, eine Zahl, ein Bild oder eine Liste von Bildern, die angezeigt werden sollen.
:param delay: Jeder Buchstabe, jede Ziffer oder jedes Bild wird mit einer Verzögerung von ``delay`` Millisekunden angezeigt.
:param wait: Wenn ``wait`` ``True`` ist, wird diese Funktion das Programm so lange anhalten, bis die Animation beendet ist, andernfalls wird die Animation im Hintergrund ausgeführt.
:param loop: Wenn ``loop`` ``True`` ist, wird die Animation endlos wiederholt.
:param clear: Wenn ``clear`` ``True`` ist, wird die Anzeige nach Beendigung der Sequenz gelöscht.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Scrollt eine Zahl oder einen Text auf dem LED-Display.

Example: ``display.scroll('micro:bit')``

:param text: Die zu scrollende Zeichenkette. Wenn ``text`` ein Integer oder Float ist, wird der Text vorher mit ``str()`` in einen String umgewandelt.
:param delay: Der Parameter ``delay`` bestimmt, wie schnell der Text gescrollt wird.
:param wait: Wenn ``wait`` ``True`` ist, wird diese Funktion das Programm anhalten, bis die Animation beendet ist, andernfalls läuft die Animation im Hintergrund ab.
:param loop: Wenn ``loop`` ``True`` ist, wird die Animation endlos wiederholt.
:param monospace: Wenn ``monospace`` ``True``ist, werden alle Zeichen 5 Pixel breit sein. Zwischen den Zeichen gibt es beim scrollen genau 1 leere Pixelspalte.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Schaltet das LED-Display ein.

Example: ``display.on()``"""
    ...

def off() -> None:
    """Schaltet das LED-Display aus (Deaktivieren des Displays ermöglicht es dir, die GPIO-Pins für andere Zwecke zu verwenden).

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Überprüft, ob die LED-Anzeige aktiviert ist.

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Bestimmt die Lichtintensität.

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...