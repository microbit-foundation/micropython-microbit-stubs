"""Pokaż tekst, obrazy i animacje na wyświetlaczu 5x5 LED."""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Uzyskaj jasność LED w kolumnie ``x`` i w wierszu ``y``.

Example: ``display.get_pixel(0, 0)``

:param x: Wyświetlana kolumna (0..4)
:param y: Wyświetlany wiersz (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Ustaw jasność LED w kolumnie ``x`` i wierszu ``y``.

Example: ``display.set_pixel(0, 0, 9)``

:param x: Wyświetlana kolumna (0..4)
:param y: Wyświetlany wiersz (0..4)
:param value: Jasność między 0 (wyłączona) i 9 (jasna)"""
    ...

def clear() -> None:
    """Ustaw jasność wszystkich diod LED na 0 (wyłączone).

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Pokazuje obrazy, litery lub cyfry na wyświetlaczu LED.

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: Łańcuch, liczba, obraz lub lista obrazów do pokazania.
:param delay: Każda litera, cyfra lub obraz są wyświetlane z ``delay`` milisekundami między sobą.
:param wait: Jeśli ``wait`` jest ``True``, ta funkcja będzie blokować, aż zakończy się animacja, w przeciwnym razie animacja pojawi się w tle.
:param loop: Jeśli ``loop`` jest ``True``, animacja będzie powtarzana w nieskończoność.
:param clear: Jeśli ``clear`` jest ``True``, wyświetlacz zostanie wyczyszczony po zakończeniu sekwencji.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Przewija liczbę lub tekst na wyświetlaczu LED.

Example: ``display.scroll('micro:bit')``

:param text: Łańcuch do przewinięcia. Jeśli ``text`` jest liczbą całkowitą lub zmiennopozycyjną, najpierw zostanie przekonwertowany na łańcuch za pomocą ``str()``.
:param delay: Parametr ``delay`` kontroluje szybkość przewijania tekstu.
:param wait: Jeśli ``wait`` jest ``True``, ta funkcja będzie blokować, aż zakończy się animacja, w przeciwnym razie animacja pojawi się w tle.
:param loop: Jeśli ``loop`` jest ``True``, animacja będzie powtarzana w nieskończoność.
:param monospace: Jeśli ``monospace`` jest ``True``, wszystkie znaki zajmą co najwyżej 5 kolumn pikseli na szerokość, w przeciwnym razie będzie dokładnie 1 pusta kolumna pikseli pomiędzy każdym znakiem, gdy się przewijają.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Włącz wyświetlacz LED.

Example: ``display.on()``"""
    ...

def off() -> None:
    """Wyłącz wyświetlacz LED (wyłączenie wyświetlania pozwala na ponowne użycie pinów GPIO do innych celów).

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Sprawdź, czy wyświetlacz LED jest włączony.

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Odczytuj poziom światła.

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...