"""Pins, imatges, sons, temperatura i volum."""
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
    """Programa l'execució d'una funció a cada interval especificat pels arguments de temps  **només V2**.

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

:param callback: Funció a cridar a l'interval previst. Omet quan el fas servir com decorador.
:param days: (dies) Estableix la marca del dia per la programació
:param h: Estableix la marca de l'hora per la programació
:param min: Estableix la marca del minut per la programació
:param s: Estableix la marca del segon per la programació
:param ms: Estableix la marca del mil·lisegon per la programació"""

def panic(n: int) -> None:
    """Entrar en mode pànic. (pànic)

Example: ``panic(127)``

:param n: Un nombre enter arbitrari <= 255 per indicar un estat.

Requires restart."""

def reset() -> None:
    """Reinicialitza la placa. (reiniciar)"""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Converteix un valor d'un interval a un interval de nombre enter. (escala)

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: (valor) Un nombre a convertir.
:param from_: (des de) Una tupla des d'on definir l'interval a convertir
:param to: (a) Una tupla que defineix l'interval d'arribada
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Converteix un valor d'un interval a un altre interval de coma flotant. (escala)

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: (valor) Un nombre a convertir.
:param from_: (des de) Una tupla des d'on definir l'interval a convertir
:param to: (a) Una tupla que defineix l'interval d'arribada de la conversió.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Espera per ``n`` mil·lisegons. (dormir)

Example: ``sleep(1000)``

:param n: El nombre de mil·lisegons a esperar

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Obté el temps d'execució de la placa. (temps d'execució)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Obté la temperatura de la micro:bit en graus Celsius. (temperatura)"""

def set_volume(v: int) -> None:
    """Configura el volum (assigna volum)

Example: ``set_volume(127)``

:param v: un valor entre 0 (baix) i 255 (alt).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """La classe dels botons ``button_a`` i ``button_b``. (botó)"""

    def is_pressed(self) -> bool:
        """Verifica si el botó està premut. (és premut)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Verifica si el botó ha estat premut d'ençà que el dispositiu va arrancar o l'última vegada que aquest mètode va ser cridat. (ha estat premut)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Obté el total acumulat de pressions dels botons i restableix aquest total
a zero abans de tornar. (obté pitjades)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""L'objecte botó esquerre ``Button`` . (botó a)"""
button_b: Button
"""L'objecte el botó dret ``Button``. (botó b)"""

class MicroBitDigitalPin:
    """Un pin digital.

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Obté el valor digital del pin. (llegeix digital)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Assigna el valor digital del pin. (escriu digital)

Example: ``pin0.write_digital(1)``

:param value: (valor) 1 per posar el pin alt o 0 per posar el pin baix"""
        ...

    def set_pull(self, value: int) -> None:
        """Configura les resistències de pull-up/pull-down un dels tres valors possibles: ``PULL_UP``, ``PULL_DOWN`` o ``NO_PULL``. (configuració de les resistències de pull up/down)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (valor) L'estat del pull-up/pull-down del pin corresponent, per ex. ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Obté l'estat de pull-up/pull-down d'un pin.

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Retorna el mode del pin (obté el mode)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Genera un senyal PWM al pin, amb el cicle de treball proporcional a ``value``. (escriu analògic)

Example: ``pin0.write_analog(254)``

:param value: (valor) Un nombre enter o de coma flotant entre 0 (cicle de treball del 0%) i 1023 (cicle de treball del 100%)."""

    def set_analog_period(self, period: int) -> None:
        """Estableix el període del senyal PWM a ``period`` en mil·lisegons. (configura el període amb un valor analògic)

Example: ``pin0.set_analog_period(10)``

:param period: (període) El període en mil·lisegons amb un valor mínim vàlid d'1\u202fms"""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Estableix el període del senyal PWM a ``period`` microsegons. (configura el període amb un valor analògic en microsegons)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (període) El període en microsegons amb un valor vàlid mínim  de 256\u202fµs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Un pin amb funcions analògiques i digitals."""

    def read_analog(self) -> int:
        """Llegeix el voltatge aplicat al pin. (llegeix analògic)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Un pin amb  característiques analògiques, digitals i tàctils."""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Comprova si el pin està sent tocat. (està tocat)

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
        """Estableix el mode tàctil per al pin. (estableix el mode tàctil)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (valor) ``CAPACITIVE`` o ``RESISTIVE`` del pin corresponent."""
        ...
pin0: MicroBitTouchPin
"""Pin amb característiques digitals, analògiques i tàctils."""
pin1: MicroBitTouchPin
"""Pin amb característiques digitals, analògiques i tàctils."""
pin2: MicroBitTouchPin
"""Pin amb característiques digitals, analògiques i tàctils."""
pin3: MicroBitAnalogDigitalPin
"""Pin amb característiques digitals i analògiques."""
pin4: MicroBitAnalogDigitalPin
"""Pin amb característiques digitals i analògiques."""
pin5: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin6: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin7: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin8: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin9: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin10: MicroBitAnalogDigitalPin
"""Pin amb característiques digitals i analògiques."""
pin11: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin12: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin13: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin14: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin15: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin16: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin19: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin20: MicroBitDigitalPin
"""Pin amb característiques digitals."""
pin_logo: MicroBitTouchPin
"""Un logotip tàctil a la part frontal de la micro:bit, que per defecte està establert al mode tàctil capacitiu. (pin logotip)"""
pin_speaker: MicroBitAnalogDigitalPin
"""Un pin per adreçar-se a l'altaveu micro:bit. (pin altaveu)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Una imatge per mostrar a la pantalla LED de micro:bit. (imatge)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Imatge d'un cor. (cor)"""
    HEART_SMALL: Image
    """Imatge d'un cor petit (cor petit)"""
    HAPPY: Image
    """Imatge d'una cara feliç (feliç)"""
    SMILE: Image
    """Imatge d'una cara somrient (somriure)"""
    SAD: Image
    """Imatge d'una cara trista (tristesa)"""
    CONFUSED: Image
    """Imatge de cara confusa. (confusa)"""
    ANGRY: Image
    """Imatge d'una cara enfadada. (enfadat)"""
    ASLEEP: Image
    """Imatge d'una cara dormint. (despert)"""
    SURPRISED: Image
    """Imatge d'una cara de sorpresa (sorprès)"""
    SILLY: Image
    """Imatge d'una cara ximple. (ximple)"""
    FABULOUS: Image
    """Imatge d'una cara amb ulleres de sol. (fabulós)"""
    MEH: Image
    """Imatge d'una cara inexpressiva. (BAH avorrit)"""
    YES: Image
    """Imatge d'una marca tic. (sí)"""
    NO: Image
    """Imatge d'una creu."""
    CLOCK12: Image
    """Imatge d'una línia apuntant les dotze. (les dotze)"""
    CLOCK11: Image
    """Imatge d'una línia apuntant les onze. (les onze)"""
    CLOCK10: Image
    """Imatge d'una línia apuntant les deu. (les deu)"""
    CLOCK9: Image
    """Imatge d'una línia apuntant les nou. (les nou)"""
    CLOCK8: Image
    """Imatge d'una línia apuntant les vuit. (les vuit)"""
    CLOCK7: Image
    """Imatge d'una línia apuntant les set. (les set)"""
    CLOCK6: Image
    """Imatge amb una línia apuntant a les 6 en punt. (les sis)"""
    CLOCK5: Image
    """Imatge amb una línia apuntant a les 5 en punt. (les cinc)"""
    CLOCK4: Image
    """Imatge amb una línia apuntant a les 4 en punt. (les quatre)"""
    CLOCK3: Image
    """Imatge amb una línia apuntant a les 3 en punt. (les tres)"""
    CLOCK2: Image
    """Imatge amb una línia apuntant a les 2 en punt. (les dues)"""
    CLOCK1: Image
    """Imatge amb una línia apuntant a la 1 en punt. (la una)"""
    ARROW_N: Image
    """Imatge de fletxa apuntant al nord. (fletxa n)"""
    ARROW_NE: Image
    """Imatge de fletxa apuntant al nord-est. (fletxa ne)"""
    ARROW_E: Image
    """Imatge de fletxa apuntant a l'est. (fletxa e)"""
    ARROW_SE: Image
    """Imatge de fletxa apuntant al sud-est. (fletxa se)"""
    ARROW_S: Image
    """Imatge de fletxa apuntant al sud. (fletxa s)"""
    ARROW_SW: Image
    """Imatge de fletxa apuntant al sud-oest. (fletxa so)"""
    ARROW_W: Image
    """Imatge de fletxa apuntant a l'oest. (fletxa o)"""
    ARROW_NW: Image
    """Imatge de fletxa apuntant al nord-oest. (fletxa no)"""
    TRIANGLE: Image
    """Imatge d'un triangle apuntant amunt."""
    TRIANGLE_LEFT: Image
    """Imatge d'un triangle en la cantonada esquerra. (triangle a l'esquerra)"""
    CHESSBOARD: Image
    """Leds alternatius il·luminats en un patró d'escacs. (Tauler d'escacs)"""
    DIAMOND: Image
    """Imatge d'un diamant (diamant)"""
    DIAMOND_SMALL: Image
    """Imatge d'un diamant petit (diamant petit)"""
    SQUARE: Image
    """Imatge d'un quadrat (quadrat)"""
    SQUARE_SMALL: Image
    """Imatge d'un quadrat petit (quadrat petit)"""
    RABBIT: Image
    """Imatge d'un conill. (conill)"""
    COW: Image
    """Imatge d'una vaca. (vaca)"""
    MUSIC_CROTCHET: Image
    """Imatge de la nota musical negra (nota musical negra)"""
    MUSIC_QUAVER: Image
    """Imatge de la nota musical corxera (nota musical corxera)"""
    MUSIC_QUAVERS: Image
    """Imatge d'un parell de notes musicals corxeres (nota musical corxera)"""
    PITCHFORK: Image
    """Imatge d'una forca. (forca)"""
    XMAS: Image
    """Imatge d'un arbre de Nadal (nadal)"""
    PACMAN: Image
    """Imatge del personatge de Pac-man a arcade"""
    TARGET: Image
    """Imatge d'objectiu. (diana)"""
    TSHIRT: Image
    """Imatge de samarreta. (Imatge d'una samarreta T-shirt)"""
    ROLLERSKATE: Image
    """Imatge d'un patinet. (patinet)"""
    DUCK: Image
    """Imatge d'un ànec. (ànec)"""
    HOUSE: Image
    """Imatge d'una casa. (casa)"""
    TORTOISE: Image
    """Imatge d'una tortuga. (tortuga)"""
    BUTTERFLY: Image
    """Imatge d'una papallona. (papallona)"""
    STICKFIGURE: Image
    """Imatge de figura d'un pal. (imatge d'un pal)"""
    GHOST: Image
    """Imatge d'un fantasma. (fantasma)"""
    SWORD: Image
    """Imatge d'una espasa (espasa)"""
    GIRAFFE: Image
    """Imatge d'una girafa. (girafa)"""
    SKULL: Image
    """Imatge d'un crani. (crani)"""
    UMBRELLA: Image
    """Imatge d'un paraigua, (paraigua)"""
    SNAKE: Image
    """Imatge d'una serp. (serp)"""
    SCISSORS: Image
    """Imatge d'unes tisores. (tisores)"""
    ALL_CLOCKS: List[Image]
    """Una llista que conté totes les imatges CLOCK_ en seqüència. (tots els rellotges)"""
    ALL_ARROWS: List[Image]
    """Una llista que conté totes les ARROW_images en seqüència. (totes les fletxes)"""

    @overload
    def __init__(self, string: str) -> None:
        """Crea una imatge a partir d'una cadena que descrigui quins leds estan encesos.

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (cadena) La cadena descrivint la imatge."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Crea una imatge buida amb ``width`` columnes i ``height`` files.

:param width: (amplada) Amplada opcional de la imatge
:param height: (alçària) Alçària opcional de la imatge
:param buffer: (memòria intermèdia) Llistes o bytes opcionals d'enters de ``width``×``height`` dins l'interval de 0 a 9 per inicialitzar la imatge

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Obté el nombre de columnes (amplada)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Obté el nombre de files. (alçària)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Estableix la brillantor d'un píxel. (estableix píxel)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: El nombre de la columna
:param y: El nombre de la fila
:param value: (valor) La brillantor com a nombre enter entre 0 (fosc) i 9 (brillant)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Obté la brillantor d'un píxel. (obté píxel)

Example: ``my_image.get_pixel(0, 0)``

:param x: El nombre de la columna
:param y: El nombre de la fila
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Crea una imatge nova movent-la cap a l'esquerra. (desplaça a l'esquerra)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: El nombre de columnes per desplaçar-se
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Crea una imatge nova movent-la cap a la dreta. (desplaça a la dreta)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: El nombre de columnes per desplaçar-se
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Crea una imatge nova desplaçant la imatge cap amunt. (desplaça cap amunt)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: El nombre de files per desplaçar-se
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Crea una imatge nova desplaçant-la cap avall. (desplaça cap avall)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: El nombre de files per desplaçar-se
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Crea una imatge nova retallant la imatge. (retalla)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: La columna de desplaçament del retall
:param y: La fila de desplaçament del retall
:param w: L'amplada del retall
:param h: L'alçària del retall
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Crea una còpia exacta de la imatge (còpia)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Crea una imatge nova invertint la brillantor dels píxels de la imatge
font. (inverteix)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Assigna la brillantor de tots els píxels de la imatge (omple)

Example: ``my_image.fill(5)``

:param value: (valor) La nova brillantor com a nombre entre 0 (fosc) i 9 (brillant).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Copia una àrea d'una altra imatge a aquesta imatge.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (font) La imatge font
:param x: Desplaçament de la columna inicial a la imatge d'origen
:param y: Desplaçament de la fila inicial a la imatge d'origen
:param w: El nombre de columnes a copiar
:param h: El nombre de files a copiar
:param xdest: El desplaçament de columna a modificar en aquesta imatge
:param ydest: El desplaçament de fila que cal modificar en aquesta imatge

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
        """Obté una representació de cadena compacta de la imatge. (repr - Obté una representació de cadena compacta de la imatge.)"""
        ...

    def __str__(self) -> str:
        """Obté una representació de cadena llegible de la imatge."""
        ...

    def __add__(self, other: Image) -> Image:
        """Crea una imatge nova afegint els valors de brillantor de les dues
imatges per a cada píxel. (afegeix)

Example: ``Image.HEART + Image.HAPPY``

:param other: (altre) La imatge a afegir."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Crea una imatge nova restant els valors de brillantor d'una altra imatge d'aquesta imatge.

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (altre) La imatge a restar."""
        ...

    def __mul__(self, n: float) -> Image:
        """Crea una imatge nova multiplicant la brillantor de cada píxel per
``n``.

Example: ``Image.HEART * 0.5``

:param n: El valor per multiplicar."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Crea una imatge nova dividint la brillantor de cada píxel per
``n``.

Example: ``Image.HEART / 2``

:param n: El valor del divisor."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Representa la transició dels esdeveniments de so, des de ``quiet`` a ``loud`` com picant de mans o cridant. (so fort)"""
    QUIET: SoundEvent
    """Representa la transició dels esdeveniments de so, des de ``loud`` a ``quiet`` com parlant o música de fons. (so fluix)"""

class Sound:
    """Els sons integrats es poden reproduir mitjançant ``audio.play(Sound.NAME)``. (so)"""
    GIGGLE: Sound
    """So de riure (riure)"""
    HAPPY: Sound
    """So feliç. (feliç)"""
    HELLO: Sound
    """So de salutació. (hola)"""
    MYSTERIOUS: Sound
    """So misteriós. (misteriós)"""
    SAD: Sound
    """So trist. (tristesa)"""
    SLIDE: Sound
    """So lliscant (so lliscant)"""
    SOARING: Sound
    """So creixent. (creixent)"""
    SPRING: Sound
    """So primaveral. (primaveral)"""
    TWINKLE: Sound
    """So de centelleig. (centelleig)"""
    YAWN: Sound
    """So de badall. (badall)"""