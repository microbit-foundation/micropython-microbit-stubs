"""端子、イメージ、サウンド、温度と音量。"""
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
    """time 引数で指定した間隔で関数を実行するようスケジュールします。 **V2** のみで使えます。

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

:param callback: 指定した間隔で呼び出す関数。デコレータとして使う場合は省略してください。
:param days: スケジューリングのための日数を設定します。
:param h: スケジューリングのための時間を設定します。
:param min: スケジューリングのための分を設定します。
:param s: スケジューリングのための秒を設定します。
:param ms: スケジューリングのためのミリ秒を設定します。"""

def panic(n: int) -> None:
    """パニックモードに入ります。

Example: ``panic(127)``

:param n: 状態を示す 255 以下の任意の整数。

Requires restart."""

def reset() -> None:
    """ボードを再起動します。"""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """ある整数区間から別の整数区間に値を変換します。

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: 変換する数値。
:param from_: 変換元の区間を定義するためのタプル。
:param to: 変換先の区間を定義するためのタプル。
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """ある浮動小数点数区間から別の浮動小数点数区間に値を変換します。

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: 変換する数値。
:param from_: 変換元の区間を定義するためのタプル。
:param to: 変換先の区間を定義するためのタプル。
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """``n`` ミリ秒待機します。

Example: ``sleep(1000)``

:param n: ミリ秒単位の待機時間

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """ボードの実行時間を取得します。

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """micro:bitの温度を摂氏で取得します。 (温度)"""

def set_volume(v: int) -> None:
    """音量を設定します。

Example: ``set_volume(127)``

:param v: 0（下限）から 255（上限）までの間の値。

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """ボタン ``button_a`` と ``button_b`` のクラス。"""

    def is_pressed(self) -> bool:
        """ボタンが押されているかどうかを確認します。

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """デバイスが起動されてから、もしくは前回このメソッドが呼び出されてからボタンが押されたかどうかを確認します。

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """ボタンを押した回数の合計を取得し、返す前に回数をゼロにリセットします。

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""左のボタン ``Button`` オブジェクト。"""
button_b: Button
"""右のボタン ``Button`` オブジェクト。"""

class MicroBitDigitalPin:
    """デジタル端子。

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """端子のデジタル値を取得します。

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """端子のデジタル値を設定します。

Example: ``pin0.write_digital(1)``

:param value: 端子をハイにするには 1 、ローにするには 0 を指定"""
        ...

    def set_pull(self, value: int) -> None:
        """プル状態を ``PULL_UP``、``PULL_DOWN``、``NO_PULL`` の３つの値のいずれかに設定します。

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: ``pin0.PULL_UP`` などの関連する端子のプル状態。"""
        ...

    def get_pull(self) -> int:
        """端子のプル状態を取得します。

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """端子のモードを返します。

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """PWM 信号を端子に出力します。時間幅周期は ``value`` に比例します。

Example: ``pin0.write_analog(254)``

:param value: 0（時間幅周期 0%）から 1023（時間幅周期 100%）までの整数または浮動小数点数。"""

    def set_analog_period(self, period: int) -> None:
        """出力されるPWM信号の周期を ``period`` にミリ秒単位で設定します。

Example: ``pin0.set_analog_period(10)``

:param period: 周期をミリ秒単位で指定。有効な最小値は1ms。"""

    def set_analog_period_microseconds(self, period: int) -> None:
        """出力されるPWM信号の周期を ``period`` にマイクロ秒単位で設定します。

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: 周期をマイクロ秒単位で指定。有効な最小値は256µs。"""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """アナログとデジタル機能を備えた端子。"""

    def read_analog(self) -> int:
        """端子にかかっている電圧を読み取ります。

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """アナログ、デジタル、タッチ機能を備えた端子。"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """端子にタッチしているかどうかを確認します。

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
        """端子のタッチモードを設定します。

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: 関連する端子の ``CAPACITIVE`` または ``RESISTIVE``。"""
        ...
pin0: MicroBitTouchPin
"""デジタル、アナログ、タッチ機能を備えた端子。"""
pin1: MicroBitTouchPin
"""デジタル、アナログ、タッチ機能を備えた端子。"""
pin2: MicroBitTouchPin
"""デジタル、アナログ、タッチ機能を備えた端子。"""
pin3: MicroBitAnalogDigitalPin
"""デジタルとアナログ機能を備えた端子。"""
pin4: MicroBitAnalogDigitalPin
"""デジタルとアナログ機能を備えた端子。"""
pin5: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin6: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin7: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin8: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin9: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin10: MicroBitAnalogDigitalPin
"""デジタルとアナログ機能を備えた端子。"""
pin11: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin12: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin13: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin14: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin15: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin16: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin19: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin20: MicroBitDigitalPin
"""デジタル機能を備えた端子。"""
pin_logo: MicroBitTouchPin
"""micro:bitの前面にあるタッチセンサー機能のあるロゴの端子です。デフォルトでは静電容量方式タッチモードになっています。"""
pin_speaker: MicroBitAnalogDigitalPin
"""micro:bitスピーカーをアドレスするための端子。

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """micro:bitのLEDディスプレイに表示するイメージ。

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """「ハート」イメージ。"""
    HEART_SMALL: Image
    """「小さいハート」イメージ。"""
    HAPPY: Image
    """「うれしい顔」イメージ。"""
    SMILE: Image
    """「笑顔」イメージ。"""
    SAD: Image
    """「かなしい顔」イメージ。"""
    CONFUSED: Image
    """「こまり顔」イメージ。"""
    ANGRY: Image
    """「おこり顔」イメージ。"""
    ASLEEP: Image
    """「ねてる顔」イメージ。"""
    SURPRISED: Image
    """「びっくり顔」イメージ。"""
    SILLY: Image
    """「へん顔」イメージ。"""
    FABULOUS: Image
    """「サングラスの笑顔」イメージ。"""
    MEH: Image
    """「ふーん」イメージ"""
    YES: Image
    """「チェック」イメージ。"""
    NO: Image
    """「バツ」イメージ。"""
    CLOCK12: Image
    """「12時を指す線」イメージ。"""
    CLOCK11: Image
    """「11時を指す線」イメージ。"""
    CLOCK10: Image
    """「10時を指す線」イメージ。"""
    CLOCK9: Image
    """「9時を指す線」イメージ。"""
    CLOCK8: Image
    """「8時を指す線」イメージ。"""
    CLOCK7: Image
    """「7時を指す線」イメージ。"""
    CLOCK6: Image
    """「6時を指す線」イメージ。"""
    CLOCK5: Image
    """「5時を指す線」イメージ。"""
    CLOCK4: Image
    """「4時を指す線」イメージ。"""
    CLOCK3: Image
    """「3時を指す線」イメージ。"""
    CLOCK2: Image
    """「2時を指す線」イメージ。"""
    CLOCK1: Image
    """「1時を指す線」イメージ。"""
    ARROW_N: Image
    """「北を指す矢印」イメージ。"""
    ARROW_NE: Image
    """「北東を指す矢印」イメージ。"""
    ARROW_E: Image
    """「西を指す矢印」イメージ。"""
    ARROW_SE: Image
    """「南東を指す矢印」イメージ。"""
    ARROW_S: Image
    """「南を指す矢印」イメージ。"""
    ARROW_SW: Image
    """「南西を指す矢印」イメージ。"""
    ARROW_W: Image
    """「西を指す矢印」イメージ。"""
    ARROW_NW: Image
    """「北西を指す矢印」イメージ。"""
    TRIANGLE: Image
    """「上向きの三角形」イメージ"""
    TRIANGLE_LEFT: Image
    """「左向き三角」イメージ。"""
    CHESSBOARD: Image
    """チェス盤パターンで交互に点灯するLED。"""
    DIAMOND: Image
    """「ダイヤモンド」イメージ。"""
    DIAMOND_SMALL: Image
    """「小さいダイヤモンド」イメージ。"""
    SQUARE: Image
    """「四角」イメージ。"""
    SQUARE_SMALL: Image
    """「小さい四角」イメージ。"""
    RABBIT: Image
    """「うさぎ」イメージ。"""
    COW: Image
    """「うし」イメージ。"""
    MUSIC_CROTCHET: Image
    """「４分音符」イメージ。"""
    MUSIC_QUAVER: Image
    """「８分音符」イメージ。"""
    MUSIC_QUAVERS: Image
    """「連結した８分音符」イメージ。"""
    PITCHFORK: Image
    """「くまで」イメージ。"""
    XMAS: Image
    """「クリスマスツリー」イメージ。"""
    PACMAN: Image
    """「パックマン」イメージ。"""
    TARGET: Image
    """「まと」イメージ。"""
    TSHIRT: Image
    """「Tシャツ」イメージ。"""
    ROLLERSKATE: Image
    """「ローラースケート」イメージ。"""
    DUCK: Image
    """「あひる」イメージ。"""
    HOUSE: Image
    """「家」イメージ。"""
    TORTOISE: Image
    """「かめ」イメージ。"""
    BUTTERFLY: Image
    """「ちょうちょ」イメージ。"""
    STICKFIGURE: Image
    """「棒人間」イメージ。"""
    GHOST: Image
    """「おばけ」イメージ。"""
    SWORD: Image
    """「剣」イメージ。"""
    GIRAFFE: Image
    """「きりん」イメージ。"""
    SKULL: Image
    """「がいこつ」イメージ。"""
    UMBRELLA: Image
    """「かさ」イメージ。"""
    SNAKE: Image
    """「へび」イメージ。"""
    SCISSORS: Image
    """「はさみ」イメージ。"""
    ALL_CLOCKS: List[Image]
    """すべての時計イメージを順番に並べたリスト。"""
    ALL_ARROWS: List[Image]
    """すべての矢印イメージを順番に並べたリスト。"""

    @overload
    def __init__(self, string: str) -> None:
        """LEDの点灯パターンを示す文字列からイメージを作成します。

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: イメージについて記述する文字列。"""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """``width`` 列と ``height`` 行からなる空のイメージを作成します。

:param width: イメージの幅を指定するオプション
:param height: イメージの高さを指定するオプション
:param buffer: イメージを初期化するために、整数値（0～9）を ``width``×``height`` 個並べた配列またはバイト列を指定します

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """列数を取得します。

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """行数を取得します。

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """1ピクセルの明るさを設定します。

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: 列数
:param y: 行数
:param value: 明るさを 0（暗い）から 9（明るい）までの整数値で指定します

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """1ピクセルの明るさを取得します。

Example: ``my_image.get_pixel(0, 0)``

:param x: 列数
:param y: 行数
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """画像を左にシフトした新しいイメージを作成します。

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: シフトする列数
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """画像を右にシフトした新しいイメージを作成します。

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: シフトする列数
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """画像を上にシフトした新しいイメージを作成します。

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: シフトする行数
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """画像を下にシフトした新しいイメージを作成します。

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: シフトする行数
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """画像をトリミングした新しいイメージを作成します。

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: トリミングするオフセット列
:param y: トリミングするオフセット行
:param w: トリミングする幅
:param h: トリミングする高さ
:return: The new image"""
        ...

    def copy(self) -> Image:
        """イメージ全体のコピーを作成します。

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """元イメージのピクセルの明るさを反転した新しいイメージ作成します。

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """イメージのすべてのピクセルの明るさを設定します。

Example: ``my_image.fill(5)``

:param value: 0（暗い）から 9（明るい）までの数値で新しい明るさを指定します。

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """このイメージに別のイメージから領域をコピーします。

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: 元イメージ
:param x: 元イメージの開始列オフセット
:param y: 元イメージの開始行オフセット
:param w: コピーする列数
:param h: コピーする行数
:param xdest: このイメージで変更する列オフセット
:param ydest: このイメージで変更する行オフセット

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
        """イメージのコンパクトな文字列表現を取得します。"""
        ...

    def __str__(self) -> str:
        """イメージの判読可能な文字列表現を取得します。"""
        ...

    def __add__(self, other: Image) -> Image:
        """２つのイメージの各ピクセルの明るさを足した新しいイメージを作成します。

Example: ``Image.HEART + Image.HAPPY``

:param other: 加算するイメージ。"""
        ...

    def __sub__(self, other: Image) -> Image:
        """このイメージから他のイメージの明るさの値を引いた新しいイメージを作成します。

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: 減算するイメージ。"""
        ...

    def __mul__(self, n: float) -> Image:
        """各ピクセルの明るさを ``n`` 倍した新しいイメージを作成します。

Example: ``Image.HEART * 0.5``

:param n: 乗算する値。"""
        ...

    def __truediv__(self, n: float) -> Image:
        """各ピクセルの明るさを ``n`` で割った新しいイメージを作成します。

Example: ``Image.HEART / 2``

:param n: 除算する値。"""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """拍手や叫び声などで ``quiet`` から ``loud`` へのサウンドイベントの変化を表します。"""
    QUIET: SoundEvent
    """発話やBGMなどで ``loud`` から ``quiet`` へのサウンドイベントの変化を表します。"""

class Sound:
    """内蔵のサウンドは ``audio.play(Sound.NAME)`` で呼び出すことができます。"""
    GIGGLE: Sound
    """「くすくす笑う」サウンド。"""
    HAPPY: Sound
    """「ハッピー」サウンド。"""
    HELLO: Sound
    """「ハロー」サウンド"""
    MYSTERIOUS: Sound
    """「ミステリアス」サウンド。"""
    SAD: Sound
    """「悲しい」サウンド。"""
    SLIDE: Sound
    """「するする動く」サウンド。"""
    SOARING: Sound
    """「舞い上がる」サウンド。"""
    SPRING: Sound
    """「バネ」サウンド。"""
    TWINKLE: Sound
    """「キラキラ」サウンド。"""
    YAWN: Sound
    """「あくび」サウンド。"""