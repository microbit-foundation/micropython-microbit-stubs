"""Show text, images and animations on the 5×5 LED display.
"""

from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Get the brightness of the LED at column ``x`` and row ``y``.

    :param x: The display column (0..4)
    :param y: The display row (0..4)
    :return: A number between 0 (off) and 9 (bright)
    """
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Set the brightness of the LED at column ``x`` and row ``y``.

    :param x: The display column (0..4)
    :param y: The display row (0..4)
    :param value: The brightness between 0 (off) and 9 (bright)
    """
    ...

def clear() -> None:
    """Set the brightness of all LEDs to 0 (off)."""
    ...

def show(
    value: Union[str, float, int, Image, Iterable[Image]],
    delay: int = 400,
    wait: bool = True,
    loop: bool = False,
    clear: bool = False,
) -> None:
    """Shows images, letters or digits on the display.

    For example, ``display.show(Image.HEART)`` or ``display.show("ABC")``.

    When ``value`` is an image or a list of images then each image is displayed in turn.
    When ``value`` is a string or number then each letter or digit is displayed in turn.

    :param value: A string, number, image or list of images to show.
    :param delay: Each letter, digit or image is shown with ``delay`` milliseconds between them.
    :param wait: If ``wait`` is ``True``, this function will block until the animation is finished, otherwise the animation will happen in the background.
    :param loop: If ``loop`` is ``True``, the animation will repeat forever.
    :param clear: If ``clear`` is ``True``, the display will be cleared after the sequence has finished.

    The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword.
    """
    ...

def scroll(
    value: Union[str, float, int],
    delay: int = 150,
    wait: bool = True,
    loop: bool = False,
    monospace: bool = False,
) -> None:
    """Scrolls a number or text on the display.

    :param value: The string to scroll. If ``value`` is an integer or float it is first converted to a string using ``str()``.
    :param delay: The ``delay`` parameter controls how fast the text is scrolling.
    :param wait: If ``wait`` is ``True``, this function will block until the animation is finished, otherwise the animation will happen in the background.
    :param loop: If ``loop`` is ``True``, the animation will repeat forever.
    :param monospace: If ``monospace`` is ``True``, the characters will all take up 5 pixel-columns in width, otherwise there will be exactly 1 blank pixel-column between each character as they scroll.

    The ``wait``, ``loop`` and ``monospace`` arguments must be specified
    using their keyword.
    """
    ...

def on() -> None:
    """Turn on the display."""
    ...

def off() -> None:
    """Turn off the display (allowing you to re-use the GPIO pins associated with the display for other purposes)."""
    ...

def is_on() -> bool:
    """Check whether the display is on.

    :return: ``True`` if the display is on, otherwise returns ``False``.
    """
    ...

def read_light_level() -> int:
    """Read the light level.

    Uses the display's LEDs in reverse-bias mode to sense the amount of light
    falling on the display.

    :return: An integer between 0 and 255 representing the light level, with larger meaning more light.
    """
    ...
