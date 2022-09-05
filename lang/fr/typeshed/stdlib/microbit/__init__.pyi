"""Broches, images, sons, température et volume (microbit)"""
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
    """Planifie une fonction à appeler à un intervalle donné **V2 uniquement**. (run every)

Example: ``run_every(my_logging, min=5)``

This function can be passed a callback::

    run_every(your_function, h=1, min=20, s=30, ms=50)

or used as a decorator::

    @run_every(h=1, min=20, s=30, ms=50)
    def your_function():
        pass

Arguments with different time units are additive.

:param callback: (callback) Le callback à appeler. A omettre dans le cas de l'utilisation via décorateur
:param days: (days) L'intervalle en jours.
:param h: (h) L'intervalle en heures.
:param min: (min) L'intervalle en minutes.
:param s: (s) L'intervalle en secondes.
:param ms: (ms) L'intervalle en millisecondes."""

def panic(n: int) -> None:
    """Passer en mode panique. (panic)

Example: ``panic(127)``

:param n: (n) Un nombre entier arbitraire <= 255 pour indiquer un état.

Requires restart."""

def reset() -> None:
    """Redémarrer la carte. (reset)"""

def sleep(n: float) -> None:
    """Attendre ``n`` millisecondes. (sleep)

Example: ``sleep(1000)``

:param n: (n) Le nombre de millisecondes à attendre

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Obtenir le temps de fonctionnement de la carte. (running time)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Obtenir la température du micro:bit en degrés Celcius. (temperature)"""

def set_volume(v: int) -> None:
    """Définit le volume. (set volume)

Example: ``set_volume(127)``

:param v: (v) Une valeur entre 0 (bas) et 255 (haut).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """La classe pour les boutons ``button_a`` et ``button_b``. (button)"""

    def is_pressed(self) -> bool:
        """Vérifier si le bouton est appuyé. (is pressed)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Vérifie si le bouton a été pressé depuis que l'appareil a été démarré ou depuis la dernière fois où cette méthode a été appelée. (was pressed)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Obtenir le nombre total d'occurrences où le bouton a été appuyé, et réinitialise ce total avant de retourner. (get presses)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""L'objet bouton ``Button`` gauche. (button a)"""
button_b: Button
"""L'objet bouton ``Button`` droit. (button b)"""

class MicroBitDigitalPin:
    """Une broche numérique. (microbitdigitalpin)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Récupère la valeur numérique de la broche (read digital)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Définit la valeur numérique de la broche (write digital)

Example: ``pin0.write_digital(1)``

:param value: (value) 1 pour définir la broche à un niveau haut ou 0 pour définir la broche à un niveau bas"""
        ...

    def set_pull(self, value: int) -> None:
        """Définissez l'état de tirage sur l'une des trois valeurs possibles\xa0: ``PULL_UP``, ``PULL_DOWN`` ou ``NO_PULL``. (set pull)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (value) L'état de tirage sur la broche correspondante, par exemple ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Obtenir l'état de tirage sur une broche. (get pull)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Renvoie le mode de la broche (get mode)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Sortie d'un signal PWM sur la broche, avec un rapport cyclique proportionnel à ``value``. (write analog)

Example: ``pin0.write_analog(254)``

:param value: (value) Un entier ou un nombre à virgule flottante entre 0 (rapport cyclique à 0%) et 1023 (rapport cyclique à 100%)."""

    def set_analog_period(self, period: int) -> None:
        """Définit la période de sortie du signal PWM à ``period`` en millisecondes. (set analog period)

Example: ``pin0.set_analog_period(10)``

:param period: (period) La période en millisecondes avec une valeur minimale valide de 1 ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Définit la période de sortie du signal PWM à ``period`` en millisecondes. (set analog period microseconds)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (period) La période en microsecondes avec une valeur minimale valide de 256µs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Une broche avec des fonctions analogiques et numériques. (microbitanalogdigitalpin)"""

    def read_analog(self) -> int:
        """Lit la tension appliquée à la broche. (read analog)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Une broche avec des fonctions analogiques, numériques et tactiles. (microbittouchpin)"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Vérifie si la broche est touchée. (is touched)

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
        """Définit le mode tactile pour la broche. (set touch mode)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (value) ``CAPACITIVE`` ou ``RESISTIVE`` pour la broche correspondante."""
        ...
pin0: MicroBitTouchPin
"""Broche avec des fonctionnalités numériques, analogiques, et tactiles. (pin0)"""
pin1: MicroBitTouchPin
"""Broche avec des fonctionnalités numériques, analogiques, et tactiles. (pin1)"""
pin2: MicroBitTouchPin
"""Broche avec des fonctionnalités numériques, analogiques, et tactiles. (pin2)"""
pin3: MicroBitAnalogDigitalPin
"""Broche avec des fonctionnalités numériques et analogiques. (pin3)"""
pin4: MicroBitAnalogDigitalPin
"""Broche avec des fonctionnalités numériques et analogiques. (pin4)"""
pin5: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin5)"""
pin6: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin6)"""
pin7: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin7)"""
pin8: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin8)"""
pin9: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin9)"""
pin10: MicroBitAnalogDigitalPin
"""Broche avec des fonctionnalités numériques et analogiques. (pin10)"""
pin11: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin11)"""
pin12: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin12)"""
pin13: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin13)"""
pin14: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin14)"""
pin15: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin15)"""
pin16: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin16)"""
pin19: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin19)"""
pin20: MicroBitDigitalPin
"""Broche avec des fonctionnalités numériques (pin20)"""
pin_logo: MicroBitTouchPin
"""Une broche logo sensible au toucher sur l'avant du micro:bit, qui est définie par défaut en mode tactile capacitif. (pin logo)"""
pin_speaker: MicroBitAnalogDigitalPin
"""Une broche pour adresser le haut-parleur micro:bit. (pin speaker)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Une image à afficher sur l'écran LED du micro:bit. (image)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Image d'un cœur. (heart)"""
    HEART_SMALL: Image
    """Petite image d'un cœur (heart small)"""
    HAPPY: Image
    """Image de visage heureux. (happy)"""
    SMILE: Image
    """Image de visage souriant. (smile)"""
    SAD: Image
    """Image de visage triste. (sad)"""
    CONFUSED: Image
    """Image d'un visage perplexe. (confused)"""
    ANGRY: Image
    """Image de visage en colère. (angry)"""
    ASLEEP: Image
    """Image de visage endormi (asleep)"""
    SURPRISED: Image
    """Image de visage surpris. (surprised)"""
    SILLY: Image
    """Image de visage absurde. (silly)"""
    FABULOUS: Image
    """Image de visage avec lunettes de soleil. (fabulous)"""
    MEH: Image
    """Image de visage pas impressionné (meh)"""
    YES: Image
    """Image d'une coche. (yes)"""
    NO: Image
    """Image d'une croix. (no)"""
    CLOCK12: Image
    """Image avec une ligne indiquant vers 12 heures. (clock12)"""
    CLOCK11: Image
    """Image avec une ligne indiquant vers 11 heures. (clock11)"""
    CLOCK10: Image
    """Image avec une ligne indiquant vers 10 heures. (clock10)"""
    CLOCK9: Image
    """Image avec une ligne indiquant vers 9 heures. (clock9)"""
    CLOCK8: Image
    """Image avec une ligne indiquant vers 8 heures. (clock8)"""
    CLOCK7: Image
    """Image avec une ligne indiquant vers 7 heures. (clock7)"""
    CLOCK6: Image
    """Image avec une ligne indiquant vers 6 heures. (clock6)"""
    CLOCK5: Image
    """Image avec une ligne indiquant vers 5 heures. (clock5)"""
    CLOCK4: Image
    """Image avec une ligne indiquant vers 4 heures. (clock4)"""
    CLOCK3: Image
    """Image avec une ligne indiquant vers 3 heures. (clock3)"""
    CLOCK2: Image
    """Image avec une ligne indiquant vers 2 heures. (clock2)"""
    CLOCK1: Image
    """Image avec une ligne indiquant vers 1 heure. (clock1)"""
    ARROW_N: Image
    """Image de flèche pointant vers le nord. (arrow n)"""
    ARROW_NE: Image
    """Image de flèche pointant vers le nord est. (arrow ne)"""
    ARROW_E: Image
    """Image de flèche pointant vers l'est. (arrow e)"""
    ARROW_SE: Image
    """Image de flèche pointant vers le sud-est. (arrow se)"""
    ARROW_S: Image
    """Image de flèche pointant vers le sud. (arrow s)"""
    ARROW_SW: Image
    """Image de flèche pointant vers le sud-ouest. (arrow sw)"""
    ARROW_W: Image
    """Image de flèche pointant vers l'ouest. (arrow w)"""
    ARROW_NW: Image
    """Image de flèche pointant vers le nord ouest. (arrow nw)"""
    TRIANGLE: Image
    """Image d'un triangle pointant vers le haut. (triangle)"""
    TRIANGLE_LEFT: Image
    """Image d'un triangle dans le coin gauche. (triangle left)"""
    CHESSBOARD: Image
    """Éclairage alternatif des LEDs dans un motif d'échiquier. (chessboard)"""
    DIAMOND: Image
    """Image de diamant. (diamond)"""
    DIAMOND_SMALL: Image
    """Petite image de diamant. (diamond small)"""
    SQUARE: Image
    """Image de carré. (square)"""
    SQUARE_SMALL: Image
    """Petite image de carré. (square small)"""
    RABBIT: Image
    """Image de lapin. (rabbit)"""
    COW: Image
    """Image de vache. (cow)"""
    MUSIC_CROTCHET: Image
    """Image d'une note. (music crotchet)"""
    MUSIC_QUAVER: Image
    """Image d'une croche. (music quaver)"""
    MUSIC_QUAVERS: Image
    """Image d'une paire de croche. (music quavers)"""
    PITCHFORK: Image
    """Image d'une fourche. (pitchfork)"""
    XMAS: Image
    """Image d'un arbre de Noël. (xmas)"""
    PACMAN: Image
    """Image du personnage d'arcade Pac-Man. (pacman)"""
    TARGET: Image
    """Image d'une cible. (target)"""
    TSHIRT: Image
    """Image de t-shirt. (tshirt)"""
    ROLLERSKATE: Image
    """Image de patin à roulette. (rollerskate)"""
    DUCK: Image
    """Image de canard. (duck)"""
    HOUSE: Image
    """Image d'une maison. (house)"""
    TORTOISE: Image
    """Image d'une tortue. (tortoise)"""
    BUTTERFLY: Image
    """Image d'un papillon. (butterfly)"""
    STICKFIGURE: Image
    """Image d'un personnage. (stickfigure)"""
    GHOST: Image
    """Image de fantôme. (ghost)"""
    SWORD: Image
    """Image d'une épée. (sword)"""
    GIRAFFE: Image
    """Image d'une girafe. (giraffe)"""
    SKULL: Image
    """Image d'un crâne. (skull)"""
    UMBRELLA: Image
    """Image d'un parapluie. (umbrella)"""
    SNAKE: Image
    """Image de serpent. (snake)"""
    ALL_CLOCKS: List[Image]
    """Une liste contenant toutes les images CLOCK_ en séquence. (all clocks)"""
    ALL_ARROWS: List[Image]
    """Une liste contenant toutes les images ARROW_ en séquence. (all arrows)"""

    @overload
    def __init__(self, string: str) -> None:
        """Créer une image à partir d'une chaîne de caractères décrivant quelles LED sont allumées. (init)

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (string) La chaîne de caractères décrivant l'image."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Créer une image vide avec ``width`` colonnes et ``height`` lignes. (init)

:param width: (width) Largeur optionnelle de l'image
:param height: (height) Hauteur optionnelle de l'image
:param buffer: (buffer) Tableau optionnel ou octets de ``width``×``height`` entiers dans la plage 0-9 pour initialiser l'image

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Récupère le nombre de colonnes. (width)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Récupère le nombre de lignes. (height)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Définit la luminosité d'un pixel. (set pixel)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: (x) Le numéro de colonne
:param y: (y) Le numéro de ligne
:param value: (value) La luminosité sous la forme d'un entier compris entre 0 (sombre) et 9 (lumineux)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Récupère la luminosité d'un pixel. (get pixel)

Example: ``my_image.get_pixel(0, 0)``

:param x: (x) Le numéro de colonne
:param y: (y) Le numéro de ligne
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Créer une nouvelle image en déplaçant l'image à gauche. (shift left)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: (n) Le nombre de colonnes par lequel déplacer
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Créer une nouvelle image en déplaçant l'image à droite. (shift right)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: (n) Le nombre de colonnes par lequel déplacer
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Créer une nouvelle image en déplaçant l'image vers le haut. (shift up)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: (n) Le nombre de lignes par lequel déplacer
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Créer une nouvelle image en déplaçant l'image vers le bas. (shift down)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: (n) Le nombre de lignes par lequel déplacer
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Créer une nouvelle image en recadrant l'image. (crop)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: (x) Le nombre de colonnes duquel décaler le recadrage
:param y: (y) Le nombre de lignes duquel décaler le recadrage
:param w: (w) La largeur du recadrage
:param h: (h) La hauteur du recadrage
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Créer une copie exacte de l'image. (copy)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Créer une nouvelle image en inversant la luminosité des pixels de l'image source. (invert)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Définit la luminosité de tous les pixels de l'image. (fill)

Example: ``my_image.fill(5)``

:param value: (value) La nouvelle luminosité sous la forme d'un nombre compris entre 0 (sombre) et 9 (lumineux).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Copier la zone d'une autre image vers cette image. (blit)

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (src) L'image source
:param x: (x) Le décalage de la colonne de départ dans l'image source
:param y: (y) Décalage de la ligne de départ dans l'image source
:param w: (w) Le nombre de colonnes à copier
:param h: (h) Le nombre de lignes à copier
:param xdest: (xdest) Le décalage de la colonne à modifier dans cette image
:param ydest: (ydest) Le décalage de la ligne à modifier dans cette image

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
        """Récupère une représentation de l'image sous forme de texte compact. (repr)"""
        ...

    def __str__(self) -> str:
        """Récupère une chaîne de caractères lisible de l'image. (str)"""
        ...

    def __add__(self, other: Image) -> Image:
        """Crée une nouvelle image en additionnant les valeurs de luminosité des deux images
pour chaque pixel. (add)

Example: ``Image.HEART + Image.HAPPY``

:param other: (other) L'image à ajouter."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Crée une nouvelle image en soustrayant de cette image les valeurs de luminosité de
l'autre image. (sub)

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (other) L'image à soustraire."""
        ...

    def __mul__(self, n: float) -> Image:
        """Crée une nouvelle image en multipliant la luminosité de chaque pixel par
``n``. (mul)

Example: ``Image.HEART * 0.5``

:param n: (n) La valeur par laquelle multiplier."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Crée une nouvelle image en divisant la luminosité de chaque pixel par
``n``. (truediv)

Example: ``Image.HEART / 2``

:param n: (n) La valeur par laquelle diviser."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Représente la transition d'événements sonores, de ``quiet`` à ``loud`` comme un clap dans les mains ou un cri. (loud)"""
    QUIET: SoundEvent
    """Représente la transition d'événements sonores de ``loud`` à ``quiet`` comme parler ou écouter de la musique de fond. (quiet)"""

class Sound:
    """Les sons intégrés peuvent être appelés en utilisant ``audio.play(Sound.NAME)``. (sound)"""
    GIGGLE: Sound
    """Bruit de gloussement. (giggle)"""
    HAPPY: Sound
    """Son joyeux. (happy)"""
    HELLO: Sound
    """Son de salutation. (hello)"""
    MYSTERIOUS: Sound
    """Son mystérieux. (mysterious)"""
    SAD: Sound
    """Son triste. (sad)"""
    SLIDE: Sound
    """Bruit de glissade. (slide)"""
    SOARING: Sound
    """Bruit d'envolée. (soaring)"""
    SPRING: Sound
    """Son d'un ressort. (spring)"""
    TWINKLE: Sound
    """Son de scintillement. (twinkle)"""
    YAWN: Sound
    """Son de bâillement. (yawn)"""