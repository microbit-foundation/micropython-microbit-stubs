"""Pinnen, afbeeldingen, geluiden, temperatuur en volume."""
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
    """Plan om een functie uit te voeren volgens het interval dat gespecificeerd is door het time argument  **V2 alleen**. (draai elke)

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

:param callback: Functie om op te roepen bij de meegeleverde interval. Weglaten wanneer je als decorator gebruikt.
:param days: (dagen) Stelt de dag markering in voor de planning.
:param h: (uur) Stelt de urenmarkering in voor de planning.
:param min: Stelt de minuut markering in voor de planning.
:param s: Stelt de seconde markering in voor de planning.
:param ms: Stelt de milliseconde markering in voor de planning."""

def panic(n: int) -> None:
    """Voer een paniekmodus in. (paniek)

Example: ``panic(127)``

:param n: Een willekeurig geheel getal <= 255 om een status aan te geven.

Requires restart."""

def reset() -> None:
    """Herstart het bord."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Zet een waarde om van een bereik naar een ander bereik van natuurlijke getallen. (schaal)

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: (waarde) Een getal om te converteren
:param from_: (van) Een getallen paar wat het bereik aangeeft vanwaar je wilt converteren
:param to: (naar) Een getallen paar om het bereik te definiëren waar je naar wilt converteren.
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Zet een waarde om van een bereik naar een ander bereik van decimale getallen. (schaal)

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: (waarde) Een getal om te converteren
:param from_: (van) Een getallen paar wat het bereik aangeeft vanwaar je wilt converteren
:param to: (naar) Een getallen paar om het bereik te definiëren waar je naar wilt converteren.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Wacht op ``n`` milliseconden. (slapen)

Example: ``sleep(1000)``

:param n: Het aantal milliseconden te wachten

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Bekijk de looptijd van het bord. (looptijd)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Krijg de temperatuur van de micro:bit in graden Celsius. (temperatuur)"""

def set_volume(v: int) -> None:
    """Stelt het volume in. (stel volume in)

Example: ``set_volume(127)``

:param v: een waarde tussen 0 (laag) en 255 (hoog).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """De klasse voor de knoppen ``button_a`` en ``button_b``. (knop)"""

    def is_pressed(self) -> bool:
        """Controleer of op de knop wordt gedrukt. (is ingedrukt)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Controleer of de knop was ingedrukt sinds het apparaat is gestart of de laatste keer dat deze methode is gebruikt. (was ingedrukt)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Krijg het totale aantal ingedrukte knoppen en reset dit totaal
naar nul voordat u terugkeert. (zie knop acties)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""Het object van de linker knop ``Button``. (knop a)"""
button_b: Button
"""Het object van de rechter knop ``Button``. (knop b)"""

class MicroBitDigitalPin:
    """Een digitale pin

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Haal de digitale waarde van de pincode op. (digitaal lezen)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Stel de digitale waarde van de pin in. (digitaal schrijven)

Example: ``pin0.write_digital(1)``

:param value: (waarde) 1 om de pin hoog of 0 om de pin laag in te stellen"""
        ...

    def set_pull(self, value: int) -> None:
        """Zet de pull-status op een van de drie mogelijke waarden: ``PULL_UP``, ``PULL_DOWN`` of ``NO_PULL``. (pull instellen)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (waarde) De pull-status van de relevante pincode, bijvoorbeeld ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Bekijk de pull status van een pin. (pull instellen)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Geeft de pinmodus weer. (Bekijk modus)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Voer een PWM-signaal uit op de pin, waarbij de taakcyclus proportioneel is aan ``value``. (analoge schrijven)

Example: ``pin0.write_analog(254)``

:param value: (waarde) Een geheel getal of een zwevend punt getal tussen 0 (0% tariefcyclus) en 1023 (100% belasting)."""

    def set_analog_period(self, period: int) -> None:
        """Stel de periode in van het PWM-signaal dat uitgevoerd wordt naar ``period`` in milliseconden. (gebruik analoge periode)

Example: ``pin0.set_analog_period(10)``

:param period: (periode) De periode in milliseconden met een minimale geldige waarde van 1 ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Stel de periode in van het PWM-signaal dat uitgevoerd wordt naar ``period`` in milliseconden. (microseconden analoge periode instellen)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (periode) De periode in microseconden met een minimumwaarde van 256 mres."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Een pin met analoge en digitale functies."""

    def read_analog(self) -> int:
        """Lees de spanning op de pin. (lees analoge)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Een pin met analoge, digitale en touch functies."""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Controleer of de pin aangeraakt wordt. (is aangeraakt)

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
        """Stel de aanraakmodus voor de pin in. (aanraakmodus instellen)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (waarde) ``CAPACITIVE`` of ``RESISTIVE`` van de relevante speler."""
        ...
pin0: MicroBitTouchPin
"""Pin met digitale, analoge en touch functies."""
pin1: MicroBitTouchPin
"""Pin met digitale, analoge en aanraak functies."""
pin2: MicroBitTouchPin
"""Pin met digitale, analoge en aanraak functies."""
pin3: MicroBitAnalogDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin4: MicroBitAnalogDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin5: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin6: MicroBitDigitalPin
"""Pin met digitale functies."""
pin7: MicroBitDigitalPin
"""Pin met digitale functies."""
pin8: MicroBitDigitalPin
"""Pin met digitale functies."""
pin9: MicroBitDigitalPin
"""Pin met digitale functies."""
pin10: MicroBitAnalogDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin11: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin12: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin13: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin14: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin15: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin16: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin19: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin20: MicroBitDigitalPin
"""Pin met digitale, analoge en aanraak functies."""
pin_logo: MicroBitTouchPin
"""Een aanraak gevoelige logo pin op de voorkant van de micro:bit, die standaard is ingesteld op capacitieve aanraking modus."""
pin_speaker: MicroBitAnalogDigitalPin
"""Een pin om de micro:bit luidspreker aan te spreken. (pin luidspreker)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Een afbeelding om te laten zien op het micro:bit LED display. (afbeelding)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Hart afbeelding (hart)"""
    HEART_SMALL: Image
    """Klein hart afbeelding. (hart klein)"""
    HAPPY: Image
    """Blije gezichtsafbeelding. (blij)"""
    SMILE: Image
    """Glimlach gezicht afbeelding. (glimlach)"""
    SAD: Image
    """Droevige gezichtsafbeelding. (verdrietig)"""
    CONFUSED: Image
    """Verward gezichtsafbeelding. (verward)"""
    ANGRY: Image
    """Boos gezichtsafbeelding. (kwaad)"""
    ASLEEP: Image
    """Slapend gezicht afbeelding. (in slaap)"""
    SURPRISED: Image
    """Verraste gezichtsafbeelding. (verrast)"""
    SILLY: Image
    """Gek gezichtsafbeelding. (gek)"""
    FABULOUS: Image
    """Zonnebril gezichtsafbeelding. (fantastisch)"""
    MEH: Image
    """Niet onder de indruk gezichtsafbeelding."""
    YES: Image
    """Aanvinken afbeelding. (ja)"""
    NO: Image
    """Kruis afbeelding. (nee)"""
    CLOCK12: Image
    """Afbeelding met lijn die naar 12.00 uur wijst. (klok 12)"""
    CLOCK11: Image
    """Afbeelding met lijn die naar 11.00 uur wijst. (klok 11)"""
    CLOCK10: Image
    """Afbeelding met lijn die naar 10.00 uur wijst. (klok 10)"""
    CLOCK9: Image
    """Afbeelding met lijn die naar 9.00 uur wijst. (klok 9)"""
    CLOCK8: Image
    """Afbeelding met lijn die naar 8.00 uur wijst. (klok 8)"""
    CLOCK7: Image
    """Afbeelding met lijn die naar 7.00 uur wijst. (klok 7)"""
    CLOCK6: Image
    """Afbeelding met lijn die naar 6.00 uur wijst. (klok 6)"""
    CLOCK5: Image
    """Afbeelding met lijn die naar 5.00 uur wijst. (klok 5)"""
    CLOCK4: Image
    """Afbeelding met lijn die naar 4.00 uur wijst. (klok 4)"""
    CLOCK3: Image
    """Afbeelding met lijn die naar 3.00 uur wijst. (klok 3)"""
    CLOCK2: Image
    """Afbeelding met lijn die naar 2 uur wijst. (klok2)"""
    CLOCK1: Image
    """Afbeelding met lijn die naar 1 uur wijst. (klok1)"""
    ARROW_N: Image
    """Afbeelding van pijl richting het noorden. (pijl n)"""
    ARROW_NE: Image
    """Afbeelding van pijl richting het noord oosten. (pijl NO)"""
    ARROW_E: Image
    """Afbeelding van pijl richting het oosten. (pijl e)"""
    ARROW_SE: Image
    """Afbeelding van pijl richting het zuid-oosten. (pijl ZO)"""
    ARROW_S: Image
    """Afbeelding van pijltje richting het zuiden. (pijl z)"""
    ARROW_SW: Image
    """Afbeelding van pijl richting het zuid-westen. (pijl ZW)"""
    ARROW_W: Image
    """Afbeelding van pijl richting het westen. (pijl w)"""
    ARROW_NW: Image
    """Afbeelding van pijl richting het noord-westen. (pijl NW)"""
    TRIANGLE: Image
    """Afbeelding van een driehoek die naar boven wijst. (driehoek)"""
    TRIANGLE_LEFT: Image
    """Afbeelding van een driehoek in de linker hoek. (Driehoek links)"""
    CHESSBOARD: Image
    """Alternatieve LED's verlichten in een schaakbord patroon. (schaakbord)"""
    DIAMOND: Image
    """Diamanten afbeelding. (diamant)"""
    DIAMOND_SMALL: Image
    """Kleine diamanten afbeelding. (diamant klein)"""
    SQUARE: Image
    """Vierkante afbeelding (vierkant)"""
    SQUARE_SMALL: Image
    """Kleine vierkante afbeelding. (vierkant klein)"""
    RABBIT: Image
    """Konijn afbeelding. (konijn)"""
    COW: Image
    """Koe afbeelding. (koe)"""
    MUSIC_CROTCHET: Image
    """Kwartnoot afbeelding. (muziek kwartnoot)"""
    MUSIC_QUAVER: Image
    """Kwartnoot afbeelding. (muziek kwartnoot)"""
    MUSIC_QUAVERS: Image
    """Koppel van kwartnoten afbeelding. (muziek kwartnoten)"""
    PITCHFORK: Image
    """Stemvork afbeelding. (stemvork)"""
    XMAS: Image
    """Kerstboom afbeelding. (kerstmis)"""
    PACMAN: Image
    """Pac-Man arcade karakterafbeelding. (Pacman)"""
    TARGET: Image
    """Doel afbeelding. (doel)"""
    TSHIRT: Image
    """T-shirt afbeelding."""
    ROLLERSKATE: Image
    """Rolschaats afbeelding. (rolschaatsen)"""
    DUCK: Image
    """Eend afbeelding. (eend)"""
    HOUSE: Image
    """Huis afbeelding. (huis)"""
    TORTOISE: Image
    """Schildpad afbeelding. (schildpad)"""
    BUTTERFLY: Image
    """Vlinder afbeelding. (vlinder)"""
    STICKFIGURE: Image
    """Stok figuur afbeelding. (stok figuur)"""
    GHOST: Image
    """Spook afbeelding. (spook)"""
    SWORD: Image
    """Zwaard afbeelding. (zwaard)"""
    GIRAFFE: Image
    """Giraffe afbeelding."""
    SKULL: Image
    """Schedel afbeelding. (doodshoofd)"""
    UMBRELLA: Image
    """Paraplu afbeelding. (paraplu)"""
    SNAKE: Image
    """Slang afbeelding. (slang)"""
    SCISSORS: Image
    """Schaar afbeelding. (schaar)"""
    ALL_CLOCKS: List[Image]
    """Een lijst met alle CLOCK_ afbeeldingen achter elkaar. (alle klokken)"""
    ALL_ARROWS: List[Image]
    """Een lijst met alle ARROW_ afbeeldingen in reeks. (alle pijlen)"""

    @overload
    def __init__(self, string: str) -> None:
        """Maak een afbeelding van een tekenreeks die beschrijft welke LED's zijn. (initialiseren)

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (tekenreeks) De tekenreeks die de afbeelding beschrijft."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Maak een lege afbeelding met ``width`` kolommen en ``height`` rijen. (initialiseren)

:param width: (breedte) Optionele breedte van de afbeelding
:param height: (hoogte) Optionele hoogte van de afbeelding
:param buffer: Optionele array of bytes van ``width``×``height`` integers in bereik 0-9 om de afbeelding te initialiseren

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Haal het aantal kolommen op. (breedte)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Krijg het aantal rijen. (hoogte)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Stel de helderheid van een pixel in. (pixel instellen)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: (х) Het kolom nummer
:param y: Het rij nummer
:param value: (waarde) De helderheid als een geheel getal tussen 0 (donker) en 9 (helder)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Krijg de helderheid van een pixel. (verkrijg pixel)

Example: ``my_image.get_pixel(0, 0)``

:param x: (х) Het kolom nummer
:param y: Het rij nummer
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Maak een nieuwe afbeelding door de afbeelding naar links te verschuiven. (verschuiving naar links)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: Het aantal te verschuiven kolommen
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Maak een nieuwe afbeelding door de afbeelding rechts te verschuiven. (verschuif Rechts)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: Het aantal te verschuiven kolommen
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Maak een nieuwe afbeelding door de afbeelding omhoog te schuiven. (verschuiving omhoog)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: Het aantal rijen om te verschuiven met
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Maak een nieuwe afbeelding door de afbeelding omlaag te verschuiven. (verschuif omlaag)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: Het aantal rijen om te verschuiven met
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Maak een nieuwe afbeelding door de afbeelding bij te snijden. (bij snijden)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: (х) De kolom verschuiving
:param y: De rij verschuiving
:param w: De bij snij breedte
:param h: (uur) Hoogte bijsnijden
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Maak een exacte kopie van de afbeelding. (kopiëer)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Maak een nieuwe afbeelding door de helderheid van de pixels in de
bronafbeelding om te draaien. (omkeren)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Stel de helderheid van alle pixels in de afbeelding in. (opvullen)

Example: ``my_image.fill(5)``

:param value: (waarde) De nieuwe helderheid als een getal tussen 0 (donker) en 9 (helder).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Kopieer een gebied van een andere afbeelding naar deze afbeelding.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: De bron afbeelding
:param x: (х) De begin kolom offset in de bron afbeelding
:param y: De beginkolom offset in de bronafbeelding
:param w: Het aantal te kopiëren kolommen
:param h: (uur) Het aantal te kopiëren rijen
:param xdest: De kolomverschuiving om aan te passen in deze afbeelding
:param ydest: De kolomverschuiving om aan te passen in deze afbeelding

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
        """Krijg een compacte tekenreeks die de afbeelding vertegenwoordigt."""
        ...

    def __str__(self) -> str:
        """Krijg een leesbare tekenreeks die de afbeelding vertegenwoordigt."""
        ...

    def __add__(self, other: Image) -> Image:
        """Maak een nieuwe afbeelding door de helderheidswaarden van de twee
afbeeldingen voor elke pixel toe te voegen. (toevoegen)

Example: ``Image.HEART + Image.HAPPY``

:param other: (overige) De afbeelding om toe te voegen."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Maak een nieuw beeld door de helderheidswaarden van de andere afbeelding van deze afbeelding af te trekken.

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (overige) De afbeelding om af te trekken."""
        ...

    def __mul__(self, n: float) -> Image:
        """Maak een nieuwe afbeelding door de helderheid van elke pixel te vermenigvuldigen met
``n``.

Example: ``Image.HEART * 0.5``

:param n: De waarde om te vermenigvuldigen."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Maak een nieuwe afbeelding door de helderheid van elke pixel te delen door
``n``.

Example: ``Image.HEART / 2``

:param n: De waarde om mee te delen."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Vertegenwoordigt de transitie van geluidsgebeurtenissen, van ``quiet`` tot ``loud`` zoals klappen of roepen. (luid)"""
    QUIET: SoundEvent
    """Vertegenwoordigt de transitie van geluidsgebeurtenissen, van ``loud`` tot ``quiet`` zoals spreken of achtergrondmuziek. (stil)"""

class Sound:
    """De ingebouwde geluiden kunnen worden aangeroepen met ``audio.play(Sound.NAME)``. (geluid)"""
    GIGGLE: Sound
    """Giechelgeluidjes (giechelen)"""
    HAPPY: Sound
    """Blij geluid. (blij)"""
    HELLO: Sound
    """Groet geluid. (hallo)"""
    MYSTERIOUS: Sound
    """Mysterieus geluid. (mysterieus)"""
    SAD: Sound
    """Droevig geluid. (verdrietig)"""
    SLIDE: Sound
    """Glij geluid. (Veeg)"""
    SOARING: Sound
    """Zweef geluid. (stijgend)"""
    SPRING: Sound
    """Spring geluid. (veer)"""
    TWINKLE: Sound
    """Twinkel geluid. (twinkeling)"""
    YAWN: Sound
    """Geeuwgeluiden (geeuw)"""