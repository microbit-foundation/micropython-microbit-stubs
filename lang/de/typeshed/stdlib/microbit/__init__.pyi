"""Pins, Bilder, Töne, Temperatur und Lautstärke."""
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
    """Plant die Ausführung einer Funktion in dem durch die Zeitargumente festgelegten Intervall. **Nur micro:bit\xa0V2**.

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

:param callback: Funktion, die in dem angegebenen Intervall aufgerufen wird. Bei Verwendung als Dekorator weglassen.
:param days: (tage) Legt den Tag für die Planung fest.
:param h: Legt die Uhrzeit für die Planung fest.
:param min: Legt die Minute für die Planung fest.
:param s: Legt die Sekunde für die Planung fest.
:param ms: Legt die Millisekunde für die Planung fest."""

def panic(n: int) -> None:
    """In einen Panik-Modus wechseln.

Example: ``panic(127)``

:param n: Eine beliebige ganze Zahl <= 255, um einen Status anzugeben.

Requires restart."""

def reset() -> None:
    """Board neu starten."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Konvertiert einen Wert aus einem Bereich in einen Ganzzahlenbereich.

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: (wert) Eine umzurechnende Zahl.
:param from_: Ein Tupel, das den Bereich definiert, aus dem konvertiert werden soll.
:param to: Ein Tupel, das den Bereich definiert, in den konvertiert werden soll.
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Konvertiert einen Wert von einem Bereich in einen Gleitkommabereich.

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: Eine umzurechnende Zahl.
:param from_: Ein Tupel, das den Bereich definiert, aus dem konvertiert werden soll.
:param to: Ein Tupel, das den Bereich definiert, in den konvertiert werden soll.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Wartet ``n`` Millisekunden.

Example: ``sleep(1000)``

:param n: Die Anzahl der zu wartenden Millisekunden

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Ermittelt die Laufzeit des Boards.

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Ermittelt die Temperatur des micro:bit in Grad Celcius."""

def set_volume(v: int) -> None:
    """Legt die Lautstärke fest.

Example: ``set_volume(127)``

:param v: ein Wert zwischen 0 (niedrig) und 255 (hoch).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """Die Klasse für die Tasten ``button_a`` und ``button_b``."""

    def is_pressed(self) -> bool:
        """Überprüft, ob die Taste gedrückt ist.

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Überprüft, ob die Taste seit dem Start des Geräts oder dem letzten Aufruf dieser Methode gedrückt wurde.

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Ermittelt die Gesamtzahl der Tastendrücke und setzt diese Summe auf Null zurück, bevor sie zurückgegeben wird.

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""Das Objekt ``Button`` der linken Taste."""
button_b: Button
"""Das Objekt ``Button`` der rechten Taste."""

class MicroBitDigitalPin:
    """Ein digitaler Pin.

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Ermittelt den digitalen Wert des Pins.

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Stellt den digitalen Wert des Pins ein. (digital schreiben)

Example: ``pin0.write_digital(1)``

:param value: (wert) 1, um den Pin zu aktivieren, oder 0, um den Pin zu deaktivieren"""
        ...

    def set_pull(self, value: int) -> None:
        """Setze den Status des Pull-Widerstands auf einen von drei möglichen Werten: ``PULL_UP``, ``PULL_DOWN`` oder ``NO_PULL``. (setze Pull-Widerstand)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (wert) Der Status des Pull-Widerstands vom relevanten Pin, z.B. ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Abrufen des Status des Pull-Widerstands eines Pins. (gib Pull-Widerstand)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Gibt den Pin-Modus zurück. (gib Pin-Modus)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Gib ein PWM-Signal am Pin aus, bei dem das Verhältnis von An- zu Auszeit proportional zu ``value`` ist. (analog schreiben)

Example: ``pin0.write_analog(254)``

:param value: (wert) Eine Ganzzahl oder eine Gleitpunktzahl zwischen 0 (0% Einschaltdauer) und 1023 (100% Einschaltdauer)."""

    def set_analog_period(self, period: int) -> None:
        """Setze die Periodendauer für die Ausgabe des PWM-Signals auf ``period`` in Mikrosekunden. (setze analoge Periodendauer)

Example: ``pin0.set_analog_period(10)``

:param period: (Periodendauer) Der Periodendauer in Millisekunden mit einem Mindestwert von 1ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Setzt den Zeitraum des PWM-Signals, das ausgegeben wird, auf ``period`` in Mikrosekunden. (setze analoge Periodendauer)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (Periodendauer) Die Periodendauer in Mikrosekunden mit einem Mindestwert von 256\xa0μs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Ein Pin, der analogen und digitalen Signale erlaubt."""

    def read_analog(self) -> int:
        """Einlesen der Spannung, die am Pin anliegt. (analog lesen)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Ein Pin mit analogen, digitalen und Touchfunktionen."""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Überprüft, ob der Pin berührt wird. (wird berührt)

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
        """Legt den Berührungsmodus für den Pin fest. (definiert Berührungsmodus)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (wert) ``CAPACITIVE`` oder ``RESISTIVE`` Touchmodus des entsprechenden Pins."""
        ...
pin0: MicroBitTouchPin
"""Pin mit digitalen, analogen und Touchfunktionen."""
pin1: MicroBitTouchPin
"""Pin mit digitalen, analogen und Touchfunktionen."""
pin2: MicroBitTouchPin
"""Pin mit digitalen, analogen und Touchfunktionen."""
pin3: MicroBitAnalogDigitalPin
"""Pin mit digitalen und analogen Funktionen."""
pin4: MicroBitAnalogDigitalPin
"""Pin mit digitalen und analogen Funktionen."""
pin5: MicroBitDigitalPin
"""Pin mit Unterstützung für digitale Signale."""
pin6: MicroBitDigitalPin
"""Pin mit Unterstützung für digitale Signale."""
pin7: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin8: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin9: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin10: MicroBitAnalogDigitalPin
"""Pin mit digitalen und analogen Funktionen."""
pin11: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin12: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin13: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin14: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin15: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin16: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin19: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin20: MicroBitDigitalPin
"""Pin mit digitalen Funktionen."""
pin_logo: MicroBitTouchPin
"""Ein berührungsempfindlicher Logo-Pin auf der Vorderseite des micro:bit, der standardmäßig auf den kapazitiven Berührungsmodus eingestellt ist."""
pin_speaker: MicroBitAnalogDigitalPin
"""Ein Pin zur Ansteuerung des micro:bit-Lautsprechers.

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Ein Bild, das auf dem micro:bit LED-Display angezeigt werden soll.

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Herz-Bild."""
    HEART_SMALL: Image
    """Kleines Herz-Bild."""
    HAPPY: Image
    """Glückliches Gesichtsbild."""
    SMILE: Image
    """Lächelndes Gesichtsbild."""
    SAD: Image
    """Trauriges Gesichtsbild."""
    CONFUSED: Image
    """Verwirrtes Gesichtsbild."""
    ANGRY: Image
    """Wütendes Gesichtsbild."""
    ASLEEP: Image
    """Schlafendes Gesichtsbild."""
    SURPRISED: Image
    """Überraschtes Gesichtsbild."""
    SILLY: Image
    """Albernes Gesichtsbild."""
    FABULOUS: Image
    """Bild mit Sonnenbrillengesicht. (fabelhaft)"""
    MEH: Image
    """Gleichgültiges Gesicht Bild."""
    YES: Image
    """abgehakt-Bild"""
    NO: Image
    """angekreuzt-Bild"""
    CLOCK12: Image
    """Bild mit Linie, die auf 12 Uhr zeigt."""
    CLOCK11: Image
    """Bild mit Linie, die auf 11 Uhr zeigt."""
    CLOCK10: Image
    """Bild mit Linie, die auf 10 Uhr zeigt."""
    CLOCK9: Image
    """Bild mit Linie, die auf 9 Uhr zeigt."""
    CLOCK8: Image
    """Bild mit Linie, die auf 8 Uhr zeigt."""
    CLOCK7: Image
    """Bild mit Linie, die auf 7 Uhr zeigt."""
    CLOCK6: Image
    """Bild mit Linie, die auf 6 Uhr zeigt."""
    CLOCK5: Image
    """Bild mit Linie, die auf 5 Uhr zeigt."""
    CLOCK4: Image
    """Bild mit Linie, die auf 4 Uhr zeigt."""
    CLOCK3: Image
    """Bild mit Linie, die auf 3 Uhr zeigt."""
    CLOCK2: Image
    """Bild mit Linie, die auf 2 Uhr zeigt."""
    CLOCK1: Image
    """Bild mit Linie, die auf 1 Uhr zeigt."""
    ARROW_N: Image
    """Bild eines Pfeils, der nach Norden zeigt."""
    ARROW_NE: Image
    """Bild eines Pfeils, der nach Nordosten zeigt."""
    ARROW_E: Image
    """Bild eines Pfeils, der nach Osten zeigt."""
    ARROW_SE: Image
    """Bild eines Pfeils, der nach Südosten zeigt."""
    ARROW_S: Image
    """Bild eines Pfeils, der nach Süden zeigt."""
    ARROW_SW: Image
    """Bild eines Pfeils, der nach Südwesten zeigt."""
    ARROW_W: Image
    """Bild eines Pfeils, der nach Westen zeigt."""
    ARROW_NW: Image
    """Bild eines Pfeils, der nach Nordwesten zeigt."""
    TRIANGLE: Image
    """Bild eines Dreiecks, das nach oben zeigt."""
    TRIANGLE_LEFT: Image
    """Bild eines Dreiecks in der linken Ecke."""
    CHESSBOARD: Image
    """Abwechselnd leuchtende LEDs in einem Schachbrettmuster."""
    DIAMOND: Image
    """Diamant-Bild."""
    DIAMOND_SMALL: Image
    """Kleines Diamant-Bild."""
    SQUARE: Image
    """Quadrat-Bild"""
    SQUARE_SMALL: Image
    """Kleines Quadrat-Bild."""
    RABBIT: Image
    """Kaninchen-Bild."""
    COW: Image
    """Kuh-Bild."""
    MUSIC_CROTCHET: Image
    """Viertelnoten-Bild."""
    MUSIC_QUAVER: Image
    """Achtelnoten-Bild."""
    MUSIC_QUAVERS: Image
    """Achtelnotenpaar-Bild."""
    PITCHFORK: Image
    """Heugabel-Bild"""
    XMAS: Image
    """Weihnachtsbaum-Bild."""
    PACMAN: Image
    """Pac-Man Spielfigurenbild."""
    TARGET: Image
    """Ziel-Bild"""
    TSHIRT: Image
    """T-Shirt-Bild."""
    ROLLERSKATE: Image
    """Rollerskate-Bild."""
    DUCK: Image
    """Ente-Bild"""
    HOUSE: Image
    """Haus-Bild"""
    TORTOISE: Image
    """Schildkröte-Bild"""
    BUTTERFLY: Image
    """Schmetterling-Bild."""
    STICKFIGURE: Image
    """Strichmännchen-Bild."""
    GHOST: Image
    """Geist-Bild."""
    SWORD: Image
    """Schwert-Bild"""
    GIRAFFE: Image
    """Giraffe-Bild."""
    SKULL: Image
    """Schädel-Bild."""
    UMBRELLA: Image
    """Bild eines Schirms."""
    SNAKE: Image
    """Bild einer Schlange. (Schlange)"""
    SCISSORS: Image
    """BIld einer Schere. (Schere)"""
    ALL_CLOCKS: List[Image]
    """Eine Liste mit allen CLOCK_ Bildern. (alle Uhren)"""
    ALL_ARROWS: List[Image]
    """Eine Liste mit allen ARROW_ Bildern. (alle Pfeile)"""

    @overload
    def __init__(self, string: str) -> None:
        """Erstellt ein Bild aus einer Zeichenkette, die beschreibt, welche LEDs leuchten.

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (Zeichenkette) Eine Zeichenkette, die das Bild beschreibt."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Erstelle ein leeres Bild mit ``width`` Spalten und ``height`` Zeilen.

:param width: (Breite) Optionale Breite des Bildes
:param height: (Höhe) Optionale Höhe des Bildes
:param buffer: (Puffer) Optionales Array oder Bytes von ``width``×``height`` Ganzzahlen im Bereich 0-9 um das Bild zu initialisieren

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Ermittelt die Anzahl der Spalten. (Breite)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Ermittelt die Anzahl der Zeilen. (Höhe)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Legt die Helligkeit eines Pixels fest. (Pixelwerte setzen)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: Die Spaltennummer
:param y: Die Zeilennummer
:param value: (wert) Die Helligkeit als Ganzzahl zwischen 0 (dunkel) und 9 (hell)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Ermittle die Helligkeit eines Pixels. (Pixelwerte holen)

Example: ``my_image.get_pixel(0, 0)``

:param x: Die Spaltennummer
:param y: Die Zeilennummer
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Erstellt ein neues Bild, indem das Bild nach links verschoben wird. (links verschieben)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: Die Anzahl der Spalten um die verschoben wird
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Erstellt ein neues Bild, indem das Bild nach rechts verschoben wird. (rechts verschieben)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: Die Anzahl der Spalten um die verschoben wird
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Erstellt ein neues Bild, indem das Bild nach oben verschoben wird. (nach oben verschieben)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: Die Anzahl der Zeilen um die verschoben wird
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Erstellt ein neues Bild, indem das Bild nach unten verschoben wird. (nach unten verschieben)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: Die Anzahl der Zeilen um die verschoben wird
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Erstellen Sie ein neues Bild, indem das Bild zugeschnitten wird.

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: Die Offset-Spalte des Zuschneidens
:param y: Die Offset-Zeile des Zuschneidens
:param w: Die Zuschneide-Breite
:param h: Die Zuschneide-Höhe
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Erstellt eine exakte Kopie des Bildes. (kopieren)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Erstellt ein neues Bild, indem es die Helligkeit der Pixel des Ausgangsbildes invertiert.

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Legt die Helligkeit für alle Pixel des Bildes fest.

Example: ``my_image.fill(5)``

:param value: Die neue Helligkeit als Zahl zwischen 0 (dunkel) und 9 (hell).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Kopiert einen Bereich aus einem anderen Bild in dieses Bild.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: Das Ausgangsbild
:param x: Der Anfangsspalten-Offset im Ausgangsbild
:param y: Der Anfangszeilen-Offset im Ausgangsbild
:param w: Die Anzahl der zu kopierenden Spalten
:param h: Die Anzahl der zu kopierenden Zeilen
:param xdest: Der Spalten-Offset, der in diesem Bild geändert werden soll
:param ydest: Der Zeilen-Offset, der in diesem Bild geändert werden soll

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
        """Liefert eine kompakte Stringrepräsentation des Bildes."""
        ...

    def __str__(self) -> str:
        """Liefert eine lesbare String-Repräsentation des Bildes."""
        ...

    def __add__(self, other: Image) -> Image:
        """Erstellt ein neues Bild, indem für jedes Pixel die Helligkeitswerte der beiden Bilder addiert werden.

Example: ``Image.HEART + Image.HAPPY``

:param other: Das zu addierende Bild."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Erstellt ein neues Bild, indem für jedes Pixel die Helligkeitswerte der beiden Bilder subtrahiert werden.

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: Das zu subtrahierende Bild."""
        ...

    def __mul__(self, n: float) -> Image:
        """Erstellt ein neues Bild, indem der Helligkeitswert jedes Pixels mit ``n`` multipliziert wird.

Example: ``Image.HEART * 0.5``

:param n: Der Wert, mit dem multipliziert werden soll."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Erstellt ein neues Bild, indem der Helligkeitswert jedes Pixels durch ``n`` dividiert wird.

Example: ``Image.HEART / 2``

:param n: Der Wert, durch den dividiert werden soll."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Stellt den Übergang von Klangereignissen von ``quiet`` auf ``loud`` dar; wie beim Klatschen oder Rufen."""
    QUIET: SoundEvent
    """Stellt den Übergang von akustischen Ereignissen, wie Sprechen oder Hintergrundmusik, von ``loud`` zu ``quiet`` dar. (stumm)"""

class Sound:
    """Die eingebauten Klänge können mit ``audio.play(Sound.NAME)`` aufgerufen werden."""
    GIGGLE: Sound
    """Kichern-Sound."""
    HAPPY: Sound
    """Happy-Sound."""
    HELLO: Sound
    """Begrüßung-Sound"""
    MYSTERIOUS: Sound
    """Geheimnisvoll-Sound"""
    SAD: Sound
    """Traurig-Sound."""
    SLIDE: Sound
    """Gleitender Ton."""
    SOARING: Sound
    """Aufsteigender Klang. (aufsteigend)"""
    SPRING: Sound
    """Springfeder Klang (Sppringfeder)"""
    TWINKLE: Sound
    """Funkeln Klang (Funkeln)"""
    YAWN: Sound
    """Gähnen Klang"""