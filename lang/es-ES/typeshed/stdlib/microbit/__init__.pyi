"""Pines, imágenes, sonidos, temperatura y volumen."""
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
    """Programa la ejecución de una función en el intervalo especificado por los argumentos de tiempo **Sólo V2**. (ejecutar cada)

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

:param callback: Función a llamar en el intervalo proporcionado. Omitir cuando se utiliza como un decorador.
:param days: (días) Configura la marca del día para la programación.
:param h: Configura la marca de la hora para la programación.
:param min: Configura la marca de los minutos para la programación.
:param s: Configura la segunda marca para la programación.
:param ms: Configura la marca de los milisegundos para la programación."""

def panic(n: int) -> None:
    """Entra en modo pánico (pánico)

Example: ``panic(127)``

:param n: Un entero arbitrario <= 255 para indicar un estado.

Requires restart."""

def reset() -> None:
    """Reiniciar la placa. (restablecer)"""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Convierte un valor de un rango a un rango de números enteros. (escala)

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: (valor) Un número a convertir.
:param from_: (de) Una tupla para definir el rango desde el que convertir.
:param to: (a) Una tupla para definir el rango al que convertir.
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Convierte un valor de un rango a un rango de punto flotante. (escala)

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: (valor) Un número a convertir.
:param from_: (de) Una tupla para definir el rango desde el que convertir.
:param to: (a) Una tupla para definir el rango al que convertir.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Espera ``n`` milisegundos. (dormir)

Example: ``sleep(1000)``

:param n: El número de milisegundos a esperar

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Obtiene el tiempo de funcionamiento de la placa. (tiempo de ejecución)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Obtiene la temperatura del micro:bit en grados Celsius. (temperatura)"""

def set_volume(v: int) -> None:
    """Establece el volumen. (configurar volumen)

Example: ``set_volume(127)``

:param v: un valor entre 0 (bajo) y 255 (alto).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """La clase para los botones ``button_a`` y ``button_b``. (botón)"""

    def is_pressed(self) -> bool:
        """Comprueba si el botón está pulsado. (está pulsado)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Comprueba si el botón ha sido pulsado desde que se inció el dispositivo o desde la última vez que se llamó a este método. (ha sido pulsado)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Obtiene el total de pulsaciones sucesivas de un botón y restablece este total
a cero. (total de pulsaciones)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""Objeto ``Button`` para el botón izquierdo. (botón a)"""
button_b: Button
"""Objeto ``Button`` para el botón derecho. (botón b)"""

class MicroBitDigitalPin:
    """Un pin digital. (pin digital microbit)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Obtiene el valor digital del pin. (lectura digital)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Establece el valor digital del pin. (escritura digital)

Example: ``pin0.write_digital(1)``

:param value: (valor) 1 para establecer valor alto en el pin o 0 para valor bajo"""
        ...

    def set_pull(self, value: int) -> None:
        """Configura el estado "pull" con uno de los tres valores posibles: ``PULL_UP``, ``PULL_DOWN`` o ``NO_PULL``. (configurar pull)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (valor) El estado "pull" del pin correspondiente, p. ej., ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Obtiene el estado "pull" de un pin. (obtener pull)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Devuelve el modo del pin. (obtener modo)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Envía una señal PWM al pin, con el ciclo de trabajo proporcional a ``value``. (escritura analógica)

Example: ``pin0.write_analog(254)``

:param value: (valor) Un número entero o de coma flotante entre 0 (ciclo de trabajo de 0 %) y 1023 (100 %)."""

    def set_analog_period(self, period: int) -> None:
        """Establece el período de la señal PWM enviada a ``period`` milisegundos. (configurar periodo analógico)

Example: ``pin0.set_analog_period(10)``

:param period: (período) El período en milisegundos con un valor mínimo válido de 1 ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Establece el período de la señal PWM enviada a ``period`` microsegundos. (configurar periodo analógico en microsegundos)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (período) El período en microsegundos con un valor mínimo válido de 256 μs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Un pin con características analógicas y digitales. (pin digital y analógico microbit)"""

    def read_analog(self) -> int:
        """Lee el voltaje aplicado al pin. (lectura analógica)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Un pin con características analógicas, digitales y táctiles. (pin táctil microbit)"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Comprueba si se está tocando el pin. (está tocado)

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
        """Establece el modo táctil del pin. (configurar modo táctil)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (valor) ``CAPACITIVE`` o ``RESISTIVE`` del pin correspondiente."""
        ...
pin0: MicroBitTouchPin
"""Pin con funciones digitales, analógicas y táctiles."""
pin1: MicroBitTouchPin
"""Pin con funciones digitales, analógicas y táctiles."""
pin2: MicroBitTouchPin
"""Pin con funciones digitales, analógicas y táctiles."""
pin3: MicroBitAnalogDigitalPin
"""Pin con funciones digitales y analógicas."""
pin4: MicroBitAnalogDigitalPin
"""Pin con funciones digitales y analógicas."""
pin5: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin6: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin7: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin8: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin9: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin10: MicroBitAnalogDigitalPin
"""Pin con funciones digitales y analógicas."""
pin11: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin12: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin13: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin14: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin15: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin16: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin19: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin20: MicroBitDigitalPin
"""Pin con funciones digitales."""
pin_logo: MicroBitTouchPin
"""Un pin táctil sensible en la parte frontal del micro:bit que por defecto está configurado en modo táctil capacitivo. (pin de logo)"""
pin_speaker: MicroBitAnalogDigitalPin
"""Un pin para dirigirse al altavoz micro:bit. (pin de altavoz)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Una imagen que se mostrará en la pantalla LED del micro:bit. (imagen)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Imagen de un corazón. (corazón)"""
    HEART_SMALL: Image
    """Imagen de un corazón pequeño. (corazón pequeño)"""
    HAPPY: Image
    """Imagen de una cara feliz. (feliz)"""
    SMILE: Image
    """Imagen de una cara sonriente. (sonrisa)"""
    SAD: Image
    """Imagen de una cara triste. (triste)"""
    CONFUSED: Image
    """Imagen de una cara confundida. (confundida)"""
    ANGRY: Image
    """Imagen de una cara enfadada. (enfadada)"""
    ASLEEP: Image
    """Imagen de una cara durmiendo. (dormida)"""
    SURPRISED: Image
    """Imagen de una cara sorprendida. (sorprendida)"""
    SILLY: Image
    """Imagen de una cara tonta. (tonta)"""
    FABULOUS: Image
    """Imagen de una cara con gafas de sol. (fabulosa)"""
    MEH: Image
    """Imagen de una cara indiferente. (indiferente)"""
    YES: Image
    """Imagen de verificación. (sí)"""
    NO: Image
    """Imagen de cruz."""
    CLOCK12: Image
    """Imagen de una línea apuntando a las 12:00. (reloj12)"""
    CLOCK11: Image
    """Imagen de una línea apuntando a las 11:00. (reloj11)"""
    CLOCK10: Image
    """Imagen de una línea apuntando a las 10:00. (reloj10)"""
    CLOCK9: Image
    """Imagen de una línea apuntando a las 9:00. (reloj9)"""
    CLOCK8: Image
    """Imagen de una línea apuntando a las 8:00. (reloj8)"""
    CLOCK7: Image
    """Imagen de una línea apuntando a las 7:00. (reloj7)"""
    CLOCK6: Image
    """Imagen de una línea apuntando a las 6:00. (reloj6)"""
    CLOCK5: Image
    """Imagen de una línea apuntando a las 5:00. (reloj5)"""
    CLOCK4: Image
    """Imagen de una línea apuntando a las 4:00. (reloj4)"""
    CLOCK3: Image
    """Imagen de una línea apuntando a las 3:00. (reloj3)"""
    CLOCK2: Image
    """Imagen de una línea apuntando a las 2:00. (reloj2)"""
    CLOCK1: Image
    """Imagen de una línea apuntando a la 1:00. (reloj1)"""
    ARROW_N: Image
    """Imagen de una flecha apuntando hacia el norte. (flecha n)"""
    ARROW_NE: Image
    """Imagen de una flecha apuntando hacia el nordeste. (flecha ne)"""
    ARROW_E: Image
    """Imagen de una flecha apuntando hacia el este. (flecha e)"""
    ARROW_SE: Image
    """Imagen de una flecha apuntando hacia el sudeste. (flecha se)"""
    ARROW_S: Image
    """Imagen de una flecha apuntando hacia el sur. (flecha s)"""
    ARROW_SW: Image
    """Imagen de una flecha apuntando hacia el sudoeste. (flecha so)"""
    ARROW_W: Image
    """Imagen de una flecha apuntando hacia el oeste. (flecha o)"""
    ARROW_NW: Image
    """Imagen de una flecha apuntando hacia el noroeste. (flecha no)"""
    TRIANGLE: Image
    """Imagen de un triángulo apuntando hacia arriba. (triángulo)"""
    TRIANGLE_LEFT: Image
    """Imagen de un triángulo en la esquina izquierda. (triángulo izquierda)"""
    CHESSBOARD: Image
    """LED iluminados de forma alterna según un patrón de tablero de ajedrez. (tablero de ajedrez)"""
    DIAMOND: Image
    """Imagen de un diamante. (diamante)"""
    DIAMOND_SMALL: Image
    """Imagen de un diamante pequeño. (diamante pequeño)"""
    SQUARE: Image
    """Imagen de un cuadrado. (cuadrado)"""
    SQUARE_SMALL: Image
    """Imagen de un cuadrado pequeño. (cuadrado pequeño)"""
    RABBIT: Image
    """Imagen de un conejo. (conejo)"""
    COW: Image
    """Imagen de una vaca. (vaca)"""
    MUSIC_CROTCHET: Image
    """Imagen de una nota negra. (negra musical)"""
    MUSIC_QUAVER: Image
    """Imagen de una nota corchea. (corchea musical)"""
    MUSIC_QUAVERS: Image
    """Imagen de un par de notas corcheas. (corcheas musicales)"""
    PITCHFORK: Image
    """Imagen de una horca. (horca)"""
    XMAS: Image
    """Imagen de un árbol de Navidad. (navidad)"""
    PACMAN: Image
    """Imagen del personaje de videojuegos Pac-Man."""
    TARGET: Image
    """Imagen de un objetivo. (diana)"""
    TSHIRT: Image
    """Imagen de una camiseta. (camiseta)"""
    ROLLERSKATE: Image
    """Imagen de un patín. (patín)"""
    DUCK: Image
    """Imagen de un pato. (pato)"""
    HOUSE: Image
    """Imagen de una casa. (casa)"""
    TORTOISE: Image
    """Imagen de una tortuga. (tortuga)"""
    BUTTERFLY: Image
    """Imagen de una mariposa. (mariposa)"""
    STICKFIGURE: Image
    """Imagen de un monigote. (monigote)"""
    GHOST: Image
    """Imagen de un fantasma. (fantasma)"""
    SWORD: Image
    """Imagen de una espada. (espada)"""
    GIRAFFE: Image
    """Imagen de una jirafa. (girafa)"""
    SKULL: Image
    """Imagen de una calavera. (calavera)"""
    UMBRELLA: Image
    """Imagen de un paraguas. (paraguas)"""
    SNAKE: Image
    """Imagen de una serpiente. (serpiente)"""
    SCISSORS: Image
    """Imagen de tijeras. (tijeras)"""
    ALL_CLOCKS: List[Image]
    """Una lista que contiene todas las imágenes CLOCK_ en secuencia. (todos los relojes)"""
    ALL_ARROWS: List[Image]
    """Una lista que contiene todas las imágenes ARROW_ en secuencia. (todas las flechas)"""

    @overload
    def __init__(self, string: str) -> None:
        """Crea una imagen a partir de una cadena que describe los LED que están encendidos.

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (cadena) La cadena que describe la imagen."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Crea una imagen vacía con ``width`` columnas y ``height`` filas.

:param width: (ancho) Ancho opcional de la imagen
:param height: (altura) Altura opcional de la imagen
:param buffer: (búfer) Matriz opcional de bytes de ``width`` × ``height`` enteros en el rango 0 - 9 para inicializar la imagen

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Obtiene el número de columnas. (ancho)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Obtiene el número de filas. (altura)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Establece el brillo de un píxel. (configurar píxel)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: El número de columna
:param y: El número de fila
:param value: (valor) El brillo expresado como un entero entre 0 (oscuro) y 9 (brillante)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Obtiene el brillo de un píxel. (obtener píxel)

Example: ``my_image.get_pixel(0, 0)``

:param x: El número de columna
:param y: El número de fila
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Crea una nueva imagen desplazando la imagen hacia la izquierda. (desplazamiento a la izquierda)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: El número de columnas a desplazar
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Crea una nueva imagen desplazando la imagen hacia la derecha. (desplazamiento a la derecha)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: El número de columnas a desplazar
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Crea una nueva imagen desplazando la imagen hacia arriba. (desplazamiento hacia arriba)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: El número de filas a desplazar
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Crea una nueva imagen desplazando la imagen hacia abajo. (desplazamiento hacia abajo)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: El número de filas a desplazar
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Crear una nueva imagen recortando la imagen. (recortar)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: La columna de desplazamiento del recorte
:param y: La fila de desplazamiento del recorte
:param w: (a) El ancho del recorte
:param h: La altura del recorte
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Crea una copia exacta de la imagen. (copiar)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Crea una nueva imagen invirtiendo el brillo de los píxeles de la
imagen de origen. (invertir)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Establece el brillo de todos los píxeles de la imagen. (llenar)

Example: ``my_image.fill(5)``

:param value: (valor) El nuevo brillo expresado como un número entre 0 (oscuro) y 9 (brillante).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Copia un área de otra imagen en esta imagen.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (org) La imagen de origen
:param x: El desplazamiento de columna inicial en la imagen de origen
:param y: El desplazamiento de fila inicial en la imagen de origen
:param w: (a) El número de columnas a copiar
:param h: El número de filas a copiar
:param xdest: El desplazamiento de columna a modificar en esta imagen
:param ydest: El desplazamiento de fila a modificar en esta imagen

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
        """Obtiene una representación en cadena compacta de la imagen."""
        ...

    def __str__(self) -> str:
        """Obtiene una representación en cadena legible de la imagen. (cad)"""
        ...

    def __add__(self, other: Image) -> Image:
        """Crea una nueva imagen sumando los valores de brillo de las dos imágenes
para cada píxel. (añadir)

Example: ``Image.HEART + Image.HAPPY``

:param other: (otro) La imagen a añadir."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Crea una nueva imagen restando los valores de brillo de la otra imagen a los de esta imagen. (rest)

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (otro) La imagen a restar."""
        ...

    def __mul__(self, n: float) -> Image:
        """Crea una nueva imagen multiplicando el brillo de cada píxel por ``n``.

Example: ``Image.HEART * 0.5``

:param n: El valor por el que multiplicar."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Crea una nueva imagen dividiendo el brillo de cada píxel entre ``n``.

Example: ``Image.HEART / 2``

:param n: El valor entre el que dividir."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Representa la transición de eventos de sonido, desde ``quiet`` a ``loud``, como aplaudir o gritar. (alto)"""
    QUIET: SoundEvent
    """Representa la transición de eventos de sonido, desde ``loud`` hasta ``quiet``, como hablar o una música de fondo. (silencioso)"""

class Sound:
    """Los sonidos predefinidos pueden llamarse usando ``audio.play(Sound.NAME)``. (sonido)"""
    GIGGLE: Sound
    """Sonido de risita. (risita)"""
    HAPPY: Sound
    """Sonido alegre. (feliz)"""
    HELLO: Sound
    """Sonido de saludo. (hola)"""
    MYSTERIOUS: Sound
    """Sonido misterioso. (misterioso)"""
    SAD: Sound
    """Sonido triste. (triste)"""
    SLIDE: Sound
    """Sonido deslizante. (deslizante)"""
    SOARING: Sound
    """Sonido creciente. (creciente)"""
    SPRING: Sound
    """Sonido de muelle. (muelle)"""
    TWINKLE: Sound
    """Sonido parpadeante. (parpadeante)"""
    YAWN: Sound
    """Sonido de bostezo. (bostezo)"""