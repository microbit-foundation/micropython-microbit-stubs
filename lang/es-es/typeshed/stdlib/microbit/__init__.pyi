"""Pines, imágenes, sonidos, temperatura y volumen. (microbit)"""
from _typeshed import ReadableBuffer
from typing import Any, Callable, List, Optional, overload
from . import accelerometer as accelerometer
from . import compass as compass
from . import display as display
from . import i2c as i2c
from . import microphone as microphone
from . import speaker as speaker
from . import spi as spi
from . import uart as uart
from . import audio as audio

def run_every(callback: Optional[Callable[[], None]]=None, days: int=0, h: int=0, min: int=0, s: int=0, ms: int=0) -> Callable[[Callable[[], None]], Callable[[], None]]:
    """Programa una función para llamarla en un intervalo dado **solo V2**. (run every)

Example: ``run_every(my_logging, min=5)``

This function can be passed a callback::

    run_every(your_function, h=1, min=20, s=30, ms=50)

or used as a decorator::

    @run_every(h=1, min=20, s=30, ms=50)
    def your_function():
        pass

Arguments with different time units are additive.

:param callback: (callback) La función "callback" (devolución de llamada) que se llama; omitir si se usa en un patrón "Decorator"
:param days: (días) El intervalo en días.
:param h: (h) El intervalo en horas.
:param min: (min) El intervalo en minutos.
:param s: (s) El intervalo en segundos.
:param ms: (ms) El intervalo en milisegundos."""

def panic(n: int) -> None:
    """Entra en modo pánico (panic)

Example: ``panic(127)``

:param n: (n) Un entero arbitrario <= 255 para indicar un estado.

Requires restart."""

def reset() -> None:
    """Reiniciar la placa. (reset)"""

def sleep(n: float) -> None:
    """Espera ``n`` milisegundos. (sleep)

Example: ``sleep(1000)``

:param n: (n) El número de milisegundos a esperar

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Obtiene el tiempo de funcionamiento de la placa. (running time)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Obtiene la temperatura del micro:bit en grados Celcius. (temperatura)"""

def set_volume(v: int) -> None:
    """Establece el volumen. (set volume)

Example: ``set_volume(127)``

:param v: (v) un valor entre 0 (bajo) y 255 (alto).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """La clase para los botones ``button_a`` y ``button_b``. (botón)"""

    def is_pressed(self) -> bool:
        """Comprueba si el botón está pulsado. (is pressed)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Comprueba si el botón ha sido pulsado desde que se inció el dispositivo o desde la última vez que se llamó a este método. (was pressed)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Obtiene el total de pulsaciones sucesivas de un botón y restablece este total
a cero. (get presses)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""Objeto ``Button`` para el botón izquierdo. (botón a)"""
button_b: Button
"""Objeto ``Button`` para el botón derecho. (botón b)"""

class MicroBitDigitalPin:
    """Un pin digital. (microbitdigitalpin)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Obtiene el valor digital del pin. (read digital)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Establece el valor digital del pin. (write digital)

Example: ``pin0.write_digital(1)``

:param value: (value) 1 para establecer valor alto en el pin o 0 para valor bajo"""
        ...

    def set_pull(self, value: int) -> None:
        """Configura el estado "pull" con uno de los tres valores posibles: ``PULL_UP``, ``PULL_DOWN`` o ``NO_PULL``. (set pull)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (valor) El estado "pull" del pin correspondiente, p. ej., ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Obtiene el estado "pull" de un pin. (get pull)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Devuelve el modo del pin. (get mode)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Envía una señal PWM al pin, con el ciclo de trabajo proporcional a ``value``. (write analog)

Example: ``pin0.write_analog(254)``

:param value: (valor) Un número entero o de coma flotante entre 0 (ciclo de trabajo de 0 %) y 1023 (100 %)."""

    def set_analog_period(self, period: int) -> None:
        """Establece el período de la señal PWM enviada a ``period`` milisegundos. (set analog period)

Example: ``pin0.set_analog_period(10)``

:param period: (período) El período en milisegundos con un valor mínimo válido de 1 ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Establece el período de la señal PWM enviada a ``period`` microsegundos. (set analog period microseconds)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (período) El período en microsegundos con un valor mínimo válido de 256 μs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Un pin con características analógicas y digitales. (microbitanalogdigitalpin)"""

    def read_analog(self) -> int:
        """Lee el voltaje aplicado al pin. (read analog)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Un pin con características analógicas, digitales y táctiles. (microbittouchpin)"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Comprueba si se está tocando el pin. (is touched)

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
        """Establece el modo táctil del pin. (set touch mode)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (valor) ``CAPACITIVE`` o ``RESISTIVE`` del pin correspondiente."""
        ...
pin0: MicroBitTouchPin
"""Pin con funciones digitales, analógicas y táctiles. (pin0)"""
pin1: MicroBitTouchPin
"""Pin con funciones digitales, analógicas y táctiles. (pin1)"""
pin2: MicroBitTouchPin
"""Pin con funciones digitales, analógicas y táctiles. (pin2)"""
pin3: MicroBitAnalogDigitalPin
"""Pin con funciones digitales y analógicas. (pin3)"""
pin4: MicroBitAnalogDigitalPin
"""Pin con funciones digitales y analógicas. (pin4)"""
pin5: MicroBitDigitalPin
"""Pin con funciones digitales. (pin5)"""
pin6: MicroBitDigitalPin
"""Pin con funciones digitales. (pin6)"""
pin7: MicroBitDigitalPin
"""Pin con funciones digitales. (pin7)"""
pin8: MicroBitDigitalPin
"""Pin con funciones digitales. (pin8)"""
pin9: MicroBitDigitalPin
"""Pin con funciones digitales. (pin9)"""
pin10: MicroBitAnalogDigitalPin
"""Pin con funciones digitales y analógicas. (pin10)"""
pin11: MicroBitDigitalPin
"""Pin con funciones digitales. (pin11)"""
pin12: MicroBitDigitalPin
"""Pin con funciones digitales. (pin12)"""
pin13: MicroBitDigitalPin
"""Pin con funciones digitales. (pin13)"""
pin14: MicroBitDigitalPin
"""Pin con funciones digitales. (pin14)"""
pin15: MicroBitDigitalPin
"""Pin con funciones digitales. (pin15)"""
pin16: MicroBitDigitalPin
"""Pin con funciones digitales. (pin16)"""
pin19: MicroBitDigitalPin
"""Pin con funciones digitales. (pin19)"""
pin20: MicroBitDigitalPin
"""Pin con funciones digitales. (pin20)"""
pin_logo: MicroBitTouchPin
"""Un pin táctil sensible en la parte frontal del micro:bit que por defecto está configurado en modo táctil capacitivo. (pin logo)"""
pin_speaker: MicroBitAnalogDigitalPin
"""Un pin para dirigirse al altavoz micro:bit. (pin speaker)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Una imagen que se mostrará en la pantalla LED del micro:bit. (image)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Imagen de un corazón. (heart)"""
    HEART_SMALL: Image
    """Imagen de un corazón pequeño. (heart small)"""
    HAPPY: Image
    """Imagen de una cara feliz. (happy)"""
    SMILE: Image
    """Imagen de una cara sonriente. (smile)"""
    SAD: Image
    """Imagen de una cara triste. (sad)"""
    CONFUSED: Image
    """Imagen de una cara confundida. (confused)"""
    ANGRY: Image
    """Imagen de una cara enfadada. (angry)"""
    ASLEEP: Image
    """Imagen de una cara durmiendo. (asleep)"""
    SURPRISED: Image
    """Imagen de una cara sorprendida. (surprised)"""
    SILLY: Image
    """Imagen de una cara tonta. (silly)"""
    FABULOUS: Image
    """Imagen de una cara con gafas de sol. (fabulous)"""
    MEH: Image
    """Imagen de una cara indiferente. (meh)"""
    YES: Image
    """Imagen de verificación. (yes)"""
    NO: Image
    """Imagen de cruz. (no)"""
    CLOCK12: Image
    """Imagen de una línea apuntando a las 12:00. (clock12)"""
    CLOCK11: Image
    """Imagen de una línea apuntando a las 11:00. (clock11)"""
    CLOCK10: Image
    """Imagen de una línea apuntando a las 10:00. (clock10)"""
    CLOCK9: Image
    """Imagen de una línea apuntando a las 9:00. (clock9)"""
    CLOCK8: Image
    """Imagen de una línea apuntando a las 8:00. (clock8)"""
    CLOCK7: Image
    """Imagen de una línea apuntando a las 7:00. (clock7)"""
    CLOCK6: Image
    """Imagen de una línea apuntando a las 6:00. (clock6)"""
    CLOCK5: Image
    """Imagen de una línea apuntando a las 5:00. (clock5)"""
    CLOCK4: Image
    """Imagen de una línea apuntando a las 4:00. (clock4)"""
    CLOCK3: Image
    """Imagen de una línea apuntando a las 3:00. (clock3)"""
    CLOCK2: Image
    """Imagen de una línea apuntando a las 2:00. (clock2)"""
    CLOCK1: Image
    """Imagen de una línea apuntando a la 1:00. (clock1)"""
    ARROW_N: Image
    """Imagen de una flecha apuntando hacia el norte. (arrow n)"""
    ARROW_NE: Image
    """Imagen de una flecha apuntando hacia el nordeste. (arrow ne)"""
    ARROW_E: Image
    """Imagen de una flecha apuntando hacia el este. (arrow e)"""
    ARROW_SE: Image
    """Imagen de una flecha apuntando hacia el sudeste. (arrow se)"""
    ARROW_S: Image
    """Imagen de una flecha apuntando hacia el sur. (arrow s)"""
    ARROW_SW: Image
    """Imagen de una flecha apuntando hacia el sudoeste. (arrow sw)"""
    ARROW_W: Image
    """Imagen de una flecha apuntando hacia el oeste. (arrow w)"""
    ARROW_NW: Image
    """Imagen de una flecha apuntando hacia el noroeste. (arrow nw)"""
    TRIANGLE: Image
    """Imagen de un triángulo apuntando hacia arriba. (triangle)"""
    TRIANGLE_LEFT: Image
    """Imagen de un triángulo en la esquina izquierda. (triangle left)"""
    CHESSBOARD: Image
    """LED iluminados de forma alterna según un patrón de tablero de ajedrez. (chessboard)"""
    DIAMOND: Image
    """Imagen de un diamante. (diamond)"""
    DIAMOND_SMALL: Image
    """Imagen de un diamante pequeño. (diamond small)"""
    SQUARE: Image
    """Imagen de un cuadrado. (square)"""
    SQUARE_SMALL: Image
    """Imagen de un cuadrado pequeño. (square small)"""
    RABBIT: Image
    """Imagen de un conejo. (rabbit)"""
    COW: Image
    """Imagen de una vaca. (cow)"""
    MUSIC_CROTCHET: Image
    """Imagen de una nota negra. (music crotchet)"""
    MUSIC_QUAVER: Image
    """Imagen de una nota corchea. (music quaver)"""
    MUSIC_QUAVERS: Image
    """Imagen de un par de notas corcheas. (music quavers)"""
    PITCHFORK: Image
    """Imagen de una horca. (pitchfork)"""
    XMAS: Image
    """Imagen de un árbol de Navidad. (xmas)"""
    PACMAN: Image
    """Imagen del personaje de videojuegos Pac-Man. (pacman)"""
    TARGET: Image
    """Imagen de un objetivo. (target)"""
    TSHIRT: Image
    """Imagen de una camiseta. (tshirt)"""
    ROLLERSKATE: Image
    """Imagen de un patín. (rollerskate)"""
    DUCK: Image
    """Imagen de un pato. (duck)"""
    HOUSE: Image
    """Imagen de una casa. (house)"""
    TORTOISE: Image
    """Imagen de una tortuga. (tortoise)"""
    BUTTERFLY: Image
    """Imagen de una mariposa. (butterfly)"""
    STICKFIGURE: Image
    """Imagen de un monigote. (stickfigure)"""
    GHOST: Image
    """Imagen de un fantasma. (ghost)"""
    SWORD: Image
    """Imagen de una espada. (sword)"""
    GIRAFFE: Image
    """Imagen de una jirafa. (giraffe)"""
    SKULL: Image
    """Imagen de una calavera. (skull)"""
    UMBRELLA: Image
    """Imagen de un paraguas. (umbrella)"""
    SNAKE: Image
    """Imagen de una serpiente. (snake)"""
    ALL_CLOCKS: List[Image]
    """Una lista que contiene todas las imágenes CLOCK_ en secuencia. (all clocks)"""
    ALL_ARROWS: List[Image]
    """Una lista que contiene todas las imágenes ARROW_ en secuencia. (all arrows)"""

    @overload
    def __init__(self, string: str) -> None:
        """Crea una imagen a partir de una cadena que describe los LED que están encendidos. (init)

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (string) La cadena que describe la imagen."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Crea una imagen vacía con ``width`` columnas y ``height`` filas. (init)

:param width: (width) Ancho opcional de la imagen
:param height: (height) Altura opcional de la imagen
:param buffer: (buffer) Matriz opcional de bytes de ``width`` × ``height`` enteros en el rango 0 - 9 para inicializar la imagen

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Obtiene el número de columnas. (width)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Obtiene el número de filas. (height)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Establece el brillo de un píxel. (set pixel)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: (x) El número de columna
:param y: (y) El número de fila
:param value: (value) El brillo expresado como un entero entre 0 (oscuro) y 9 (brillante)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Obtiene el brillo de un píxel. (get pixel)

Example: ``my_image.get_pixel(0, 0)``

:param x: (x) El número de columna
:param y: (y) El número de fila
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Crea una nueva imagen desplazando la imagen hacia la izquierda. (shift left)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: (n) El número de columnas a desplazar
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Crea una nueva imagen desplazando la imagen hacia la derecha. (shift right)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: (n) El número de columnas a desplazar
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Crea una nueva imagen desplazando la imagen hacia arriba. (shift up)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: (n) El número de filas a desplazar
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Crea una nueva imagen desplazando la imagen hacia abajo. (shift down)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: (n) El número de filas a desplazar
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Crear una nueva imagen recortando la imagen. (crop)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: (x) La columna de desplazamiento del recorte
:param y: (y) La fila de desplazamiento del recorte
:param w: (w) El ancho del recorte
:param h: (h) La altura del recorte
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Crea una copia exacta de la imagen. (copy)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Crea una nueva imagen invirtiendo el brillo de los píxeles de la
imagen de origen. (invert)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Establece el brillo de todos los píxeles de la imagen. (fill)

Example: ``my_image.fill(5)``

:param value: (value) El nuevo brillo expresado como un número entre 0 (oscuro) y 9 (brillante).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Copia un área de otra imagen en esta imagen. (blit)

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (src) La imagen de origen
:param x: (x) El desplazamiento de columna inicial en la imagen de origen
:param y: (y) El desplazamiento de fila inicial en la imagen de origen
:param w: (w) El número de columnas a copiar
:param h: (h) El número de filas a copiar
:param xdest: (xdest) El desplazamiento de columna a modificar en esta imagen
:param ydest: (ydest) El desplazamiento de fila a modificar en esta imagen

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
        """Obtiene una representación en cadena compacta de la imagen. (repr)"""
        ...

    def __str__(self) -> str:
        """Obtiene una representación en cadena legible de la imagen. (str)"""
        ...

    def __add__(self, other: Image) -> Image:
        """Crea una nueva imagen sumando los valores de brillo de las dos imágenes
para cada píxel. (add)

Example: ``Image.HEART + Image.HAPPY``

:param other: (other) La imagen a añadir."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Crea una nueva imagen restando los valores de brillo de la otra imagen a los de esta imagen. (sub)

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (other) La imagen a restar."""
        ...

    def __mul__(self, n: float) -> Image:
        """Crea una nueva imagen multiplicando el brillo de cada píxel por ``n``. (mul)

Example: ``Image.HEART * 0.5``

:param n: (n) El valor por el que multiplicar."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Crea una nueva imagen dividiendo el brillo de cada píxel entre ``n``. (truediv)

Example: ``Image.HEART / 2``

:param n: (n) El valor entre el que dividir."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Representa la transición de eventos de sonido, desde ``quiet`` a ``loud``, como aplaudir o gritar. (loud)"""
    QUIET: SoundEvent
    """Representa la transición de eventos de sonido, desde ``loud`` hasta ``quiet``, como hablar o una música de fondo. (quiet)"""

class Sound:
    """Los sonidos predefinidos pueden llamarse usando ``audio.play(Sound.NAME)``. (sound)"""
    GIGGLE: Sound
    """Sonido de risita. (giggle)"""
    HAPPY: Sound
    """Sonido alegre. (happy)"""
    HELLO: Sound
    """Sonido de saludo. (hello)"""
    MYSTERIOUS: Sound
    """Sonido misterioso. (mysterious)"""
    SAD: Sound
    """Sonido triste. (sad)"""
    SLIDE: Sound
    """Sonido deslizante. (slide)"""
    SOARING: Sound
    """Sonido creciente. (soaring)"""
    SPRING: Sound
    """Sonido de muelle. (spring)"""
    TWINKLE: Sound
    """Sonido parpadeante. (twinkle)"""
    YAWN: Sound
    """Sonido de bostezo. (yawn)"""