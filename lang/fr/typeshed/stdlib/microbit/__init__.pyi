"""Broches, images, sons, température et volume"""
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
    """Planifie l'exécution d'une fonction à l'intervalle spécifié par les arguments temporels **V2 uniquement**.

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

:param callback: Fonction à appeler à l'intervalle fourni. À omettre en cas d'utilisation comme décorateur.
:param days: Définit la marque du jour pour la programmation.
:param h: Définit la marque d'heure pour la programmation.
:param min: Définit la marque de minute pour la programmation.
:param s: Définit la marque de seconde pour la programmation.
:param ms: Définit la marque de milliseconde pour la programmation."""

def panic(n: int) -> None:
    """Passer en mode panique.

Example: ``panic(127)``

:param n: Un nombre entier arbitraire <= 255 pour indiquer un état.

Requires restart."""

def reset() -> None:
    """Redémarrer la carte."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Convertit une valeur dans l'intervalle donné vers son équivalent dans un autre intervalle d'entiers.

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: Un nombre à convertir.
:param from_: Un tuple qui définit l'intervalle de départ.
:param to: Un tuple qui définit l'intervalle d'arrivée.
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Convertit une valeur dans l'intervalle donné vers son équivalent dans un autre intervalle de nombres à virgule flottante.

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: Un nombre à convertir.
:param from_: Un tuple qui définit l'intervalle de départ.
:param to: Un tuple qui définit l'intervalle d'arrivée.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Attendre ``n`` millisecondes.

Example: ``sleep(1000)``

:param n: Le nombre de millisecondes à attendre

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Obtenir le temps de fonctionnement de la carte.

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Obtenir la température du micro:bit en degrés Celsius."""

def set_volume(v: int) -> None:
    """Définit le volume.

Example: ``set_volume(127)``

:param v: Une valeur entre 0 (bas) et 255 (haut).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """La classe pour les boutons ``button_a`` et ``button_b``."""

    def is_pressed(self) -> bool:
        """Vérifier si le bouton est appuyé.

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Vérifie si le bouton a été pressé depuis que l'appareil a été démarré ou depuis la dernière fois où cette méthode a été appelée.

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Obtenir le nombre total d'occurrences où le bouton a été appuyé, et réinitialise ce total avant de retourner.

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""L'objet bouton ``Button`` gauche."""
button_b: Button
"""L'objet bouton ``Button`` droit."""

class MicroBitDigitalPin:
    """Une broche numérique.

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Récupère la valeur numérique de la broche

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Définit la valeur numérique de la broche

Example: ``pin0.write_digital(1)``

:param value: 1 pour définir la broche à un niveau haut ou 0 pour définir la broche à un niveau bas"""
        ...

    def set_pull(self, value: int) -> None:
        """Définissez l'état de tirage sur l'une des trois valeurs possibles\xa0: ``PULL_UP``, ``PULL_DOWN`` ou ``NO_PULL``.

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: L'état de tirage sur la broche correspondante, par exemple ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Obtenir l'état de tirage sur une broche.

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Renvoie le mode de la broche

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Sortie d'un signal PWM sur la broche, avec un rapport cyclique proportionnel à ``value``.

Example: ``pin0.write_analog(254)``

:param value: Un entier ou un nombre à virgule flottante entre 0 (rapport cyclique à 0%) et 1023 (rapport cyclique à 100%)."""

    def set_analog_period(self, period: int) -> None:
        """Définit la période de sortie du signal PWM à ``period`` en millisecondes.

Example: ``pin0.set_analog_period(10)``

:param period: La période en millisecondes avec une valeur minimale valide de 1 ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Définit la période de sortie du signal PWM à ``period`` en millisecondes.

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: La période en microsecondes avec une valeur minimale valide de 256µs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Une broche avec des fonctions analogiques et numériques."""

    def read_analog(self) -> int:
        """Lit la tension appliquée à la broche.

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Une broche avec des fonctions analogiques, numériques et tactiles."""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Vérifie si la broche est touchée.

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
        """Définit le mode tactile pour la broche.

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: ``CAPACITIVE`` ou ``RESISTIVE`` pour la broche correspondante."""
        ...
pin0: MicroBitTouchPin
"""Broche avec des fonctionnalités numériques, analogiques, et tactiles."""
pin1: MicroBitTouchPin
"""Broche avec des fonctionnalités numériques, analogiques, et tactiles."""
pin2: MicroBitTouchPin
"""Broche avec des fonctionnalités numériques, analogiques, et tactiles."""
pin3: MicroBitAnalogDigitalPin
"""Broche avec des fonctionnalités numériques et analogiques."""
pin4: MicroBitAnalogDigitalPin
"""Broche avec des fonctionnalités numériques et analogiques."""
pin5: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin6: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin7: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin8: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin9: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin10: MicroBitAnalogDigitalPin
"""Broche avec des fonctionnalités numériques et analogiques."""
pin11: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin12: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin13: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin14: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin15: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin16: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin19: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin20: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques"""
pin_logo: MicroBitTouchPin
"""Une broche logo sensible au toucher sur l'avant du micro:bit, qui est définie par défaut en mode tactile capacitif."""
pin_speaker: MicroBitAnalogDigitalPin
"""Une broche pour adresser le haut-parleur micro:bit.

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Une image à afficher sur l'écran LED du micro:bit.

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Image d'un cœur."""
    HEART_SMALL: Image
    """Petite image d'un cœur"""
    HAPPY: Image
    """Image de visage heureux."""
    SMILE: Image
    """Image de visage souriant."""
    SAD: Image
    """Image de visage triste."""
    CONFUSED: Image
    """Image d'un visage perplexe."""
    ANGRY: Image
    """Image de visage en colère."""
    ASLEEP: Image
    """Image de visage endormi"""
    SURPRISED: Image
    """Image de visage surpris."""
    SILLY: Image
    """Image de visage absurde."""
    FABULOUS: Image
    """Image de visage avec lunettes de soleil."""
    MEH: Image
    """Image de visage pas impressionné"""
    YES: Image
    """Image d'une coche."""
    NO: Image
    """Image d'une croix."""
    CLOCK12: Image
    """Image avec une ligne indiquant vers 12 heures."""
    CLOCK11: Image
    """Image avec une ligne indiquant vers 11 heures."""
    CLOCK10: Image
    """Image avec une ligne indiquant vers 10 heures."""
    CLOCK9: Image
    """Image avec une ligne indiquant vers 9 heures."""
    CLOCK8: Image
    """Image avec une ligne indiquant vers 8 heures."""
    CLOCK7: Image
    """Image avec une ligne indiquant vers 7 heures."""
    CLOCK6: Image
    """Image avec une ligne indiquant vers 6 heures."""
    CLOCK5: Image
    """Image avec une ligne indiquant vers 5 heures."""
    CLOCK4: Image
    """Image avec une ligne indiquant vers 4 heures."""
    CLOCK3: Image
    """Image avec une ligne indiquant vers 3 heures."""
    CLOCK2: Image
    """Image avec une ligne indiquant vers 2 heures."""
    CLOCK1: Image
    """Image avec une ligne indiquant vers 1 heure."""
    ARROW_N: Image
    """Image de flèche pointant vers le nord."""
    ARROW_NE: Image
    """Image de flèche pointant vers le nord est."""
    ARROW_E: Image
    """Image de flèche pointant vers l'est."""
    ARROW_SE: Image
    """Image de flèche pointant vers le sud-est."""
    ARROW_S: Image
    """Image de flèche pointant vers le sud."""
    ARROW_SW: Image
    """Image de flèche pointant vers le sud-ouest."""
    ARROW_W: Image
    """Image de flèche pointant vers l'ouest."""
    ARROW_NW: Image
    """Image de flèche pointant vers le nord ouest."""
    TRIANGLE: Image
    """Image d'un triangle pointant vers le haut."""
    TRIANGLE_LEFT: Image
    """Image d'un triangle dans le coin gauche."""
    CHESSBOARD: Image
    """Éclairage alternatif des LEDs dans un motif d'échiquier."""
    DIAMOND: Image
    """Image de diamant."""
    DIAMOND_SMALL: Image
    """Petite image de diamant."""
    SQUARE: Image
    """Image de carré."""
    SQUARE_SMALL: Image
    """Petite image de carré."""
    RABBIT: Image
    """Image de lapin."""
    COW: Image
    """Image de vache."""
    MUSIC_CROTCHET: Image
    """Image d'une note."""
    MUSIC_QUAVER: Image
    """Image d'une croche."""
    MUSIC_QUAVERS: Image
    """Image d'une paire de croche."""
    PITCHFORK: Image
    """Image d'une fourche."""
    XMAS: Image
    """Image d'un arbre de Noël."""
    PACMAN: Image
    """Image du personnage d'arcade Pac-Man."""
    TARGET: Image
    """Image d'une cible."""
    TSHIRT: Image
    """Image de t-shirt."""
    ROLLERSKATE: Image
    """Image de patin à roulette."""
    DUCK: Image
    """Image de canard."""
    HOUSE: Image
    """Image d'une maison."""
    TORTOISE: Image
    """Image d'une tortue."""
    BUTTERFLY: Image
    """Image d'un papillon."""
    STICKFIGURE: Image
    """Image d'un personnage."""
    GHOST: Image
    """Image de fantôme."""
    SWORD: Image
    """Image d'une épée."""
    GIRAFFE: Image
    """Image d'une girafe."""
    SKULL: Image
    """Image d'un crâne."""
    UMBRELLA: Image
    """Image d'un parapluie."""
    SNAKE: Image
    """Image de serpent."""
    SCISSORS: Image
    """Image de ciseaux."""
    ALL_CLOCKS: List[Image]
    """Une liste contenant toutes les images CLOCK_ en séquence."""
    ALL_ARROWS: List[Image]
    """Une liste contenant toutes les images ARROW_ en séquence."""

    @overload
    def __init__(self, string: str) -> None:
        """Créer une image à partir d'une chaîne de caractères décrivant quelles LED sont allumées.

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: La chaîne de caractères décrivant l'image."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Créer une image vide avec ``width`` colonnes et ``height`` lignes.

:param width: Largeur optionnelle de l'image
:param height: Hauteur optionnelle de l'image
:param buffer: Tableau optionnel ou octets de ``width``×``height`` entiers dans la plage 0-9 pour initialiser l'image

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Récupère le nombre de colonnes.

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Récupère le nombre de lignes.

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Définit la luminosité d'un pixel.

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: Le numéro de colonne
:param y: Le numéro de ligne
:param value: La luminosité sous la forme d'un entier compris entre 0 (sombre) et 9 (lumineux)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Récupère la luminosité d'un pixel.

Example: ``my_image.get_pixel(0, 0)``

:param x: Le numéro de colonne
:param y: Le numéro de ligne
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Créer une nouvelle image en déplaçant l'image à gauche.

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: Le nombre de colonnes par lequel déplacer
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Créer une nouvelle image en déplaçant l'image à droite.

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: Le nombre de colonnes par lequel déplacer
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Créer une nouvelle image en déplaçant l'image vers le haut.

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: Le nombre de lignes par lequel déplacer
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Créer une nouvelle image en déplaçant l'image vers le bas.

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: Le nombre de lignes par lequel déplacer
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Créer une nouvelle image en recadrant l'image.

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: Le nombre de colonnes duquel décaler le recadrage
:param y: Le nombre de lignes duquel décaler le recadrage
:param w: La largeur du recadrage
:param h: La hauteur du recadrage
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Créer une copie exacte de l'image.

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Créer une nouvelle image en inversant la luminosité des pixels de l'image source.

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Définit la luminosité de tous les pixels de l'image.

Example: ``my_image.fill(5)``

:param value: La nouvelle luminosité sous la forme d'un nombre compris entre 0 (sombre) et 9 (lumineux).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Copier la zone d'une autre image vers cette image.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: L'image source
:param x: Le décalage de la colonne de départ dans l'image source
:param y: Décalage de la ligne de départ dans l'image source
:param w: Le nombre de colonnes à copier
:param h: Le nombre de lignes à copier
:param xdest: Le décalage de la colonne à modifier dans cette image
:param ydest: Le décalage de la ligne à modifier dans cette image

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
        """Récupère une représentation de l'image sous forme de texte compact."""
        ...

    def __str__(self) -> str:
        """Récupère une chaîne de caractères lisible de l'image."""
        ...

    def __add__(self, other: Image) -> Image:
        """Crée une nouvelle image en additionnant les valeurs de luminosité des deux images
pour chaque pixel.

Example: ``Image.HEART + Image.HAPPY``

:param other: L'image à ajouter."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Crée une nouvelle image en soustrayant de cette image les valeurs de luminosité de
l'autre image.

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: L'image à soustraire."""
        ...

    def __mul__(self, n: float) -> Image:
        """Crée une nouvelle image en multipliant la luminosité de chaque pixel par
``n``.

Example: ``Image.HEART * 0.5``

:param n: La valeur par laquelle multiplier."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Crée une nouvelle image en divisant la luminosité de chaque pixel par
``n``.

Example: ``Image.HEART / 2``

:param n: La valeur par laquelle diviser."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Représente la transition d'événements sonores, de ``quiet`` à ``loud`` comme un clap dans les mains ou un cri."""
    QUIET: SoundEvent
    """Représente la transition d'événements sonores de ``loud`` à ``quiet`` comme parler ou écouter de la musique de fond."""

class Sound:
    """Les sons intégrés peuvent être appelés en utilisant ``audio.play(Sound.NAME)``."""
    GIGGLE: Sound
    """Bruit de gloussement."""
    HAPPY: Sound
    """Son joyeux."""
    HELLO: Sound
    """Son de salutation."""
    MYSTERIOUS: Sound
    """Son mystérieux."""
    SAD: Sound
    """Son triste."""
    SLIDE: Sound
    """Bruit de glissade."""
    SOARING: Sound
    """Bruit d'envolée."""
    SPRING: Sound
    """Son d'un ressort."""
    TWINKLE: Sound
    """Son de scintillement."""
    YAWN: Sound
    """Son de bâillement."""