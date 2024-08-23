"""crwdns330040:0crwdne330040:0 (crwdns330038:0crwdne330038:0)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """crwdns330044:0``x``crwdnd330044:0``y``crwdne330044:0 (crwdns330042:0crwdne330042:0)

Example: ``display.get_pixel(0, 0)``

:param x: (crwdns330046:0crwdne330046:0) crwdns330048:0crwdne330048:0
:param y: (crwdns330050:0crwdne330050:0) crwdns330052:0crwdne330052:0
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """crwdns330056:0``x``crwdnd330056:0``y``crwdne330056:0 (crwdns330054:0crwdne330054:0)

Example: ``display.set_pixel(0, 0, 9)``

:param x: (crwdns330062:0crwdne330062:0) crwdns330064:0crwdne330064:0
:param y: (crwdns330066:0crwdne330066:0) crwdns330068:0crwdne330068:0
:param value: (crwdns330058:0crwdne330058:0) crwdns330060:0crwdne330060:0"""
    ...

def clear() -> None:
    """crwdns330072:0crwdne330072:0 (crwdns330070:0crwdne330070:0)

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """crwdns330076:0crwdne330076:0 (crwdns330074:0crwdne330074:0)

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: (crwdns330086:0crwdne330086:0) crwdns330088:0crwdne330088:0
:param delay: (crwdns330082:0crwdne330082:0) crwdns330084:0``delay``crwdne330084:0
:param wait: (crwdns330094:0crwdne330094:0) crwdns330096:0``wait``crwdnd330096:0``True``crwdne330096:0
:param loop: (crwdns330090:0crwdne330090:0) crwdns330092:0``loop``crwdnd330092:0``True``crwdne330092:0
:param clear: (crwdns330078:0crwdne330078:0) crwdns330080:0``clear``crwdnd330080:0``True``crwdne330080:0

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """crwdns330100:0crwdne330100:0 (crwdns330098:0crwdne330098:0)

Example: ``display.scroll('micro:bit')``

:param text: (crwdns330114:0crwdne330114:0) crwdns330116:0``text``crwdnd330116:0``str()``crwdne330116:0
:param delay: (crwdns330102:0crwdne330102:0) crwdns330104:0``delay``crwdne330104:0
:param wait: (crwdns330118:0crwdne330118:0) crwdns330120:0``wait``crwdnd330120:0``True``crwdne330120:0
:param loop: (crwdns330106:0crwdne330106:0) crwdns330108:0``loop``crwdnd330108:0``True``crwdne330108:0
:param monospace: (crwdns330110:0crwdne330110:0) crwdns330112:0``monospace``crwdnd330112:0``True``crwdne330112:0

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """crwdns330124:0crwdne330124:0 (crwdns330122:0crwdne330122:0)

Example: ``display.on()``"""
    ...

def off() -> None:
    """crwdns330128:0crwdne330128:0 (crwdns330126:0crwdne330126:0)

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """crwdns330132:0crwdne330132:0 (crwdns330130:0crwdne330130:0)

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """crwdns330136:0crwdne330136:0 (crwdns330134:0crwdne330134:0)

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...