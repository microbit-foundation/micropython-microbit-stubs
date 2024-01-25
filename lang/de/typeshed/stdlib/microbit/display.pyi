"""Texte, Bilder und Animationen auf dem 5x5 LED-Display anzeigen. (Display)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Ermittle die Helligkeit der LED auf Spalte ``x`` und Zeile ``y``. (Pixelwerte holen)

Example: ``display.get_pixel(0, 0)``

:param x: Die Anzeige-Spalte (0..4)
:param y: Die Anzeigezeile (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Ändere die Helligkeit der LED auf Spalte ``x`` und Zeile ``y``. (Pixelwerte setzen)

Example: ``display.set_pixel(0, 0, 9)``

:param x: Die Anzeige-Spalte (0..4)
:param y: Die Anzeigezeile (0..4)
:param value: (wert) Die Helligkeit zwischen 0 (aus) und 9 (am hellsten)"""
    ...

def clear() -> None:
    """Setzt die Helligkeit aller LEDs auf 0 (aus). (löschen)

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Zeigt Bilder, Buchstaben oder Ziffern auf der LED-Anzeige an.

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: Eine Zeichenkette, Nummer, Bild oder Liste der anzuzeigenden Bilder.
:param delay: (Verzögerung) Jeder Buchstabe, Ziffer oder Bild wird mit ``delay`` Millisekunden zwischen ihnen angezeigt.
:param wait: Wenn ``wait`` ``True``ist, wird diese Funktion blockiert, bis die Animation beendet ist, andernfalls wird die Animation im Hintergrund stattfinden.
:param loop: Wenn ``loop`` ``True``ist, wird sich die Animation für immer wiederholen.
:param clear: (löschen) Wenn ``clear`` ``True``ist, wird die Anzeige ausgeschaltet, nachdem die Sequenz beendet ist.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Scrollt eine Zahl oder einen Text auf dem LED-Display. (scrollen)

Example: ``display.scroll('micro:bit')``

:param text: Der zu wiederzugebende String. Wenn ``text`` eine Ganzzahl oder ein Float ist, wird er zuerst mit ``str()`` in einen String konvertiert.
:param delay: (Verzögerung) Der ``delay`` -Parameter bestimmt, wie schnell der Text scrollt.
:param wait: Wenn ``wait`` ``True``ist, wird diese Funktion blockiert, bis die Animation beendet ist, andernfalls wird die Animation im Hintergrund stattfinden.
:param loop: Wenn ``loop`` ``True``ist, wird sich die Animation für immer wiederholen.
:param monospace: (Monospace) Wenn ``monospace`` ``True``ist, werden alle Zeichen 5 Pixel breit sein. Zwischen den Zeichen gibt es beim scrollen genau 1 leere Pixelspalte.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Schalten Sie das LED-Display ein. (an)

Example: ``display.on()``"""
    ...

def off() -> None:
    """Schalten Sie die LED-Anzeige aus (das Deaktivieren des Displays erlaubt es Ihnen, die GPIO-Pins für andere Zwecke zu verwenden).

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Überprüfen Sie, ob die LED-Anzeige aktiviert ist. (ist an)

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Bestimmt die Lichtintensität. (bestimme Licht Intensität)

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...