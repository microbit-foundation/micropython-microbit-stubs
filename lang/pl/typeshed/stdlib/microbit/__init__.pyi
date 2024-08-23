"""Piny, obrazy, dźwięki, temperatura i głośność."""
from typing import Any, Callable, List, Optional, Tuple, Union, overload
from _typeshed import ReadableBuffer
from . import accelerometer as accelerometer
from . import audio as audio
from . import compass as compass
from . import display as display
from . import i2c as i2c
from . import microphone as microphone
from . import speaker as speaker
from . import spi as spi
from . import uart as uart

def run_every(callback: Optional[Callable[[], None]]=None, days: int=0, h: int=0, min: int=0, s: int=0, ms: int=0) -> Callable[[Callable[[], None]], Callable[[], None]]:
    """Zaplanuj uruchomienie funkcji w przedziale określonym przez argumenty czasu **tylko V2**.

Example: ``run_every(my_logging, min=5)``

``run_every`` can be used in two ways:

As a Decorator - placed on top of the function to schedule. For example::

    @run_every(h=1, min=20, s=30, ms=50)
    def my_function():
        # Do something here

As a Function - passing the callback as a positional argument. For example::

    def my_function():
        # Do something here
    run_every(my_function, s=30)

Each argument corresponds to a different time unit and they are additive.
So ``run_every(min=1, s=30)`` schedules the callback every minute and a half.

When an exception is thrown inside the callback function it deschedules the
function. To avoid this you can catch exceptions with ``try/except``.

:param callback: Funkcja wywoływana w podanym przedziale. Pomiń, jeśli używasz jako dekorator.
:param days: Ustawia oznaczenie dnia dla harmonogramu.
:param h: Ustawia znak godziny dla harmonogramu.
:param min: Ustawia znak minuty dla harmonogramu.
:param s: Ustawia znak sekundy dla harmonogramu.
:param ms: Ustawia znak milisekundy dla harmonogramu."""

def panic(n: int) -> None:
    """Wejdź w tryb paniki.

Example: ``panic(127)``

:param n: Dowolna liczba całkowita <= 255 dla wskazania statusu.

Requires restart."""

def reset() -> None:
    """Uruchom ponownie płytkę."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Konwertuje wartość z zakresu do zakresu liczb całkowitych.

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: Liczba do konwersji.
:param from_: Krotka do zdefiniowania zakresu dla konwersji z.
:param to: Krotka do zdefiniowania zakresu dla konwersji do.
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Konwertuje wartość z zakresu do zakresu o zmiennopozycyjnego.

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: Liczba do konwersji.
:param from_: Krotka do zdefiniowania zakresu dla konwersji z.
:param to: Krotka do zdefiniowania zakresu, na jaki konwertować.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Poczekaj ``n`` milisekund.

Example: ``sleep(1000)``

:param n: Liczba milisekund oczekiwania

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Uzyskaj czas pracy płytki.

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Uzyskaj temperaturę micro:bita w stopniach Celsjusza."""

def set_volume(v: int) -> None:
    """Ustawia głośność.

Example: ``set_volume(127)``

:param v: wartość między 0 (niska) a 255 (wysoka).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """Klasa dla przycisków ``button_a`` i ``button_b``."""

    def is_pressed(self) -> bool:
        """Sprawdź, czy przycisk jest naciśnięty.

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Sprawdź, czy przycisk został naciśnięty od momentu uruchomienia urządzenia lub kiedy ta metoda została wywołana.

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Pobierz sumę naciśnięć przycisków i zresetuje tę sumę
do zera przed powrotem.

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""Lewy przycisk ``Button`` obiekt."""
button_b: Button
"""Prawy przycisk ``Button`` obiekt."""

class MicroBitDigitalPin:
    """Cyfrowy pin.

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Uzyskaj cyfrową wartość pinu.

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Ustaw cyfrową wartość pinu.

Example: ``pin0.write_digital(1)``

:param value: 1, aby ustawić wysoką wartość pinu lub 0, aby ustawić niską wartość pinu"""
        ...

    def set_pull(self, value: int) -> None:
        """Ustaw stan ciągnięcia na jedną z trzech możliwych wartości: ``PULL_UP``, ``PULL_DOWN`` lub ``NO_PULL``.

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: Stan ciągnięcia z odpowiedniego pinu, np. ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Uzyskaj stan cignięcia na pinie.

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Zwraca tryb pinu.

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Wysyłaj sygnał PWM na pin, z cyklem pracy proporcjonalnym do ``value``.

Example: ``pin0.write_analog(254)``

:param value: Liczba całkowita lub liczba zmiennopozycyjna między 0 (0% cyklu pracy) a 1023 (100% cyklu pracy)."""

    def set_analog_period(self, period: int) -> None:
        """Ustaw okres wyjścia sygnału PWM na ``period`` w milisekundach.

Example: ``pin0.set_analog_period(10)``

:param period: Okres w milisekundach z minimalną poprawną wartością 1 ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Ustaw okres wyjścia sygnału PWM na ``period`` w mikrosekundach. (ustaw mikrosekundy okresu analogowego)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: Okres w mikrosekundach z minimalną poprawną wartością 256µs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Pin z funkcjami analogowymi i cyfrowymi."""

    def read_analog(self) -> int:
        """Odczytaj napięcie przyłożone do pinu.

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Pin z funkcjami analogowymi, cyfrowymi i dotykowymi."""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Sprawdź, czy pin został dotknięty.

Example: ``pin0.is_touched()``

The default touch mode for the pins on the edge connector is ``resistive``.
The default for the logo pin **V2** is ``capacitive``.

**Resistive touch**
This test is done by measuring how much resistance there is between the
pin and ground.  A low resistance gives a reading of ``True``.  To get
a reliable reading using a finger you may need to touch the ground pin
with another part of your body, for example your other hand.

**Capacitive touch**
This test is done by interacting with the electric field of a capacitor
using a finger as a conductor. `Capacitive touch
<https://www.allaboutcircuits.com/technical-articles/introduction-to-capacitive-touch-sensing>`_
does not require you to make a ground connection as part of a circuit.

:return: ``True`` if the pin is being touched with a finger, otherwise return ``False``."""
        ...

    def set_touch_mode(self, value: int) -> None:
        """Ustaw tryb dotykowy dla pinu.

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: ``CAPACITIVE`` lub ``RESISTIVE`` z odpowiedniego pinu."""
        ...
pin0: MicroBitTouchPin
"""Pin z funkcjami cyfrową, analogową i dotykową."""
pin1: MicroBitTouchPin
"""Pin z funkcjami cyfrową, analogową i dotykową."""
pin2: MicroBitTouchPin
"""Pin z funkcjami cyfrową, analogową i dotykową."""
pin3: MicroBitAnalogDigitalPin
"""Pin z funkcjami cyfrowymi i analogowymi."""
pin4: MicroBitAnalogDigitalPin
"""Pin z funkcjami cyfrowymi i analogowymi."""
pin5: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin6: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin7: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin8: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin9: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin10: MicroBitAnalogDigitalPin
"""Pin z funkcjami cyfrowymi i analogowymi."""
pin11: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin12: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin13: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin14: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin15: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin16: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin19: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin20: MicroBitDigitalPin
"""Pin z funkcjami cyfrowymi."""
pin_logo: MicroBitTouchPin
"""Wrażliwy na dotyk pin z logo z przodu micro:bita, który domyślnie jest ustawiony na pojemnościowy tryb dotykowy."""
pin_speaker: MicroBitAnalogDigitalPin
"""Pin adresujący głośnik micro:bita.

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Obraz wyświetlany na wyświetlaczu LED micro:bita.

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Obraz serca."""
    HEART_SMALL: Image
    """Obraz małego serca."""
    HAPPY: Image
    """Obraz szczęśliwej twarzy."""
    SMILE: Image
    """Obraz uśmiechniętej twarzy."""
    SAD: Image
    """Obraz smutnej twarzy."""
    CONFUSED: Image
    """Obraz zmieszanej twarzy."""
    ANGRY: Image
    """Obraz złej twarzy."""
    ASLEEP: Image
    """Obraz śpiącej twarzy."""
    SURPRISED: Image
    """Obraz zaskoczonej twarzy."""
    SILLY: Image
    """Obraz głupiej twarzy."""
    FABULOUS: Image
    """Obraz twarzy w okularach przeciwsłonecznych."""
    MEH: Image
    """Obraz niewzruszonej twarzy."""
    YES: Image
    """Haczyk na TAK."""
    NO: Image
    """Krzyżyk na NIE."""
    CLOCK12: Image
    """Obraz z linią wskazującą na godzinę 12."""
    CLOCK11: Image
    """Obraz z linią wskazującą na godzinę 11."""
    CLOCK10: Image
    """Obraz z linią wskazującą na godzinę 10."""
    CLOCK9: Image
    """Obraz z linią wskazującą na godzinę 9."""
    CLOCK8: Image
    """Obraz z linią wskazującą na godzinę 8."""
    CLOCK7: Image
    """Obraz z linią wskazującą na godzinę 7."""
    CLOCK6: Image
    """Obraz z linią wskazującą na godzinę 6."""
    CLOCK5: Image
    """Obraz z linią wskazującą na godzinę 5."""
    CLOCK4: Image
    """Obraz z linią wskazującą na godzinę 4."""
    CLOCK3: Image
    """Obraz z linią wskazującą na godzinę 3."""
    CLOCK2: Image
    """Obraz z linią wskazującą na godzinę 2."""
    CLOCK1: Image
    """Obraz z linią wskazującą na godzinę 1."""
    ARROW_N: Image
    """Obraz strzałki wskazującej północ."""
    ARROW_NE: Image
    """Obraz strzałki wskazującej północny wschód."""
    ARROW_E: Image
    """Obraz strzałki wskazującej wschód."""
    ARROW_SE: Image
    """Obraz strzałki wskazującej południowy wschód."""
    ARROW_S: Image
    """Obraz strzałki wskazującej południe."""
    ARROW_SW: Image
    """Obraz strzałki wskazującej południowy zachód."""
    ARROW_W: Image
    """Obraz strzałki wskazującej zachód."""
    ARROW_NW: Image
    """Obraz strzałki wskazującej północny zachód."""
    TRIANGLE: Image
    """Obraz trójkąta skierowanego do góry."""
    TRIANGLE_LEFT: Image
    """Obraz trójkąta w lewym rogu."""
    CHESSBOARD: Image
    """Diody LED świecą naprzemiennie w układzie szachownicy."""
    DIAMOND: Image
    """Obraz diamentu."""
    DIAMOND_SMALL: Image
    """Obraz małego diamentu."""
    SQUARE: Image
    """Obraz kwadratu."""
    SQUARE_SMALL: Image
    """Obraz małego kwadratu."""
    RABBIT: Image
    """Obraz królika."""
    COW: Image
    """Obraz krowy."""
    MUSIC_CROTCHET: Image
    """Obraz ćwierćnuty."""
    MUSIC_QUAVER: Image
    """Obraz nuty ósemki."""
    MUSIC_QUAVERS: Image
    """Obraz pary nut ósemek."""
    PITCHFORK: Image
    """Obraz kamertonu."""
    XMAS: Image
    """Obraz choinki."""
    PACMAN: Image
    """Obrazek postaci arcade Pac-Man"""
    TARGET: Image
    """Obraz celu."""
    TSHIRT: Image
    """Obraz t-shirt."""
    ROLLERSKATE: Image
    """Obraz Rollerskate."""
    DUCK: Image
    """Obraz kaczki."""
    HOUSE: Image
    """Obraz domu."""
    TORTOISE: Image
    """Obraz żółwia."""
    BUTTERFLY: Image
    """Obraz motyla."""
    STICKFIGURE: Image
    """Obraz przyklejonej figury."""
    GHOST: Image
    """Obraz ducha."""
    SWORD: Image
    """Obraz miecza."""
    GIRAFFE: Image
    """Obraz żyrafy."""
    SKULL: Image
    """Obraz czaszki."""
    UMBRELLA: Image
    """Obraz parasola."""
    SNAKE: Image
    """Obraz węża."""
    SCISSORS: Image
    """Obraz nożyczek."""
    ALL_CLOCKS: List[Image]
    """Lista zawierająca wszystkie obrazy CLOCK_ po kolei."""
    ALL_ARROWS: List[Image]
    """Lista zawierająca wszystkie obrazy ARROW_ po kolei."""

    @overload
    def __init__(self, string: str) -> None:
        """Utwórz obraz z łańcucha opisującego, które diody LED są zapalone.

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: Łańcuch opisujący obraz."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Utwórz pusty obraz z ``width`` kolumnami i ``height`` wierszami.

:param width: Opcjonalna szerokość obrazu
:param height: Opcjonalna wysokość obrazu
:param buffer: Opcjonalna tablica lub bajty ``width``×``height`` liczb całkowitych w zakresie 0-9 do zainicjowania obrazu

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Ustal liczbę kolumn

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Uzyskaj liczbę wierszy

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Ustaw jasność piksela.

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: Numer kolumny
:param y: Numer wiersza
:param value: Jasność jako liczba całkowita między 0 (ciemny) i 9 (jasna)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """uzyskaj jasność piksela.

Example: ``my_image.get_pixel(0, 0)``

:param x: Numer kolumny
:param y: Numer wiersza
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Utwórz nowy obraz przesuwając ten obraz w lewo.

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: Liczba kolumn do przesunięcia
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Utwórz nowy obraz, przesuwając ten obraz w prawo.

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: Liczba kolumn do przesunięcia
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Utwórz nowy obraz, przesuwając obraz do góry.

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: Liczba wierszy do przesunięcia o
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Utwórz nowy obraz, przesuwając obraz do dołu.

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: Liczba wierszy do przesunięcia o
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Utwórz nowy obraz przez przycięcie zdjęcia.

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: Kolumna przesunięcia przycięcia
:param y: Wiersz przesunięcia przycięcia
:param w: Szerokość przycięcia
:param h: Wysokość przycięcia
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Utwórz dokładną kopię obrazu.

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Utwórz nowy obraz przez odwrócenie jasności pikseli w obrazie źródłowym.

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Ustaw jasność wszystkich pikseli obrazka.

Example: ``my_image.fill(5)``

:param value: Nowa jasność jako liczba między 0 (ciemny) a 9 (jasny).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Skopiuj obszar z innego obrazu na ten obraz.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: Zdjęcie źródłowe
:param x: Początkowe przesunięcie kolumny w obrazie źródłowym
:param y: Początkowe przesunięcie wiersza na obrazie źródłowym
:param w: Liczba kolumn do skopiowania
:param h: Liczba wierszy do skopiowania
:param xdest: Przesunięcie kolumny do modyfikacji na tym obrazie
:param ydest: Przesunięcie wiersza do modyfikacji na tym obrazie

Pixels outside the source image are treated as having a brightness of 0.

``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()``
and ``crop()`` can are all implemented by using ``blit()``.

For example, img.crop(x, y, w, h) can be implemented as::

    def crop(self, x, y, w, h):
        res = Image(w, h)
        res.blit(self, x, y, w, h)
        return res"""
        ...

    def __repr__(self) -> str:
        """Uzyskaj kompaktową reprezentację obrazu w postaci łańcucha."""
        ...

    def __str__(self) -> str:
        """Uzyskaj czytelną reprezentację obrazu w postaci łańcucha."""
        ...

    def __add__(self, other: Image) -> Image:
        """Utwórz nowy obraz, dodając wartości jasności z dwóch
obrazów dla każdego piksela.

Example: ``Image.HEART + Image.HAPPY``

:param other: Obraz do dodania."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Utwórz nowy obraz, odejmując wartości jasności
innego obrazu od tego obrazu.

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: Obraz do odjęcia."""
        ...

    def __mul__(self, n: float) -> Image:
        """Utwórz nowy obraz, mnożąc jasność każdego piksela przez
``n``.

Example: ``Image.HEART * 0.5``

:param n: Wartość do mnożenia przez."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Utwórz nowy obraz, dzieląc jasność każdego piksela przez
``n``.

Example: ``Image.HEART / 2``

:param n: Wartość do dzielenia przez."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Przedstawia przejście zdarzeń dźwiękowych z ``quiet`` do ``loud``, jak klaskanie lub krzyczenie."""
    QUIET: SoundEvent
    """Przedstawia przejście zdarzeń dźwiękowych z ``loud`` do ``quiet``, jak mówienie lub muzyka w tle."""

class Sound:
    """Wbudowane dźwięki można wywołać za pomocą ``audio.play(Sound.NAME)``."""
    GIGGLE: Sound
    """Chichoczący dźwięk."""
    HAPPY: Sound
    """Szczęśliwy dźwięk."""
    HELLO: Sound
    """Dźwięk powitania."""
    MYSTERIOUS: Sound
    """Tajemniczy dźwięk."""
    SAD: Sound
    """Smutny dźwięk."""
    SLIDE: Sound
    """Przesuwający się dźwięk."""
    SOARING: Sound
    """Wznoszący się dźwięk."""
    SPRING: Sound
    """Wiosny dźwięk."""
    TWINKLE: Sound
    """Migoczący dźwięk."""
    YAWN: Sound
    """Dźwięk ziewania."""