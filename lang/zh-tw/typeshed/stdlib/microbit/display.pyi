"""在 5×5 LED 顯示器上顯示文字、影像和動畫。 (顯示)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """取得 ``x`` 列和 ``y`` 行的 LED 亮度。 (取得像素)

Example: ``display.get_pixel(0, 0)``

:param x: (x) 顯示資料行 (0..4)
:param y: (y) 顯示資料列 (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """在 ``x`` 資料行和 ``y`` 資料列設定 LED 的亮度。 (設定像素)

Example: ``display.set_pixel(0, 0, 9)``

:param x: (x) 顯示資料行 (0..4)
:param y: (y) 顯示資料列 (0..4)
:param value: (數值) 0（關閉）和 9（最亮）之間的亮度"""
    ...

def clear() -> None:
    """將所有 LED 的亮度設定為 0（關閉）。 (clear)

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """在 LED 顯示器上顯示影像、字母或數字。 (show)

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: (圖片) 要顯示的字串、數字、影像或影像列表。
:param delay: (delay) 每個字母、數字或影像之間的顯示時間為 ``delay`` 毫秒。
:param wait: (wait) 如果 ``wait`` 為 ``True``，此函式將封鎖直到動畫完成，否則動畫將在背景發生。
:param loop: (loop) 如果 ``loop`` 為 ``True``，動畫將永遠重複。
:param clear: (clear) 如果 ``clear`` 為 ``True``，則顯示將在序列完成後清除。

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """捲動 LED 顯示器上的數字或文字。 (scroll)

Example: ``display.scroll('micro:bit')``

:param text: (text) 要捲動的字串。如果 ``text`` 是整數或浮點數，則首先使用 ``str()`` 將其轉換為字串。
:param delay: (delay) ``delay`` 參數能控制文字捲動的速度。
:param wait: (wait) 如果 ``wait`` 為 ``True``，此函式將封鎖直到動畫完成，否則動畫將在背景發生。
:param loop: (loop) 如果 ``loop`` 為 ``True``，動畫將永遠重複。
:param monospace: (monospace) 如果 ``monospace`` 為 ``True``，則字元的寬度將全部佔用 5 個像素資料行，否則捲動時每個字元之間將恰好有 1 個空白像素資料行。

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """打開 LED 顯示器。 (on)

Example: ``display.on()``"""
    ...

def off() -> None:
    """關閉 LED 顯示器（停用顯示器可讓您將 GPIO 引腳重新用於其他目的）。 (off)

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """檢查 LED 顯示器是否啟用。 (is on)

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """讀取光照水平。 (read light level)

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...