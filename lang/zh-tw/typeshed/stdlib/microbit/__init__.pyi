"""引腳、影像、聲音、溫度和音量。"""
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
    """安排一個函式以指定的時間間隔叫用 **僅限 V2**。

Example: ``run_every(my_logging, min=5)``

This function can be passed a callback::

    run_every(your_function, h=1, min=20, s=30, ms=50)

or used as a decorator::

    @run_every(h=1, min=20, s=30, ms=50)
    def your_function():
        pass

Arguments with different time units are additive.

:param callback: 要叫用的回呼。做為裝飾項目時省略。
:param days: 以天數為單位的間隔。
:param h: 以小時為單位的間隔。
:param min: 以分鐘為單位的間隔。
:param s: 以秒為單位的間隔。
:param ms: 以毫秒為單位的間隔。"""

def panic(n: int) -> None:
    """進入緊急模式。

Example: ``panic(127)``

:param n: 任意整數 <= 255 表示狀態。

Requires restart."""

def reset() -> None:
    """重啟板子。"""

def sleep(n: float) -> None:
    """等待 ``n`` 毫秒。

Example: ``sleep(1000)``

:param n: 要等待的毫秒數。

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """取得板子的執行時間。

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """取得 micro:bit 的溫度 (以攝氏為單位)。 (溫度)"""

def set_volume(v: int) -> None:
    """設定音量。

Example: ``set_volume(127)``

:param v: 介於 0 (低) 和 255 (高) 之間的值。

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """按鈕 ``button_a`` 和 ``button_b`` 的類別。"""

    def is_pressed(self) -> bool:
        """檢查按鈕是否按下。

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """檢查自裝置啟動或上次呼叫此方法以來是否按下該按鈕。

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """取得按下按鈕的執行總數，並在傳回前，將此總數重設為零。

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""左鍵 ``Button`` 物件。"""
button_b: Button
"""右鍵 ``Button`` 物件。"""

class MicroBitDigitalPin:
    """數位引腳。

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """取得引腳的數位值。

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """設定引腳的數位值。

Example: ``pin0.write_digital(1)``

:param value: 1 將引腳設為高電平，或 0 將引腳設為低電平"""
        ...

    def set_pull(self, value: int) -> None:
        """將提取狀態設為三個可能值之一：``PULL_UP``、``PULL_DOWN`` 或 ``NO_PULL``。

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: 相關引腳的提取狀態，例如 ``pin0.PULL_UP``。"""
        ...

    def get_pull(self) -> int:
        """取得引腳上的提取狀態。

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """傳回引腳模式。

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """在引腳上輸出 PWM 訊號，工作週期與 ``value`` 成正比。

Example: ``pin0.write_analog(254)``

:param value: 介於 0 (0% 工作週期) 和 1023 (100% 工作週期) 之間的整數或浮點數。"""

    def set_analog_period(self, period: int) -> None:
        """將輸出的 PWM 訊號週期設為 ``period`` (以毫秒為單位)。

Example: ``pin0.set_analog_period(10)``

:param period: 以毫秒為單位的週期，最小有效值為 1ms。"""

    def set_analog_period_microseconds(self, period: int) -> None:
        """將輸出的 PWM 訊號週期設為 ``period`` (以微秒為單位)。

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: 以微秒為單位的週期，最小有效值為 256µs。"""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """具有類比和數位功能的引腳。"""

    def read_analog(self) -> int:
        """讀取施加到引腳的電壓。

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """具有類比、數位和觸控功能的引腳。"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """檢查引腳是否受觸控。

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
        """設定引腳的觸控模式。

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: 相關引腳的 ``CAPACITIVE`` 或 ``RESISTIVE``。"""
        ...
pin0: MicroBitTouchPin
"""具有數位、類比和觸控功能的引腳。"""
pin1: MicroBitTouchPin
"""具有數位、類比和觸控功能的引腳。"""
pin2: MicroBitTouchPin
"""具有數位、類比和觸控功能的引腳。"""
pin3: MicroBitAnalogDigitalPin
"""具有數位和類比功能的引腳。"""
pin4: MicroBitAnalogDigitalPin
"""具有數位和類比功能的引腳。"""
pin5: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin6: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin7: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin8: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin9: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin10: MicroBitAnalogDigitalPin
"""具有數位和類比功能的引腳。"""
pin11: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin12: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin13: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin14: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin15: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin16: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin19: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin20: MicroBitDigitalPin
"""具有數位功能的引腳。"""
pin_logo: MicroBitTouchPin
"""micro:bit 正面的觸控感應標誌引腳，預設為電容式觸控模式。"""
pin_speaker: MicroBitAnalogDigitalPin
"""用於定址 micro:bit 揚聲器的引腳。

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """要在 micro:bit LED 顯示器上顯示的圖片。

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """愛心圖片。"""
    HEART_SMALL: Image
    """小愛心影像。"""
    HAPPY: Image
    """開心的臉圖片。"""
    SMILE: Image
    """微笑的臉圖片。"""
    SAD: Image
    """傷心的臉圖片。"""
    CONFUSED: Image
    """困惑的臉圖片。"""
    ANGRY: Image
    """生氣的臉圖片。"""
    ASLEEP: Image
    """瞌睡的臉圖片。"""
    SURPRISED: Image
    """驚訝的臉圖片。"""
    SILLY: Image
    """鬼臉圖片。"""
    FABULOUS: Image
    """戴太陽眼鏡的臉圖片。"""
    MEH: Image
    """冷漠的臉圖片。"""
    YES: Image
    """勾號圖片。"""
    NO: Image
    """叉號圖片。"""
    CLOCK12: Image
    """指針指向 12 點鐘的圖片。"""
    CLOCK11: Image
    """指針指向 11 點鐘的圖片。"""
    CLOCK10: Image
    """指針指向 10 點鐘的圖片。"""
    CLOCK9: Image
    """指針指向 9 點鐘的圖片。"""
    CLOCK8: Image
    """指針指向 8 點鐘的圖片。"""
    CLOCK7: Image
    """指針指向 7 點鐘的圖片。"""
    CLOCK6: Image
    """指針指向 6 點鐘的圖片。"""
    CLOCK5: Image
    """指針指向 5 點鐘的圖片。"""
    CLOCK4: Image
    """指針指向 4 點鐘的圖片。"""
    CLOCK3: Image
    """指針指向 3 點鐘的圖片。"""
    CLOCK2: Image
    """指針指向 2 點鐘的圖片。"""
    CLOCK1: Image
    """指針指向 1 點鐘的圖片。"""
    ARROW_N: Image
    """指向北方箭頭的圖片。"""
    ARROW_NE: Image
    """指向東北箭頭的圖片。"""
    ARROW_E: Image
    """指向東方箭頭的圖片。"""
    ARROW_SE: Image
    """指向東南箭頭的圖片。"""
    ARROW_S: Image
    """指向南方箭頭的圖片。"""
    ARROW_SW: Image
    """指向西南箭頭的圖片。"""
    ARROW_W: Image
    """指向西方箭頭的圖片。"""
    ARROW_NW: Image
    """指向西北箭頭的圖片。"""
    TRIANGLE: Image
    """朝上三角形的圖片。"""
    TRIANGLE_LEFT: Image
    """左角三角形的圖片。"""
    CHESSBOARD: Image
    """以棋盤圖案交錯發亮的 LED 燈。"""
    DIAMOND: Image
    """鑽石圖片。"""
    DIAMOND_SMALL: Image
    """小鑽石圖片。"""
    SQUARE: Image
    """正方形圖片。"""
    SQUARE_SMALL: Image
    """小正方形圖片。"""
    RABBIT: Image
    """兔子圖片。"""
    COW: Image
    """乳牛圖片。"""
    MUSIC_CROTCHET: Image
    """四分音符圖片。"""
    MUSIC_QUAVER: Image
    """八分音符圖片。"""
    MUSIC_QUAVERS: Image
    """一組八分音符圖片。"""
    PITCHFORK: Image
    """乾草叉圖片。"""
    XMAS: Image
    """聖誕樹圖片。"""
    PACMAN: Image
    """吃豆人街機角色圖片。"""
    TARGET: Image
    """靶子圖片。"""
    TSHIRT: Image
    """T 恤圖片。"""
    ROLLERSKATE: Image
    """輪式溜冰鞋圖片。"""
    DUCK: Image
    """鴨子圖片。"""
    HOUSE: Image
    """房子圖片。"""
    TORTOISE: Image
    """陸龜圖片。"""
    BUTTERFLY: Image
    """蝴蝶圖片。"""
    STICKFIGURE: Image
    """簡筆人物畫圖片。"""
    GHOST: Image
    """幽靈圖片。"""
    SWORD: Image
    """劍圖片。"""
    GIRAFFE: Image
    """長頸鹿圖片。"""
    SKULL: Image
    """骷髏頭圖片。"""
    UMBRELLA: Image
    """雨傘圖片。"""
    SNAKE: Image
    """蛇圖片。"""
    ALL_CLOCKS: List[Image]
    """按順序包含所有時鐘圖片的清單。"""
    ALL_ARROWS: List[Image]
    """按順序包含所有箭頭圖片的清單。"""

    @overload
    def __init__(self, string: str) -> None:
        """從描述點亮哪些 LED 的字串建立圖片。

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: 描述圖片的字串。"""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """建立一個 ``width`` 行 ``height`` 列的空白圖片。

:param width: 可選的圖片寬度
:param height: 可選的圖片高度
:param buffer: 用可選陣列或在 0-9 範圍內的 ``width``×``height`` 整數位元組，來初始化圖片

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """取得行數。

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """取得列數。

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """設定像素的亮度。

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: 行號
:param y: 列號
:param value: 亮度為介於 0 (暗) 和 9 (亮) 之間的整數

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """取得像素的亮度。

Example: ``my_image.get_pixel(0, 0)``

:param x: 行號
:param y: 列號
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """透過向左移動圖片，以建立一個新影像。

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: 要移動的行數
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """透過向右移動圖片，以建立一個新影像。

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: 要移動的行數
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """透過向上移動圖片，以建立一個新影像。

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: 要移動的列數
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """透過向下移動圖片，以建立一個新影像。

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: 要移動的列數
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """透過裁剪圖片，以建立一個新影像。

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: 裁剪位移行
:param y: 裁剪位移列
:param w: 剪裁寬度
:param h: 剪裁高度
:return: The new image"""
        ...

    def copy(self) -> Image:
        """建立影像的精確副本。

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """透過反轉來源影像的像素亮度，以建立一個新影像。

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """設定影像中所有像素的亮度。

Example: ``my_image.fill(5)``

:param value: 新亮度為 0 (暗) 和 9 (亮) 之間的數字。

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """將另一個影像中的一個區域複製到該影像中。

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: 來源影像
:param x: 來源影像中的起始資料行偏移量
:param y: 來源影像中的起始資料列偏移量
:param w: 要複製的資料行
:param h: 要複製的資料列
:param xdest: 此影像中要修改的資料列偏移量
:param ydest: 此影像中要修改的資料列偏移量

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
        """取得影像的緊湊字串顯示。"""
        ...

    def __str__(self) -> str:
        """取得影像的可讀字串顯示。"""
        ...

    def __add__(self, other: Image) -> Image:
        """透過將兩個影像的像素亮度值相加，以建立一個新影像。

Example: ``Image.HEART + Image.HAPPY``

:param other: 要新增的影像。"""
        ...

    def __sub__(self, other: Image) -> Image:
        """透過從該影像中減去另一個影像的亮度值，以建立一個新影像。

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: 要減去的影像。"""
        ...

    def __mul__(self, n: float) -> Image:
        """透過將各像素的亮度乘以 ``n``，以建立一個新影像。

Example: ``Image.HEART * 0.5``

:param n: 要乘以的值。"""
        ...

    def __truediv__(self, n: float) -> Image:
        """透過將各像素的亮度除以 ``n``，以建立一個新影像。

Example: ``Image.HEART / 2``

:param n: 要除以的值。"""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """表示聲音事件的轉換，從 ``quiet`` 到 ``loud``，如鼓掌或喊叫。"""
    QUIET: SoundEvent
    """表示聲音事件的轉換，從 ``loud`` 到 ``quiet``，例如說話或背景音樂。"""

class Sound:
    """可以使用 ``audio.play(Sound.NAME)`` 調用內建聲音。"""
    GIGGLE: Sound
    """咯咯笑的聲音。"""
    HAPPY: Sound
    """開心的聲音。"""
    HELLO: Sound
    """歡迎的聲音。"""
    MYSTERIOUS: Sound
    """神祕的聲音。"""
    SAD: Sound
    """難過的聲音。"""
    SLIDE: Sound
    """滑動的聲音。"""
    SOARING: Sound
    """高昂的聲音。"""
    SPRING: Sound
    """彈跳的聲音。"""
    TWINKLE: Sound
    """閃亮的聲音。"""
    YAWN: Sound
    """呵欠的聲音。"""