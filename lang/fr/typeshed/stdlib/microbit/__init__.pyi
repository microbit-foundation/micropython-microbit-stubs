"""Pins, images, sounds, temperature and volume. ()"""
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
    """Schedule a function to be called at a given interval **V2 only**. (run every)

Example: ``run_every(my_logging, min=5)``

This function can be passed a callback::

    run_every(your_function, h=1, min=20, s=30, ms=50)

or used as a decorator::

    @run_every(h=1, min=20, s=30, ms=50)
    def your_function():
        pass

Arguments with different time units are additive.

:param callback: (callback) The callback to invoke. Omit when using as a decorator.
:param days: (days) The interval in days.
:param h: (h) The interval in hours.
:param min: (min) The interval in minutes.
:param s: (s) The interval in seconds.
:param ms: (ms) The interval in milliseconds."""

def panic(n: int) -> None:
    """Enter a panic mode. (panic)

Example: ``panic(127)``

:param n: (n) An arbitrary integer <= 255 to indicate a status.

Requires restart."""

def reset() -> None:
    """Restart the board. (reset)"""

def sleep(n: float) -> None:
    """Wait for ``n`` milliseconds. (sleep)

Example: ``sleep(1000)``

:param n: (n) The number of milliseconds to wait

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Get the running time of the board. (running time)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Get the temperature of the micro:bit in degrees Celcius. (temperature)"""

def set_volume(v: int) -> None:
    """Sets the volume. (set volume)

Example: ``set_volume(127)``

:param v: (v) a value between 0 (low) and 255 (high).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """The class for the buttons `button_a` and `button_b`. (button)"""

    def is_pressed(self) -> bool:
        """Check if the button is pressed. (is pressed)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Check if the button was pressed since the device started or the last time this method was called. (was pressed)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Get the running total of button presses, and resets this total
to zero before returning. (get presses)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""The left button ``Button`` object. (button a)"""
button_b: Button
"""The right button ``Button`` object. (button b)"""

class MicroBitDigitalPin:
    """A digital pin. (microbitdigitalpin)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Get the digital value of the pin. (read digital)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Set the digital value of the pin. (write digital)

Example: ``pin0.write_digital(1)``

:param value: (value) ``1`` to set the pin high or ``0`` to set the pin low"""
        ...

    def set_pull(self, value: int) -> None:
        """Set the pull state to one of three possible values: ``PULL_UP``, ``PULL_DOWN`` or ``NO_PULL``. (set pull)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (value) The pull state from the relevant pin, e.g. ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Get the pull state on a pin. (get pull)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Returns the pin mode. (get mode)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Output a PWM signal on the pin, with the duty cycle proportional to ``value``. (write analog)

Example: ``pin0.write_analog(254)``

:param value: (value) An integer or a floating point number between 0 (0% duty cycle) and 1023 (100% duty)."""

    def set_analog_period(self, period: int) -> None:
        """Set the period of the PWM signal being output to ``period`` in milliseconds. (set analog period)

Example: ``pin0.set_analog_period(10)``

:param period: (period) The period in milliseconds with a minimum valid value of 1ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Set the period of the PWM signal being output to ``period`` in microseconds. (set analog period microseconds)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (period) The period in microseconds with a minimum valid value of 256µs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """A pin with analog and digital features. (microbitanalogdigitalpin)"""

    def read_analog(self) -> int:
        """Read the voltage applied to the pin. (read analog)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """A pin with analog, digital and touch features. (microbittouchpin)"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Check if the pin is being touched. (is touched)

Example: ``pin0.is_touched()``

The default touch mode for the pins on the edge connector is `resistive`.
The default for the logo pin **V2** is `capacitive`.

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
        """Set the touch mode for the pin. (set touch mode)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
`resistive`. The default for the logo pin **V2** is `capacitive`.

:param value: (value) ``CAPACITIVE`` or ``RESISTIVE`` from the relevant pin."""
        ...
pin0: MicroBitTouchPin
"""Pin with digital, analog and touch features. (pin0)"""
pin1: MicroBitTouchPin
"""Pin with digital, analog and touch features. (pin1)"""
pin2: MicroBitTouchPin
"""Pin with digital, analog and touch features. (pin2)"""
pin3: MicroBitAnalogDigitalPin
"""Pin with digital and analog features. (pin3)"""
pin4: MicroBitAnalogDigitalPin
"""Pin with digital and analog features. (pin4)"""
pin5: MicroBitDigitalPin
"""Pin with digital features. (pin5)"""
pin6: MicroBitDigitalPin
"""Pin with digital features. (pin6)"""
pin7: MicroBitDigitalPin
"""Pin with digital features. (pin7)"""
pin8: MicroBitDigitalPin
"""Pin with digital features. (pin8)"""
pin9: MicroBitDigitalPin
"""Pin with digital features. (pin9)"""
pin10: MicroBitAnalogDigitalPin
"""Pin with digital and analog features. (pin10)"""
pin11: MicroBitDigitalPin
"""Pin with digital features. (pin11)"""
pin12: MicroBitDigitalPin
"""Pin with digital features. (pin12)"""
pin13: MicroBitDigitalPin
"""Pin with digital features. (pin13)"""
pin14: MicroBitDigitalPin
"""Pin with digital features. (pin14)"""
pin15: MicroBitDigitalPin
"""Pin with digital features. (pin15)"""
pin16: MicroBitDigitalPin
"""Pin with digital features. (pin16)"""
pin19: MicroBitDigitalPin
"""Pin with digital features. (pin19)"""
pin20: MicroBitDigitalPin
"""Pin with digital features. (pin20)"""
pin_logo: MicroBitTouchPin
"""A touch sensitive logo pin on the front of the micro:bit, which by default is set to capacitive touch mode. (pin logo)"""
pin_speaker: MicroBitAnalogDigitalPin
"""A pin to address the micro:bit speaker. (pin speaker)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """An image to show on the micro:bit LED display. (image)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Heart image. (heart)"""
    HEART_SMALL: Image
    """Small heart image. (heart small)"""
    HAPPY: Image
    """Happy face image. (happy)"""
    SMILE: Image
    """Smiling face image. (smile)"""
    SAD: Image
    """Sad face image. (sad)"""
    CONFUSED: Image
    """Confused face image. (confused)"""
    ANGRY: Image
    """Angry face image. (angry)"""
    ASLEEP: Image
    """Sleeping face image. (asleep)"""
    SURPRISED: Image
    """Surprised face image. (surprised)"""
    SILLY: Image
    """Silly face image. (silly)"""
    FABULOUS: Image
    """Sunglasses face image. (fabulous)"""
    MEH: Image
    """Unimpressed face image. (meh)"""
    YES: Image
    """Tick image. (yes)"""
    NO: Image
    """Cross image. (no)"""
    CLOCK12: Image
    """Image with line pointing to 12 o'clock. (clock12)"""
    CLOCK11: Image
    """Image with line pointing to 11 o'clock. (clock11)"""
    CLOCK10: Image
    """Image with line pointing to 10 o'clock. (clock10)"""
    CLOCK9: Image
    """Image with line pointing to 9 o'clock. (clock9)"""
    CLOCK8: Image
    """Image with line pointing to 8 o'clock. (clock8)"""
    CLOCK7: Image
    """Image with line pointing to 7 o'clock. (clock7)"""
    CLOCK6: Image
    """Image with line pointing to 6 o'clock. (clock6)"""
    CLOCK5: Image
    """Image with line pointing to 5 o'clock. (clock5)"""
    CLOCK4: Image
    """Image with line pointing to 4 o'clock. (clock4)"""
    CLOCK3: Image
    """Image with line pointing to 3 o'clock. (clock3)"""
    CLOCK2: Image
    """Image with line pointing to 2 o'clock. (clock2)"""
    CLOCK1: Image
    """Image with line pointing to 1 o'clock. (clock1)"""
    ARROW_N: Image
    """Image of arrow pointing north. (arrow n)"""
    ARROW_NE: Image
    """Image of arrow pointing north east. (arrow ne)"""
    ARROW_E: Image
    """Image of arrow pointing east. (arrow e)"""
    ARROW_SE: Image
    """Image of arrow pointing south east. (arrow se)"""
    ARROW_S: Image
    """Image of arrow pointing south. (arrow s)"""
    ARROW_SW: Image
    """Image of arrow pointing south west. (arrow sw)"""
    ARROW_W: Image
    """Image of arrow pointing west. (arrow w)"""
    ARROW_NW: Image
    """Image of arrow pointing north west. (arrow nw)"""
    TRIANGLE: Image
    """Image of a triangle pointing up. (triangle)"""
    TRIANGLE_LEFT: Image
    """Image of a triangle in the left corner. (triangle left)"""
    CHESSBOARD: Image
    """Alternate LEDs lit in a chessboard pattern. (chessboard)"""
    DIAMOND: Image
    """Diamond image. (diamond)"""
    DIAMOND_SMALL: Image
    """Small diamond image. (diamond small)"""
    SQUARE: Image
    """Square image. (square)"""
    SQUARE_SMALL: Image
    """Small square image. (square small)"""
    RABBIT: Image
    """Rabbit image. (rabbit)"""
    COW: Image
    """Cow image. (cow)"""
    MUSIC_CROTCHET: Image
    """Crotchet note image. (music crotchet)"""
    MUSIC_QUAVER: Image
    """Quaver note image. (music quaver)"""
    MUSIC_QUAVERS: Image
    """Pair of quavers note image. (music quavers)"""
    PITCHFORK: Image
    """Pitchfork image. (pitchfork)"""
    XMAS: Image
    """Christmas tree image. (xmas)"""
    PACMAN: Image
    """Pac-Man arcade character image. (pacman)"""
    TARGET: Image
    """Target image. (target)"""
    TSHIRT: Image
    """T-shirt image. (tshirt)"""
    ROLLERSKATE: Image
    """Rollerskate image. (rollerskate)"""
    DUCK: Image
    """Duck image. (duck)"""
    HOUSE: Image
    """House image. (house)"""
    TORTOISE: Image
    """Tortoise image. (tortoise)"""
    BUTTERFLY: Image
    """Butterfly image. (butterfly)"""
    STICKFIGURE: Image
    """Stick figure image. (stickfigure)"""
    GHOST: Image
    """Ghost image. (ghost)"""
    SWORD: Image
    """Sword image. (sword)"""
    GIRAFFE: Image
    """Giraffe image. (giraffe)"""
    SKULL: Image
    """Skull image. (skull)"""
    UMBRELLA: Image
    """Umbrella image. (umbrella)"""
    SNAKE: Image
    """Snake image. (snake)"""
    ALL_CLOCKS: List[Image]
    """A list containing all the CLOCK_ images in sequence. (all clocks)"""
    ALL_ARROWS: List[Image]
    """A list containing all the ARROW_ images in sequence. (all arrows)"""

    @overload
    def __init__(self, string: str) -> None:
        """Create an image from a string describing which LEDs are lit. (init)

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (string) The string describing the image."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Create an empty image with ``width`` columns and ``height`` rows. (init)

:param width: (width) Optional width of the image
:param height: (height) Optional height of the image
:param buffer: (buffer) Optional array or bytes of ``width``×``height`` integers in range 0-9 to initialize the image

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Get the number of columns. (width)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Get the number of rows. (height)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Set the brightness of a pixel. (set pixel)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: (x) The column number
:param y: (y) The row number
:param value: (value) The brightness as an integer between 0 (dark) and 9 (bright)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Get the brightness of a pixel. (get pixel)

Example: ``my_image.get_pixel(0, 0)``

:param x: (x) The column number
:param y: (y) The row number
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Create a new image by shifting the picture left. (shift left)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: (n) The number of columns to shift by
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Create a new image by shifting the picture right. (shift right)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: (n) The number of columns to shift by
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Create a new image by shifting the picture up. (shift up)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: (n) The number of rows to shift by
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Create a new image by shifting the picture down. (shift down)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: (n) The number of rows to shift by
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Create a new image by cropping the picture. (crop)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: (x) The crop offset column
:param y: (y) The crop offset row
:param w: (w) The crop width
:param h: (h) The crop height
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Create an exact copy of the image. (copy)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Create a new image by inverting the brightness of the pixels in the
source image. (invert)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Set the brightness of all the pixels in the image. (fill)

Example: ``my_image.fill(5)``

:param value: (value) The new brightness as a number between 0 (dark) and 9 (bright).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Copy an area from another image into this image. (blit)

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (src) The source image
:param x: (x) The starting column offset in the source image
:param y: (y) The starting row offset in the source image
:param w: (w) The number of columns to copy
:param h: (h) The number of rows to copy
:param xdest: (xdest) The column offset to modify in this image
:param ydest: (ydest) The row offset to modify in this image

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
        """Get a compact string representation of the image. (repr)"""
        ...

    def __str__(self) -> str:
        """Get a readable string representation of the image. (str)"""
        ...

    def __add__(self, other: Image) -> Image:
        """Create a new image by adding the brightness values from the two
images for each pixel. (add)

Example: ``Image.HEART + Image.HAPPY``

:param other: (other) The image to add."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Create a new image by subtracting the brightness values of the
other image from this image. (sub)

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (other) The image to subtract."""
        ...

    def __mul__(self, n: float) -> Image:
        """Create a new image by multiplying the brightness of each pixel by
``n``. (mul)

Example: ``Image.HEART * 0.5``

:param n: (n) The value to multiply by."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Create a new image by dividing the brightness of each pixel by
``n``. (truediv)

Example: ``Image.HEART / 2``

:param n: (n) The value to divide by."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Represents the transition of sound events, from ``loud`` to ``quiet`` like speaking or background music. (loud)"""
    QUIET: SoundEvent
    """Represents the transition of sound events, from ``quiet`` to ``loud`` like clapping or shouting. (quiet)"""

class Sound:
    """The built-in sounds can be called using ``audio.play(Sound.NAME)``. (sound)"""
    GIGGLE: Sound
    """Giggling sound. (giggle)"""
    HAPPY: Sound
    """Happy sound. (happy)"""
    HELLO: Sound
    """Greeting sound. (hello)"""
    MYSTERIOUS: Sound
    """Mysterious sound. (mysterious)"""
    SAD: Sound
    """Sad sound. (sad)"""
    SLIDE: Sound
    """Sliding sound. (slide)"""
    SOARING: Sound
    """Soaring sound. (soaring)"""
    SPRING: Sound
    """Spring sound. (spring)"""
    TWINKLE: Sound
    """Twinkling sound. (twinkle)"""
    YAWN: Sound
    """Yawning sound. (yawn)"""