"""在 5×5 LED 顯示器上顯示文字、圖像和動畫。"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """取得行 ``x`` 和列 ``y`` 的 LED 亮度。

Example: ``display.get_pixel(0, 0)``

:param x: 顯示行 (0..4)
:param y: 顯示列 (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """在行 ``x`` 和列 ``y`` 設定 LED 亮度。

Example: ``display.set_pixel(0, 0, 9)``

:param x: 顯示行 (0..4)
:param y: 顯示列 (0..4)
:param value: 0 (關閉) 和 9 (最亮) 之間的亮度"""
    ...

def clear() -> None:
    """將所有 LED 的亮度設定為 0 (關閉)。

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """在 LED 顯示器上顯示圖像、字母或數字。

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: 要顯示的字串、數字、圖像或圖像列表。
:param delay: 每個字母、數字或圖像之間的顯示時間為 ``delay`` 毫秒。
:param wait: 如果 ``wait`` 為 ``True``，此函式將封鎖直到動畫完成，否則動畫將在背景發生。
:param loop: 如果 ``loop`` 為 ``True``，動畫將永遠重複。
:param clear: 如果 ``clear`` 為 ``True``，則顯示將在序列完成後被清除。

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """捲動 LED 顯示器上的數字或文字。

Example: ``display.scroll('micro:bit')``

:param text: 要捲動的字串。如果 ``text`` 是整數或浮點數，則先使用 ``str()`` 將其轉換為字串。
:param delay: ``delay`` 參數可控制文字捲動的速度。
:param wait: 如果 ``wait`` 為 ``True``，此函式將封鎖直到動畫完成，否則動畫將在背景發生。
:param loop: 如果 ``loop`` 為 ``True``，動畫將永遠重複。
:param monospace: 如果 ``monospace`` 為 ``True``，字元寬度將全部佔用 5 個像素行。否則，捲動時每個字元之間將恰好有 1 個空白像素行。

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """開啟 LED 顯示器。

Example: ``display.on()``"""
    ...

def off() -> None:
    """關閉 LED 顯示器 (停用顯示器，可讓您將 GPIO 引腳重新用於其他目的)。

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """檢查 LED 顯示器是否有啟用。

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """讀取光度。

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...