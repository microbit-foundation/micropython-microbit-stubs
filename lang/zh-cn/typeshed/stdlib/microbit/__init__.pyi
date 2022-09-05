"""引脚、图像、声音、温度和音量。 (microbit)"""
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
    """安排按给定的时间间隔调用一个函数**仅限 V2**。 (run every)

Example: ``run_every(my_logging, min=5)``

This function can be passed a callback::

    run_every(your_function, h=1, min=20, s=30, ms=50)

or used as a decorator::

    @run_every(h=1, min=20, s=30, ms=50)
    def your_function():
        pass

Arguments with different time units are additive.

:param callback: (callback) 要调用的回调。当用作装饰器时省略。
:param days: (days) 以天为单位的间隔。
:param h: (h) 以小时为单位的间隔。
:param min: (min) 以分钟为单位的间隔。
:param s: (s) 以秒为单位的间隔。
:param ms: (ms) 以毫秒为单位的间隔。"""

def panic(n: int) -> None:
    """进入panic 模式（恐慌）。 (panic)

Example: ``panic(127)``

:param n: (n) 一个 <= 255的任意整数，以表示一个状态。

Requires restart."""

def reset() -> None:
    """重启主板。 (reset)"""

def sleep(n: float) -> None:
    """等待 ``n`` 毫秒。 (sleep)

Example: ``sleep(1000)``

:param n: (n) 要等待的毫秒数

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """获取主板的运行时间。 (running time)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """以摄氏度为单位获取 micro:bit 的温度。 (temperature)"""

def set_volume(v: int) -> None:
    """设置音量。 (set volume)

Example: ``set_volume(127)``

:param v: (v) 一个介于 0 (低) 和 255 (高) 之间的值。

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """按键 ``button_a`` 和 ``button_b`` 的类。 (button)"""

    def is_pressed(self) -> bool:
        """检查按键是否被按下。 (is pressed)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """检查按键自设备启动以来或者上次调用此方法之后是否被按下。 (was pressed)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """获得按键按下的总计次数，并在返回之前将该总计次数重置为0。 (get presses)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""左键 ``Button`` 对象。 (button a)"""
button_b: Button
"""右键 ``Button`` 对象。 (button b)"""

class MicroBitDigitalPin:
    """数字引脚。 (microbitdigitalpin)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """获取引脚的数字值。 (read digital)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """设置引脚的数字值。 (write digital)

Example: ``pin0.write_digital(1)``

:param value: (value) 1 将引脚设置为高电平，或 0 将引脚设置为低电平"""
        ...

    def set_pull(self, value: int) -> None:
        """将拉取状态设置为以下三个可能的值之一：``PULL_UP``、``PULL_DOWN``或N``NO_PULL``。 (set pull)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (value) 相关引脚的拉取状态，例如： ``pin0.PULL_UP``。"""
        ...

    def get_pull(self) -> int:
        """获取引脚上的拉取状态。 (get pull)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """返回引脚模式。 (get mode)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """在引脚上输出 PWM 信号，占空比为``value``。 (write analog)

Example: ``pin0.write_analog(254)``

:param value: (value) 介于 0（0% 占空比）和 1023（100% 占空比）之间的整数或浮点数。"""

    def set_analog_period(self, period: int) -> None:
        """将输出的 PWM 信号的周期设置为 ``period``（单位：毫秒）。 (set analog period)

Example: ``pin0.set_analog_period(10)``

:param period: (period) 以毫秒为单位的周期，最小有效值为 1 毫秒。"""

    def set_analog_period_microseconds(self, period: int) -> None:
        """将输出的 PWM 信号的周期设置为 ``period``（单位：微秒）。 (set analog period microseconds)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (period) 以微秒为单位的周期，最小有效值为 256 毫秒。"""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """带有模拟和数字功能的引脚。 (microbitanalogdigitalpin)"""

    def read_analog(self) -> int:
        """读取应用于引脚的电压。 (read analog)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """带有模拟、数字和触摸功能的引脚。 (microbittouchpin)"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """检查引脚是否被触摸。 (is touched)

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
        """设置引脚的触摸模式。 (set touch mode)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (value)  来自相关引脚的``CAPACITIVE`` 或 ``RESISTIVE``。"""
        ...
pin0: MicroBitTouchPin
"""具有数字、模拟和触摸功能的引脚。 (pin0)"""
pin1: MicroBitTouchPin
"""具有数字、模拟和触摸功能的引脚。 (pin1)"""
pin2: MicroBitTouchPin
"""具有数字、模拟和触摸功能的引脚。 (pin2)"""
pin3: MicroBitAnalogDigitalPin
"""具有数字和模拟功能的引脚。 (pin3)"""
pin4: MicroBitAnalogDigitalPin
"""具有数字和模拟功能的引脚。 (pin4)"""
pin5: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin5)"""
pin6: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin6)"""
pin7: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin7)"""
pin8: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin8)"""
pin9: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin9)"""
pin10: MicroBitAnalogDigitalPin
"""具有数字和模拟功能的引脚。 (pin10)"""
pin11: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin11)"""
pin12: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin12)"""
pin13: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin13)"""
pin14: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin14)"""
pin15: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin15)"""
pin16: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin16)"""
pin19: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin19)"""
pin20: MicroBitDigitalPin
"""具有数字功能的引脚。 (pin20)"""
pin_logo: MicroBitTouchPin
"""micro:bit 正面的触摸感应徽标引脚，默认设置为电容触摸模式。 (pin logo)"""
pin_speaker: MicroBitAnalogDigitalPin
"""用于对 micro:bit 扬声器寻址的引脚。 (pin speaker)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """在micro:bit LED显示屏上显示的图像。 (image)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """心形图像 (heart)"""
    HEART_SMALL: Image
    """小的心形图像。 (heart small)"""
    HAPPY: Image
    """快乐的脸部图像。 (happy)"""
    SMILE: Image
    """微笑的脸部图像。 (smile)"""
    SAD: Image
    """难过的脸部图像。 (sad)"""
    CONFUSED: Image
    """困惑的面部图像。 (confused)"""
    ANGRY: Image
    """愤怒的脸部图像。 (angry)"""
    ASLEEP: Image
    """睡着的脸部图像。 (asleep)"""
    SURPRISED: Image
    """惊讶的脸部图像。 (surprised)"""
    SILLY: Image
    """傻傻的脸部图像。 (silly)"""
    FABULOUS: Image
    """戴墨镜的脸部图像。 (fabulous)"""
    MEH: Image
    """印象平平的脸部图像 (meh)"""
    YES: Image
    """对勾图像。 (yes)"""
    NO: Image
    """打叉图像。 (no)"""
    CLOCK12: Image
    """指针指向12点钟位置的图像。 (clock12)"""
    CLOCK11: Image
    """指针指向11点钟位置的图像。 (clock11)"""
    CLOCK10: Image
    """指针指向10点钟位置的图像。 (clock10)"""
    CLOCK9: Image
    """指针指向9点钟位置的图像。 (clock9)"""
    CLOCK8: Image
    """指针指向8点钟位置的图像。 (clock8)"""
    CLOCK7: Image
    """指针指向7点钟位置的图像。 (clock7)"""
    CLOCK6: Image
    """指针指向6点钟位置的图像。 (clock6)"""
    CLOCK5: Image
    """指针指向5点钟位置的图像。 (clock5)"""
    CLOCK4: Image
    """指针指向4点钟位置的图像。 (clock4)"""
    CLOCK3: Image
    """指针指向3点钟位置的图像。 (clock3)"""
    CLOCK2: Image
    """指针指向2点钟位置的图像。 (clock2)"""
    CLOCK1: Image
    """指针指向1点钟位置的图像。 (clock1)"""
    ARROW_N: Image
    """指向北方的箭头的图像。 (arrow n)"""
    ARROW_NE: Image
    """指向东北方的箭头的图像。 (arrow ne)"""
    ARROW_E: Image
    """指向东方的箭头的图像。 (arrow e)"""
    ARROW_SE: Image
    """指向东南方的箭头的图像。 (arrow se)"""
    ARROW_S: Image
    """指向南方的箭头图像。 (arrow s)"""
    ARROW_SW: Image
    """指向西南方的箭头的图像。 (arrow sw)"""
    ARROW_W: Image
    """指向西方的箭头的图像。 (arrow w)"""
    ARROW_NW: Image
    """指向西北方的箭头的图像。 (arrow nw)"""
    TRIANGLE: Image
    """向上的三角形图像。 (triangle)"""
    TRIANGLE_LEFT: Image
    """左角的三角形图像。 (
triangle left)"""
    CHESSBOARD: Image
    """按棋盘式交替点亮 LED。 (chessboard)"""
    DIAMOND: Image
    """钻石图像。 (diamond)"""
    DIAMOND_SMALL: Image
    """小钻石图像。 (diamond small)"""
    SQUARE: Image
    """方形图像。 (square)"""
    SQUARE_SMALL: Image
    """小的方形图像。 (square small)"""
    RABBIT: Image
    """兔子图像。 (rabbit)"""
    COW: Image
    """奶牛图像。 (cow)"""
    MUSIC_CROTCHET: Image
    """音乐音符图像 (music crotchet)"""
    MUSIC_QUAVER: Image
    """八分音符图像。 (music quaver)"""
    MUSIC_QUAVERS: Image
    """一对八分音符图像。 (music quavers)"""
    PITCHFORK: Image
    """干草叉图像。 (pitchfork)"""
    XMAS: Image
    """圣诞树图像。 (xmas)"""
    PACMAN: Image
    """吃豆人游戏角色图像。 (pacman)"""
    TARGET: Image
    """目标图像 (target)"""
    TSHIRT: Image
    """T 恤图像。 (tshirt)"""
    ROLLERSKATE: Image
    """轮滑图像。 (rollerskate)"""
    DUCK: Image
    """鸭子图像。 (duck)"""
    HOUSE: Image
    """房子图像。 (house)"""
    TORTOISE: Image
    """乌龟图像。 (tortoise)"""
    BUTTERFLY: Image
    """蝴蝶图像 (butterfly)"""
    STICKFIGURE: Image
    """
火柴人图像。 (stickfigure)"""
    GHOST: Image
    """幽灵图像。 (ghost)"""
    SWORD: Image
    """利剑图像。 (sword)"""
    GIRAFFE: Image
    """长颈鹿图像。 (giraffe)"""
    SKULL: Image
    """骷髅图像。 (skull)"""
    UMBRELLA: Image
    """雨伞图像。 (umbrella)"""
    SNAKE: Image
    """蛇图像。 (snake)"""
    ALL_CLOCKS: List[Image]
    """按顺序包含所有 CLOCK_ 图像的列表（时钟）。 (all clocks)"""
    ALL_ARROWS: List[Image]
    """按顺序包含所有 ARROW_ 图像的列表（箭头）。 (all arrows)"""

    @overload
    def __init__(self, string: str) -> None:
        """根据描述点亮 LED 的字符串来创建一幅图像。 (init)

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (string) 描述图像的字符串。"""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """创建一幅具有 ``width`` 列和 ``height`` 行的空白图像。 (init)

:param width: (width) 可选的图像宽度
:param height: (height) 可选的图像高度
:param buffer: (buffer) 用可选数组或在 0-9 范围内的``width``×``height`` 整数字节来初始化图像

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """获取列数。 (width)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """获取行数。 (height)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """设置像素亮度。 (set pixel)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: (x) 列号
:param y: (y) 行号
:param value: (value) 用 0（暗）和 9（亮）之间的整数来代表亮度

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """获取一个像素的亮度。 (get pixel)

Example: ``my_image.get_pixel(0, 0)``

:param x: (x) 列号
:param y: (y) 行号
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """通过向左移动图片来创建新图像。 (shift left)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: (n) 要移动的列数
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """通过向右移动图片来创建新图像。 (shift right)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: (n) 要移动的列数
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """通过向上移动图片来创建新图像。 (shift up)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: (n) 要移动的行数
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """通过向下移动图片来创建新图像。 (shift down)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: (n) 要移动的行数
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """通过裁剪图片来创建一幅新图像。 (crop)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: (x) 裁剪偏移列
:param y: (y) 裁剪偏移行
:param w: (w) 裁剪宽度
:param h: (h) 裁剪高度
:return: The new image"""
        ...

    def copy(self) -> Image:
        """创建图像的精确副本。 (copy)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """通过反转源图像中像素的亮度来创建一幅新图像。 (invert)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """设置图像中所有像素的亮度。 (fill)

Example: ``my_image.fill(5)``

:param value: (value) 新亮度为 0 (暗) 和 9 (明) 之间的数字。

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """复制另一幅图像的一部分区域到这幅图像。 (blit)

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (src) 源图像
:param x: (x) 源图像的起始列偏移量
:param y: (y) 源图像的起始行偏移量
:param w: (w) 要复制的列数
:param h: (h) 要复制的行数
:param xdest: (xdest) 此图像中要修改的列偏移量
:param ydest: (ydest) 此图像中要修改的行偏移量

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
        """获取图像的缩小字符串表示。 (repr)"""
        ...

    def __str__(self) -> str:
        """获取图像的可读字符串表示。 (str)"""
        ...

    def __add__(self, other: Image) -> Image:
        """通过将两幅图像每个像素的亮度值相加来创建一幅新图像。 (add)

Example: ``Image.HEART + Image.HAPPY``

:param other: (other) 要添加的图像。"""
        ...

    def __sub__(self, other: Image) -> Image:
        """通过从此图像中减去另一幅图像的亮度值来创建一幅新图像。 (sub)

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (other) 要减去的图像。"""
        ...

    def __mul__(self, n: float) -> Image:
        """通过将每个像素的亮度乘以``n`` 来创建一幅新图像。 (mul)

Example: ``Image.HEART * 0.5``

:param n: (n) 要相乘的数值。"""
        ...

    def __truediv__(self, n: float) -> Image:
        """通过将每个像素的亮度除以``n`` 来创建一幅新图像。 (truediv)

Example: ``Image.HEART / 2``

:param n: (n) 要除以的数值。"""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """表示声音事件从``quiet``到``loud``的过渡，如拍手或者喊叫。 (loud)"""
    QUIET: SoundEvent
    """表示声音事件从``loud``到``quiet``的过渡，如说话或者背景音乐。 (quiet)"""

class Sound:
    """可以使用 ``audio.play(Sound.NAME)`` 调用内置声音。 (sound)"""
    GIGGLE: Sound
    """咯咯的声音。 (giggle)"""
    HAPPY: Sound
    """快乐的声音。 (happy)"""
    HELLO: Sound
    """问候声。 (hello)"""
    MYSTERIOUS: Sound
    """神秘的声音 (mysterious)"""
    SAD: Sound
    """
悲伤的声音。 (sad)"""
    SLIDE: Sound
    """滑动声。 (slide)"""
    SOARING: Sound
    """翱翔的声音。 (soaring)"""
    SPRING: Sound
    """春天的声音。 (spring)"""
    TWINKLE: Sound
    """闪烁的声音。 (twinkle)"""
    YAWN: Sound
    """打哈欠的声音。 (yawn)"""