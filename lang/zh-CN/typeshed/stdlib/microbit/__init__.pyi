"""引脚、图像、声音、温度和音量。 (Microbit)"""
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
    """计划以时间参数指定的时间间隔运行函数**仅限V2** 。 (周期性运行)

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

:param callback: 在提供的时间间隔内调用的函数。用作装饰器时省略。
:param days: (天) 设置定时计划的日期标记。
:param h: 设置定时计划的小时标记。
:param min: (分钟) 设置定时计划的分钟标记。
:param s: (秒) 设置定时计划的秒标记。
:param ms: (毫秒) 设置定时计划的毫秒标记。"""

def panic(n: int) -> None:
    """进入 panic （恐慌）模式。 (恐慌)

Example: ``panic(127)``

:param n: 一个 <= 255 的任意整数，以表示一个状态。

Requires restart."""

def reset() -> None:
    """重启主板。"""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """将一个数值从一个范围转换为整数范围。 (范围)

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: 要转换的数字。
:param from_: (从) 一个元组，用于定义要转换的范围。
:param to: (至) 一个元组，用于定义要转换到的范围。
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """将一个数值从一个范围转换为浮点数范围。 (范围)

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: 要转换的数字。
:param from_: (从) 一个元组，用于定义要转换的范围。
:param to: (至) 一个元组，用于定义要转换到的范围。
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """等待 ``n`` 毫秒。 (休眠)

Example: ``sleep(1000)``

:param n: 要等待的毫秒数

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """获取主板的运行时间。

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """以摄氏度为单位获取 micro:bit 的温度。"""

def set_volume(v: int) -> None:
    """设置音量。

Example: ``set_volume(127)``

:param v: 一个介于 0 (低) 和 255 (高) 之间的值。

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """按钮 ``button_a`` 和 ``button_b`` 的类。"""

    def is_pressed(self) -> bool:
        """检查按钮是否被按下。

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """检查按钮自设备启动以来或者上次调用此方法之后是否被按下。

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """获得按钮被按下的总计次数，并在返回之前将该总计次数重置为 0。

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""左键 ``Button`` 对象。 (按钮 a)"""
button_b: Button
"""右键 ``Button`` 对象。 (按钮 b)"""

class MicroBitDigitalPin:
    """数字引脚。 (Microbit 数字引脚)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """获取引脚的数字值。

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """设置引脚的数字值。

Example: ``pin0.write_digital(1)``

:param value: 1 将引脚设置为高电平，或 0 将引脚设置为低电平"""
        ...

    def set_pull(self, value: int) -> None:
        """将拉取状态设置为以下三个可能的值之一：``PULL_UP``、``PULL_DOWN`` 或 N``NO_PULL``。

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: 相关引脚的拉取状态，例如： ``pin0.PULL_UP``。"""
        ...

    def get_pull(self) -> int:
        """获取引脚上的拉取状态。

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """返回引脚模式。

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """在引脚上输出 PWM 信号，占空比为 ``value``。

Example: ``pin0.write_analog(254)``

:param value: 介于 0（0% 占空比）和 1023（100% 占空比）之间的整数或浮点数。"""

    def set_analog_period(self, period: int) -> None:
        """将输出的 PWM 信号的周期设置为 ``period``（单位：毫秒）。

Example: ``pin0.set_analog_period(10)``

:param period: 以毫秒为单位的周期，最小有效值为 1 毫秒。"""

    def set_analog_period_microseconds(self, period: int) -> None:
        """将输出的 PWM 信号的周期设置为 ``period``（单位：微秒）。

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: 以微秒为单位的周期，最小有效值为 256 毫秒。"""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """带有模拟和数字功能的引脚。"""

    def read_analog(self) -> int:
        """读取应用于引脚的电压。

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """带有模拟、数字和触摸功能的引脚。"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """检查引脚是否被触摸。

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
        """设置引脚的触摸模式。

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: 来自相关引脚的 ``CAPACITIVE`` 或 ``RESISTIVE``。"""
        ...
pin0: MicroBitTouchPin
"""具有数字、模拟和触摸功能的引脚。 (引脚0)"""
pin1: MicroBitTouchPin
"""具有数字、模拟和触摸功能的引脚。 (引脚1)"""
pin2: MicroBitTouchPin
"""具有数字、模拟和触摸功能的引脚。 (引脚2)"""
pin3: MicroBitAnalogDigitalPin
"""具有数字和模拟功能的引脚。 (引脚3)"""
pin4: MicroBitAnalogDigitalPin
"""具有数字和模拟功能的引脚。 (引脚4)"""
pin5: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚5)"""
pin6: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚6)"""
pin7: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚7)"""
pin8: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚8)"""
pin9: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚9)"""
pin10: MicroBitAnalogDigitalPin
"""具有数字和模拟功能的引脚。 (引脚10)"""
pin11: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚11)"""
pin12: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚12)"""
pin13: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚13)"""
pin14: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚14)"""
pin15: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚15)"""
pin16: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚16)"""
pin19: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚19)"""
pin20: MicroBitDigitalPin
"""具有数字功能的引脚。 (引脚20)"""
pin_logo: MicroBitTouchPin
"""micro:bit 正面的触摸感应标志引脚，默认设置为电容式触摸模式。 (引脚标志)"""
pin_speaker: MicroBitAnalogDigitalPin
"""用于对 micro:bit 扬声器寻址的引脚。 (扬声器引脚)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """在 micro:bit LED 显示屏上显示的图像。 (图像)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """心形图像 (心形)"""
    HEART_SMALL: Image
    """小的心形图像。 (小的心形)"""
    HAPPY: Image
    """快乐的脸部图像。 (快乐)"""
    SMILE: Image
    """微笑的脸部图像。 (微笑)"""
    SAD: Image
    """难过的脸部图像。 (难过)"""
    CONFUSED: Image
    """困惑的面部图像。 (困惑)"""
    ANGRY: Image
    """愤怒的脸部图像。 (愤怒)"""
    ASLEEP: Image
    """睡着的脸部图像。 (睡着)"""
    SURPRISED: Image
    """惊讶的脸部图像。 (惊讶)"""
    SILLY: Image
    """傻傻的脸部图像。 (傻的)"""
    FABULOUS: Image
    """戴墨镜的脸部图像。 (极好的)"""
    MEH: Image
    """印象平平的脸部图像 (不感兴趣的)"""
    YES: Image
    """对勾图像。 (是的)"""
    NO: Image
    """打叉图像。 (不是)"""
    CLOCK12: Image
    """指针指向 12 点钟位置的图像。 (时钟12点)"""
    CLOCK11: Image
    """指针指向 11 点钟位置的图像。 (时钟11点)"""
    CLOCK10: Image
    """指针指向 10 点钟位置的图像。 (时钟10点)"""
    CLOCK9: Image
    """指针指向 9 点钟位置的图像。 (时钟9点)"""
    CLOCK8: Image
    """指针指向 8 点钟位置的图像。 (时钟8点)"""
    CLOCK7: Image
    """指针指向 7 点钟位置的图像。 (时钟7点)"""
    CLOCK6: Image
    """指针指向 6 点钟位置的图像。 (时钟6点)"""
    CLOCK5: Image
    """指针指向 5 点钟位置的图像。 (时钟5点)"""
    CLOCK4: Image
    """指针指向 4 点钟位置的图像。 (时钟4点)"""
    CLOCK3: Image
    """指针指向 3 点钟位置的图像。 (时钟3点)"""
    CLOCK2: Image
    """指针指向 2 点钟位置的图像。 (时钟2点)"""
    CLOCK1: Image
    """指针指向 1 点钟位置的图像。 (时钟1点)"""
    ARROW_N: Image
    """指向北方的箭头的图像。 (箭头（指向北）)"""
    ARROW_NE: Image
    """指向东北方的箭头的图像。 (箭头（指向东北）)"""
    ARROW_E: Image
    """指向东方的箭头的图像。 (箭头（指向东）)"""
    ARROW_SE: Image
    """指向东南方的箭头的图像。 (箭头（指向东南）)"""
    ARROW_S: Image
    """指向南方的箭头图像。 (箭头（指向南）)"""
    ARROW_SW: Image
    """指向西南方的箭头的图像。 (箭头（指向西南）)"""
    ARROW_W: Image
    """指向西方的箭头的图像。 (箭头（指向西）)"""
    ARROW_NW: Image
    """指向西北方的箭头的图像。 (箭头（指向西北）)"""
    TRIANGLE: Image
    """向上的三角形图像。 (三角)"""
    TRIANGLE_LEFT: Image
    """左角的三角形图像。 (左三角)"""
    CHESSBOARD: Image
    """按棋盘式交替点亮 LED。 (国际象棋棋盘)"""
    DIAMOND: Image
    """钻石图像。 (菱形)"""
    DIAMOND_SMALL: Image
    """小钻石图像。 (小的菱形)"""
    SQUARE: Image
    """方形图像。 (正方形)"""
    SQUARE_SMALL: Image
    """小的方形图像。 (小方形)"""
    RABBIT: Image
    """兔子图像。 (兔子)"""
    COW: Image
    """奶牛图像。 (牛)"""
    MUSIC_CROTCHET: Image
    """音乐音符图像 (音乐音符)"""
    MUSIC_QUAVER: Image
    """八分音符图像。 (八分音符)"""
    MUSIC_QUAVERS: Image
    """一对八分音符图像。 (一对八分音符)"""
    PITCHFORK: Image
    """干草叉图像。 (干草叉)"""
    XMAS: Image
    """圣诞树图像。 (圣诞节)"""
    PACMAN: Image
    """吃豆人游戏角色图像。 (吃豆人)"""
    TARGET: Image
    """目标图像 (目标)"""
    TSHIRT: Image
    """T 恤图像。 (T恤)"""
    ROLLERSKATE: Image
    """轮滑图像。 (轮滑)"""
    DUCK: Image
    """鸭子图像。 (鸭子)"""
    HOUSE: Image
    """房子图像。 (房子)"""
    TORTOISE: Image
    """乌龟图像。 (乌龟)"""
    BUTTERFLY: Image
    """蝴蝶图像 (蝴蝶)"""
    STICKFIGURE: Image
    """火柴人图像。 (简笔人物画)"""
    GHOST: Image
    """幽灵图像。 (幽灵)"""
    SWORD: Image
    """利剑图像。 (剑)"""
    GIRAFFE: Image
    """长颈鹿图像。 (长颈鹿)"""
    SKULL: Image
    """骷髅图像。 (骷髅)"""
    UMBRELLA: Image
    """雨伞图像。 (雨伞)"""
    SNAKE: Image
    """蛇图像。 (蛇)"""
    SCISSORS: Image
    """剪刀图像。 (剪刀)"""
    ALL_CLOCKS: List[Image]
    """按顺序包含所有 CLOCK_ 图像的列表（时钟）。 (所有时钟)"""
    ALL_ARROWS: List[Image]
    """按顺序包含所有 ARROW_ 图像的列表（箭头）。 (所有箭头)"""

    @overload
    def __init__(self, string: str) -> None:
        """根据描述点亮 LED 的字符串来创建一幅图像。

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: 描述图像的字符串。"""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """创建一幅具有 ``width`` 列和 ``height`` 行的空白图像。

:param width: (宽度) 可选的图像宽度
:param height: (高度) 可选的图像高度
:param buffer: (缓冲区) 用可选数组或在 0-9 范围内的 ``width`` × ``height`` 整数字节来初始化图像

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """获取列数。 (宽度)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """获取行数。 (高度)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """设置像素亮度。

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: 列号
:param y: 行号
:param value: 用 0（暗）和 9（亮）之间的整数来代表亮度

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """获取一个像素的亮度。

Example: ``my_image.get_pixel(0, 0)``

:param x: 列号
:param y: 行号
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """通过向左移动图片来创建新图像。

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: 要移动的列数
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """通过向右移动图片来创建新图像。

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: 要移动的列数
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """通过向上移动图片来创建新图像。

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: 要移动的行数
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """通过向下移动图片来创建新图像。

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: 要移动的行数
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """通过裁剪图片来创建一幅新图像。 (裁剪)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: 裁剪偏移列
:param y: 裁剪偏移行
:param w: 裁剪宽度
:param h: 裁剪高度
:return: The new image"""
        ...

    def copy(self) -> Image:
        """创建图像的精确副本。 (复制)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """通过反转源图像中像素的亮度来创建一幅新图像。 (反转)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """设置图像中所有像素的亮度。 (填充)

Example: ``my_image.fill(5)``

:param value: 新亮度为 0 (暗) 和 9 (明) 之间的数字。

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """复制另一幅图像的一部分区域到这幅图像。

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (来源) 源图像
:param x: 源图像的起始列偏移量
:param y: 源图像的起始行偏移量
:param w: 要复制的列数
:param h: 要复制的行数
:param xdest: (x偏离量) 此图像中要修改的列偏移量
:param ydest: (y偏离量) 此图像中要修改的行偏移量

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
        """获取图像的缩小字符串表示。 (表示)"""
        ...

    def __str__(self) -> str:
        """获取图像的可读字符串表示。 (字符串)"""
        ...

    def __add__(self, other: Image) -> Image:
        """通过将两幅图像每个像素的亮度值相加来创建一幅新图像。

Example: ``Image.HEART + Image.HAPPY``

:param other: (其他) 要添加的图像。"""
        ...

    def __sub__(self, other: Image) -> Image:
        """通过从此图像中减去另一幅图像的亮度值来创建一幅新图像。 (减去)

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (其他) 要减去的图像。"""
        ...

    def __mul__(self, n: float) -> Image:
        """通过将每个像素的亮度乘以 ``n`` 来创建一幅新图像。 (相乘)

Example: ``Image.HEART * 0.5``

:param n: 要相乘的数值。"""
        ...

    def __truediv__(self, n: float) -> Image:
        """通过将每个像素的亮度除以 ``n`` 来创建一幅新图像。 (除以)

Example: ``Image.HEART / 2``

:param n: 要除以的数值。"""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """表示声音事件从``quiet``到``loud``的过渡，如拍手或者喊叫。 (大声)"""
    QUIET: SoundEvent
    """表示声音事件从``loud``到``quiet``的过渡，如说话或者背景音乐。 (安静)"""

class Sound:
    """可以使用 ``audio.play(Sound.NAME)`` 调用内置声音。 (声音)"""
    GIGGLE: Sound
    """咯咯的声音。 (咯咯笑)"""
    HAPPY: Sound
    """快乐的声音。 (快乐)"""
    HELLO: Sound
    """问候声。 (你好)"""
    MYSTERIOUS: Sound
    """神秘的声音 (神秘的)"""
    SAD: Sound
    """悲伤的声音。 (难过)"""
    SLIDE: Sound
    """滑动声。 (滑动)"""
    SOARING: Sound
    """翱翔的声音。 (高昂)"""
    SPRING: Sound
    """春天的声音。 (弹簧)"""
    TWINKLE: Sound
    """闪烁的声音。 (闪烁)"""
    YAWN: Sound
    """打哈欠的声音。 (打哈欠)"""