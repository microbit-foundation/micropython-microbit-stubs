"""在5×5的 LED 显示屏上显示文字、图像和动画。 (显示)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """获取第``y``行第``x``列的 LED 亮度。

Example: ``display.get_pixel(0, 0)``

:param x: 显示屏的列(0..4)
:param y: 显示行 (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """设置在 ``x`` 列和 ``y`` 行的 LED 的亮度。

Example: ``display.set_pixel(0, 0, 9)``

:param x: 显示屏的列(0..4)
:param y: 显示行 (0..4)
:param value: 在 0 (关闭) 和 9 (亮) 之间的亮度"""
    ...

def clear() -> None:
    """将所有 LED 的亮度设置为 0（关闭）。 (清除)

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """在 LED 显示屏上显示图像、字母或数字。 (显示)

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: (图像) 要显示的一个字符串、数字、图像或图像列表。
:param delay: (延迟) 每个字母、数字或图像之间显示的间隔时间为 ``delay`` 毫秒。
:param wait: (等待) 如果 ``wait`` 为 ``True``，此函数将阻塞直到动画完成，否则动画将在后台发生。
:param loop: 如果 ``loop`` 为 ``True``, 动画将永远重复。
:param clear: (清除) 如果 ``clear`` 是 ``True``, 则显示将在序列完成后被清除。

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """在 LED 显示屏上滚动一个数字或文本。 (滚动)

Example: ``display.scroll('micro:bit')``

:param text: (文本) 要滚动的字符串。如果 ``text`` 是整数或浮点数，则首先使用 ``str()`` 将其转换为字符串。
:param delay: (延迟) ``delay`` 参数控制文本滚动的速度。
:param wait: (等待) 如果 ``wait`` 为 ``True``，此函数将阻塞直到动画完成，否则动画将发生在后台。
:param loop: 如果 ``loop`` 为 ``True``, 动画将永远重复。
:param monospace: (等宽) 如果 ``monospace`` 为 ``True``，则字符的宽度都将占用 5 个像素列，否则在滚动时每个字符之间将恰好有 1 个空白像素列。

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """打开 LED 显示屏。 (打开)

Example: ``display.on()``"""
    ...

def off() -> None:
    """关闭 LED 显示屏（禁用显示屏可让您将 GPIO 引脚重新用于其他用途）。 (关闭)

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """检查 LED 显示屏是否启用。

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """读取亮度。

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...