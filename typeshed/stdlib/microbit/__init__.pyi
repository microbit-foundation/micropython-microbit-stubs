"""The ``microbit`` module gives you access to all the hardware that is built-in
into your board.
"""

from typing import Any, List, overload

from . import accelerometer as accelerometer
from . import compass as compass
from . import display as display
from . import i2c as i2c
from . import microphone as microphone
from . import speaker as speaker
from . import spi as spi
from . import uart as uart

# V2 only
from .. import audio as audio

def panic(n: int) -> None:
    """Enter a panic mode. Requires restart. Pass in an arbitrary integer <= 255
    to indicate a status::

        microbit.panic(255)
    """

def reset() -> None:
    """Restart the board."""

def sleep(n: float) -> None:
    """Wait for ``n`` milliseconds. One second is 1000 milliseconds, so::

        microbit.sleep(1000)

    will pause the execution for one second.  ``n`` can be an integer or
    a floating point number.
    """

def running_time() -> int:
    """Return the number of milliseconds since the board was switched on or
    restarted.
    """

def temperature() -> int:
    """Return the temperature of the micro:bit in degrees Celcius."""

def set_volume(v: int) -> None:
    """Sets the volume. ``v`` is a value between 0 and 255.

    **V2** only.

    Out of range values will be clamped to 0 or 255.
    """
    ...

class Button:
    """Represents a button.

    .. note::
        This class is not actually available to the user, it is only used by
        the two button instances, which are provided already initialized.
    """

    def is_pressed(self) -> bool:
        """Returns ``True`` if the specified button ``button`` is pressed, and
        ``False`` otherwise.
        """
        ...
    def was_pressed(self) -> bool:
        """Returns ``True`` or ``False`` to indicate if the button was pressed
        since the device started or the last time this method was called.

        Calling this method will clear the press state so
        that the button must be pressed again before this method will return
        ``True`` again.
        """
        ...
    def get_presses(self) -> int:
        """Returns the running total of button presses, and resets this total
        to zero before returning.
        """
        ...

button_a: Button
"""A ``Button`` instance representing the left button."""

button_b: Button
"""Represents the right button."""

class MicroBitDigitalPin:
    """The pins are your board's way to communicate with external devices connected to
    it. There are 19 pins for your disposal, numbered 0-16 and 19-20. Pins 17 and
    18 are not available. There is also a ``pin_logo`` **V2** and ``pin_speaker``
    **V2** available to use with the latest micro:bit device.
    """

    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int
    def read_digital(self) -> int:
        """Return 1 if the pin is high, and 0 if it's low."""
        ...
    def write_digital(self, value: int) -> None:
        """Set the pin to high if ``value`` is 1, or to low, if it is 0."""
        ...
    def set_pull(self, value: int) -> None:
        """Set the pull state to one of three possible values: ``pin.PULL_UP``,
        ``pin.PULL_DOWN`` or ``pin.NO_PULL`` (where ``pin`` is an instance of
        a pin). See below for discussion of default pull states.
        """
        ...
    def get_pull(self) -> int:
        """Returns the pull configuration on a pin, which can be one of three
        possible values: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``. These
        are set using the ``set_pull()`` method or automatically configured
        when a pin mode requires it."""
        ...
    def get_mode(self) -> str:
        """Returns the pin mode. When a pin is used for a specific function, like
        writing a digital value, or reading an analog value, the pin mode
        changes. Pins can have one of the following modes: ``"unused"``,
        ``"analog"``, ``"read_digital"``, ``"write_digital"``,
        ``"display"``, ``"button"``, ``"music"``, ``"audio"``,
        ``"touch"``, ``"i2c"``, ``"spi"``.
        """
        ...

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    def read_analog(self) -> int:
        """Read the voltage applied to the pin, and return it as an integer
        between 0 (meaning 0V) and 1023 (meaning 3.3V).
        """
    def write_analog(self, value: int) -> None:
        """Output a PWM signal on the pin, with the duty cycle proportional to
        the provided ``value``. The ``value`` may be either an integer or a
        floating point number between 0 (0% duty cycle) and 1023 (100% duty).
        """
    def set_analog_period(self, period: int) -> None:
        """Set the period of the PWM signal being output to ``period`` in
        milliseconds. The minimum valid value is 1ms.
        """
    def set_analog_period_microseconds(self, period: int) -> None:
        """Set the period of the PWM signal being output to ``period`` in
        microseconds. The minimum valid value is 256µs.
        """

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    CAPACITIVE: int
    RESISTIVE: int
    def is_touched(self) -> bool:
        """Return ``True`` if the pin is being touched with a finger, otherwise
        return ``False``.

        .. note::
            The default touch mode for the pins on the edge connector is
            `resistive`. The default for the logo pin **V2** is `capacitive`.

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
        """
        ...
        def set_touch_mode(value: int) -> None:
            """
            .. note::
                The default touch mode for the pins on the edge connector is
                `resistive`. The default for the logo pin **V2** is `capacitive`.

            Set the touch mode for the given pin. Value can be either ``CAPACITIVE``
            or ``RESISTIVE``. For example, ``pin0.set_touch_mode(pin0.CAPACITIVE)``.
            """
            ...

pin0: MicroBitTouchPin
"""A MicroBitTouchPin labelled 0 on the board."""

pin1: MicroBitTouchPin
"""A MicroBitTouchPin labelled 1 on the board."""

pin2: MicroBitTouchPin
"""A MicroBitTouchPin labelled 2 on the board."""

pin3: MicroBitAnalogDigitalPin
"""A MicroBitAnalogDigitalPin."""

pin4: MicroBitAnalogDigitalPin
"""A MicroBitAnalogDigitalPin."""

pin5: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin6: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin7: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin8: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin9: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin10: MicroBitAnalogDigitalPin
"""A MicroBitAnalogDigitalPin."""

pin11: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin12: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin13: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin14: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin15: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin16: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin19: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin20: MicroBitDigitalPin
"""A MicroBitDigitalPin."""

pin_logo: MicroBitTouchPin
"""A touch sensitive logo pin on the front of the micro:bit, which by default is set to capacitive touch mode."""

pin_speaker: MicroBitAnalogDigitalPin
"""A pin to address the micro:bit speaker.

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128)."""

class Image:
    """The ``Image`` class is used to create images that can be displayed easily on
    the device's LED matrix. Given an image object it's possible to display it via
    the ``display`` API::

        display.show(Image.HAPPY)
    """

    HEART: Image
    """An image."""

    HEART_SMALL: Image
    """An image."""

    HAPPY: Image
    """An image."""

    SMILE: Image
    """An image."""

    SAD: Image
    """An image."""

    CONFUSED: Image
    """An image."""

    ANGRY: Image
    """An image."""

    ASLEEP: Image
    """An image."""

    SURPRISED: Image
    """An image."""

    SILLY: Image
    """An image."""

    FABULOUS: Image
    """An image."""

    MEH: Image
    """An image."""

    YES: Image
    """An image."""

    NO: Image
    """An image."""

    CLOCK12: Image
    """An image."""

    CLOCK11: Image
    """An image."""

    CLOCK10: Image
    """An image."""

    CLOCK9: Image
    """An image."""

    CLOCK8: Image
    """An image."""

    CLOCK7: Image
    """An image."""

    CLOCK6: Image
    """An image."""

    CLOCK5: Image
    """An image."""

    CLOCK4: Image
    """An image."""

    CLOCK3: Image
    """An image."""

    CLOCK2: Image
    """An image."""

    CLOCK1: Image
    """An image."""

    ARROW_N: Image
    """An image."""

    ARROW_NE: Image
    """An image."""

    ARROW_E: Image
    """An image."""

    ARROW_SE: Image
    """An image."""

    ARROW_S: Image
    """An image."""

    ARROW_SW: Image
    """An image."""

    ARROW_W: Image
    """An image."""

    ARROW_NW: Image
    """An image."""

    TRIANGLE: Image
    """An image."""

    TRIANGLE_LEFT: Image
    """An image."""

    CHESSBOARD: Image
    """An image."""

    DIAMOND: Image
    """An image."""

    DIAMOND_SMALL: Image
    """An image."""

    SQUARE: Image
    """An image."""

    SQUARE_SMALL: Image
    """An image."""

    RABBIT: Image
    """An image."""

    COW: Image
    """An image."""

    MUSIC_CROTCHET: Image
    """An image."""

    MUSIC_QUAVER: Image
    """An image."""

    MUSIC_QUAVERS: Image
    """An image."""

    PITCHFORK: Image
    """An image."""

    XMAS: Image
    """An image."""

    PACMAN: Image
    """An image."""

    TARGET: Image
    """An image."""

    TSHIRT: Image
    """An image."""

    ROLLERSKATE: Image
    """An image."""

    DUCK: Image
    """An image."""

    HOUSE: Image
    """An image."""

    TORTOISE: Image
    """An image."""

    BUTTERFLY: Image
    """An image."""

    STICKFIGURE: Image
    """An image."""

    GHOST: Image
    """An image."""

    SWORD: Image
    """An image."""

    GIRAFFE: Image
    """An image."""

    SKULL: Image
    """An image."""

    UMBRELLA: Image
    """An image."""

    SNAKE: Image
    """An image."""

    ALL_CLOCKS: List[Image]
    """A list containing all the CLOCK_ images in sequence."""

    ALL_ARROWS: List[Image]
    """A list containing all the ARROW_ images in sequence."""
    @overload
    def __init__(self, string: str) -> None:
        """``string`` has to consist of digits 0-9 arranged into lines,
        describing the image, for example::

            image = Image("90009:"
                          "09090:"
                          "00900:"
                          "09090:"
                          "90009")

        will create a 5×5 image of an X. The end of a line is indicated by a
        colon. It's also possible to use a newline (\\n) to indicate the end of
        a line like this::

            image = Image("90009\\n"
                          "09090\\n"
                          "00900\\n"
                          "09090\\n"
                          "90009")
        """
        ...
    @overload
    def __init__(
        self, width: int = None, height: int = None, buffer: Any = None
    ) -> None:
        """Create an empty image with ``width`` columns and ``height`` rows.
        Optionally ``buffer`` can be an array of ``width``×``height`` integers
        in range 0-9 to initialize the image::

            Image(2, 2, b'\x08\x08\x08\x08')

        or::

            Image(2, 2, bytearray([9,9,9,9]))

        Will create a 2 x 2 pixel image at full brightness.

        .. note::

            Keyword arguments cannot be passed to ``buffer``.
        """
        ...
    def width(self) -> int:
        """Return the number of columns in the image."""
        ...
    def height(self) -> int:
        """Return the numbers of rows in the image."""
        ...
    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Set the brightness of the pixel at column ``x`` and row ``y`` to the
        ``value``, which has to be between 0 (dark) and 9 (bright).

        This method will raise an exception when called on any of the built-in
        read-only images, like ``Image.HEART``.
        """
        ...
    def get_pixel(self, x: int, y: int) -> int:
        """Return the brightness of pixel at column ``x`` and row ``y`` as an
        integer between 0 and 9.
        """
        ...
    def shift_left(self, n: int) -> Image:
        """Return a new image created by shifting the picture left by ``n``
        columns.
        """
        ...
    def shift_right(self, n: int) -> Image:
        """Same as ``image.shift_left(-n)``."""
        ...
    def shift_up(self, n: int) -> Image:
        """Return a new image created by shifting the picture up by ``n``
        rows.
        """
        ...
    def shift_down(self, n: int) -> Image:
        """Same as ``image.shift_up(-n)``."""
        ...
    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Return a new image by cropping the picture to a width of ``w`` and a
        height of ``h``, starting with the pixel at column ``x`` and row
        ``y``.
        """
        ...
    def copy(self) -> Image:
        """Return an exact copy of the image."""
        ...
    def invert(self) -> Image:
        """Return a new image by inverting the brightness of the pixels in the
        source image."""
        ...
    def fill(self, value: int) -> None:
        """Set the brightness of all the pixels in the image to the
        ``value``, which has to be between 0 (dark) and 9 (bright).

        This method will raise an exception when called on any of the built-in
        read-only images, like ``Image.HEART``.
        """
        ...
    def blit(
        self,
        src: Image,
        x: int,
        y: int,
        w: int,
        h: int,
        xdest: int = ...,
        ydest: int = ...,
    ) -> None:
        """Copy the rectangle defined by ``x``, ``y``, ``w``, ``h`` from the
        image ``src`` into this image at ``xdest``, ``ydest``. Areas in the
        source rectangle, but outside the source image are treated as having a
        value of 0.

        ``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()``
        and ``crop()`` can are all implemented by using ``blit()``.

        For example, img.crop(x, y, w, h) can be implemented as::

            def crop(self, x, y, w, h):
                res = Image(w, h)
                res.blit(self, x, y, w, h)
                return res
        """
        ...
    def __repr__(self) -> str:
        """Get a compact string representation of the image."""
        ...
    def __str__(self) -> str:
        """Get a readable string representation of the image."""
        ...
    def __add__(self, other: Image) -> Image:
        """Create a new image by adding the brightness values from the two
        images for each pixel.
        """
        ...
    def __sub__(self, other: Image) -> Image:
        """Create a new image by subtracting the brightness values of the
        other image from this image.
        """
        ...
    def __mul__(self, n: float) -> Image:
        """Create a new image by multiplying the brightness of each pixel by
        ``n``.
        """
        ...
    def __div__(self, other: float) -> Image:
        """Create a new image by multiplying the brightness of each pixel by
        ``n``.
        """
        ...

class SoundEvent:
    """Represents the transition of sound events, from ``loud`` to ``quiet`` like speaking or background music."""

    LOUD: SoundEvent
    """Represents the transition of sound events, from ``quiet`` to ``loud`` like clapping or shouting."""
    QUIET: SoundEvent

class Sound:
    """The built-in sounds can be called using ``audio.play(Sound.NAME)``."""

    GIGGLE: Sound
    """A sound."""

    HAPPY: Sound
    """A sound."""

    HELLO: Sound
    """A sound."""

    MYSTERIOUS: Sound
    """A sound."""

    SAD: Sound
    """A sound."""

    SLIDE: Sound
    """A sound."""

    SOARING: Sound
    """A sound."""

    SPRING: Sound
    """A sound."""

    TWINKLE: Sound
    """A sound."""

    YAWN: Sound
    """A sound."""
