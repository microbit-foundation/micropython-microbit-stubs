"""핀, 이미지, 소리, 온도 및 음량입니다. (microbit)"""
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
    """주어진 주기에 따라 함수 호출 일정을 설정합니다 **V2 전용**. (run every)

Example: ``run_every(my_logging, min=5)``

This function can be passed a callback::

    run_every(your_function, h=1, min=20, s=30, ms=50)

or used as a decorator::

    @run_every(h=1, min=20, s=30, ms=50)
    def your_function():
        pass

Arguments with different time units are additive.

:param callback: (callback) 인보크(원격 실행) 기능을 호출합니다. 데코레이터(장식자)로 사용할 때는 생략합니다.
:param days: (days) 일 단위 주기입니다.
:param h: (h) 시간 단위 주기입니다.
:param min: (min) 분 단위 주기입니다.
:param s: (s) 초 주기입니다.
:param ms: (ms) 밀리초 주기입니다."""

def panic(n: int) -> None:
    """패닉 모드를 활성화합니다. (panic)

Example: ``panic(127)``

:param n: (n) <= 255의 임의 정수로 상태를 표시합니다.

Requires restart."""

def reset() -> None:
    """보드를 재시작합니다. (reset)"""

def sleep(n: float) -> None:
    """``n``밀리초 동안 대기합니다. (sleep)

Example: ``sleep(1000)``

:param n: (n) 대기할 밀리초 수

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """보드의 실행 시간을 불러옵니다. (running time)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """섭씨로 micro:bit의 온도를 불러옵니다. (온도)"""

def set_volume(v: int) -> None:
    """음량을 설정합니다. (set volume)

Example: ``set_volume(127)``

:param v: (v) 0(낮음) 및 255(높음) 사이의 값입니다.

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """``button_a`` 및 ``button_b`` 버튼의 클래스입니다. (button)"""

    def is_pressed(self) -> bool:
        """해당 버튼이 눌렸는지 확인합니다. (is pressed)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """장치가 시작한 후 또는 이 메서드가 호출된 후 해당 버튼이 눌렸는지 확인합니다. (was pressed)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """버튼이 눌린 총 횟수를 불러오고, 총값을 반환하기 전 초기화합니다. (get presses)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""좌측 버튼 ``Button`` 개체입니다. (button a)"""
button_b: Button
"""우측 버튼 ``Button`` 개체입니다. (button b)"""

class MicroBitDigitalPin:
    """디지털 핀입니다. (microbitdigitalpin)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """핀의 디지털 값을 불러옵니다. (read digital)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """핀의 디지털 값을 설정합니다. (write digital)

Example: ``pin0.write_digital(1)``

:param value: (value) 핀을 하이로 설정하려면 1, 로우로 설정하려면 0"""
        ...

    def set_pull(self, value: int) -> None:
        """다음 중 하나의 값으로 풀 상태를 설정: ``PULL_UP``, ``PULL_DOWN`` 또는 ``NO_PULL`` (set pull)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (value) 관련 핀의 풀 상태입니다. (예: ``pin0.PULL_UP``)"""
        ...

    def get_pull(self) -> int:
        """핀의 풀 상태를 불러옵니다. (get pull)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """핀 모드를 반환합니다. (get mode)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """핀의 PWM 신호를 출력하고 ``value``와(과) 비례하게 듀티 사이클을 설정합니다. (write analog)

Example: ``pin0.write_analog(254)``

:param value: (value) 0(0% 듀티 사이클) 및 1023(100% 듀티) 사이의 정수 또는 부동 소수점 수입니다."""

    def set_analog_period(self, period: int) -> None:
        """PWM 신호가 출력되는 주기를 ``period``밀리초로 설정합니다. (set analog period)

Example: ``pin0.set_analog_period(10)``

:param period: (period) 유효한 최소값이 1ms인 밀리초 주기입니다."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """PWM 신호가 출력되는 주기를 ``period``마이크로초로 설정합니다. (set analog period microseconds)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (period) 유효한 최소값이 256µs인 마이크로초 주기입니다."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """아날로그 및 디지털 기능이 있는 핀입니다. (microbitanalogdigitalpin)"""

    def read_analog(self) -> int:
        """핀에 적용된 전압을 읽습니다. (read analog)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """아날로그, 디지털, 터치 기능이 있는 핀입니다. (microbittouchpin)"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """핀이 접촉 상태인지 확인합니다. (is touched)

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
        """핀의 터치 모드를 설정합니다. (set touch mode)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (value) 관련 핀의 ``CAPACITIVE`` 또는 ``RESISTIVE``입니다."""
        ...
pin0: MicroBitTouchPin
"""디지털 및 아날로그, 터치 기능이 있는 핀입니다. (pin0)"""
pin1: MicroBitTouchPin
"""디지털 및 아날로그, 터치 기능이 있는 핀입니다. (pin1)"""
pin2: MicroBitTouchPin
"""디지털 및 아날로그, 터치 기능이 있는 핀입니다. (pin2)"""
pin3: MicroBitAnalogDigitalPin
"""디지털 및 아날로그 기능이 있는 핀입니다. (pin3)"""
pin4: MicroBitAnalogDigitalPin
"""디지털 및 아날로그 기능이 있는 핀입니다. (pin4)"""
pin5: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin speaker)"""
pin6: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin6)"""
pin7: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin7)"""
pin8: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin8)"""
pin9: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin9)"""
pin10: MicroBitAnalogDigitalPin
"""디지털 및 아날로그 기능이 있는 핀입니다. (pin10)"""
pin11: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin11)"""
pin12: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin12)"""
pin13: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin13)"""
pin14: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin14)"""
pin15: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin15)"""
pin16: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin16)"""
pin19: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin19)"""
pin20: MicroBitDigitalPin
"""디지털 기능이 있는 핀입니다. (pin20)"""
pin_logo: MicroBitTouchPin
"""micro:bit 전면의 터치 감지 로고 핀으로, 기본값은 정전식 터치 모드입니다. (핀 로고)"""
pin_speaker: MicroBitAnalogDigitalPin
"""micro:bit 스피커를 처리하는 핀입니다. (핀 스피커)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """micro:bit LED 디스플레이에 표시할 이미지입니다. (image)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """하트 이미지입니다. (heart)"""
    HEART_SMALL: Image
    """작은 하트 이미지입니다. (heart small)"""
    HAPPY: Image
    """행복한 얼굴 이미지입니다. (happy)"""
    SMILE: Image
    """미소 짓는 얼굴 이미지입니다. (smile)"""
    SAD: Image
    """슬픈 얼굴 이미지입니다. (sad)"""
    CONFUSED: Image
    """혼란스러운 얼굴 이미지입니다. (confused)"""
    ANGRY: Image
    """화난 얼굴 이미지입니다. (angry)"""
    ASLEEP: Image
    """자는 얼굴 이미지. (asleep)"""
    SURPRISED: Image
    """놀란 얼굴 이미지. (surprised)"""
    SILLY: Image
    """우스꽝스러운 얼굴 이미지. (silly)"""
    FABULOUS: Image
    """선글라스 얼굴 이미지. (fabulous)"""
    MEH: Image
    """지루한 얼굴 이미지. (meh)"""
    YES: Image
    """Tick 이미지. (yes)"""
    NO: Image
    """크로스 이미지. (no)"""
    CLOCK12: Image
    """12시 정각을 가리키는 이미지. (clock12)"""
    CLOCK11: Image
    """11시 정각을 가리키는 이미지. (clock11)"""
    CLOCK10: Image
    """10시 정각을 가리키는 이미지. (clock10)"""
    CLOCK9: Image
    """9시 정각을 가리키는 이미지. (clock9)"""
    CLOCK8: Image
    """8시 정각을 가리키는 이미지. (clock8)"""
    CLOCK7: Image
    """7시 정각을 가리키는 이미지. (clock7)"""
    CLOCK6: Image
    """6시 정각을 가리키는 이미지. (clock6)"""
    CLOCK5: Image
    """5시 정각을 가리키는 이미지. (clock5)"""
    CLOCK4: Image
    """4시 정각을 가리키는 이미지. (clock4)"""
    CLOCK3: Image
    """3시 정각을 가리키는 이미지. (clock3)"""
    CLOCK2: Image
    """2시 정각을 가리키는 이미지. (clock2)"""
    CLOCK1: Image
    """1시 정각을 가리키는 이미지. (clock1)"""
    ARROW_N: Image
    """북쪽을 가리키는 화살표 이미지. (arrow n)"""
    ARROW_NE: Image
    """북동쪽을 가리키는 화살표 이미지. (arrow ne)"""
    ARROW_E: Image
    """동쪽을 가리키는 화살표 이미지. (arrow e)"""
    ARROW_SE: Image
    """남동쪽을 가리키는 화살표 이미지. (arrow se)"""
    ARROW_S: Image
    """남쪽을 가리키는 화살표 이미지. (arrow s)"""
    ARROW_SW: Image
    """남서쪽을 가리키는 화살표 이미지. (arrow sw)"""
    ARROW_W: Image
    """서쪽을 가리키는 화살표 이미지. (arrow w)"""
    ARROW_NW: Image
    """북서쪽을 가리키는 화살표 이미지. (arrow nw)"""
    TRIANGLE: Image
    """위쪽을 가리키는 삼각형 이미지. (triangle)"""
    TRIANGLE_LEFT: Image
    """왼쪽을 가리키는 삼각형 이미지. (triangle left)"""
    CHESSBOARD: Image
    """체스판 패턴으로 비치는 여러 LED. (chessboard)"""
    DIAMOND: Image
    """다이아몬드 이미지. (diamond)"""
    DIAMOND_SMALL: Image
    """작은 다이아몬드 이미지. (diamond small)"""
    SQUARE: Image
    """사각형 이미지. (square)"""
    SQUARE_SMALL: Image
    """작은 사각형 이미지. (square small)"""
    RABBIT: Image
    """토끼 이미지. (rabbit)"""
    COW: Image
    """소 이미지. (cow)"""
    MUSIC_CROTCHET: Image
    """사분음표 이미지. (music crotchet)"""
    MUSIC_QUAVER: Image
    """Quaver note image. (music quaver)"""
    MUSIC_QUAVERS: Image
    """Pair of quavers note image. (music quavers)"""
    PITCHFORK: Image
    """쇠스랑 이미지. (pitchfork)"""
    XMAS: Image
    """크리스마스 나무 이미지. (xmas)"""
    PACMAN: Image
    """Pac-Man 아케이드 캐릭터 이미지. (pacman)"""
    TARGET: Image
    """표적 이미지. (target)"""
    TSHIRT: Image
    """티셔츠 이미지. (tshirt)"""
    ROLLERSKATE: Image
    """롤러스케이트 이미지. (rollerskate)"""
    DUCK: Image
    """오리 이미지. (duck)"""
    HOUSE: Image
    """집 이미지. (house)"""
    TORTOISE: Image
    """거북 이미지. (tortoise)"""
    BUTTERFLY: Image
    """나비 이미지. (butterfly)"""
    STICKFIGURE: Image
    """스틱 피규어 이미지. (stickfigure)"""
    GHOST: Image
    """유령 이미지. (ghost)"""
    SWORD: Image
    """칼 이미지. (sword)"""
    GIRAFFE: Image
    """기린 이미지. (giraffe)"""
    SKULL: Image
    """해골 이미지. (skull)"""
    UMBRELLA: Image
    """우산 이미지. (umbrella)"""
    SNAKE: Image
    """뱀 이미지 (snake)"""
    ALL_CLOCKS: List[Image]
    """모든 CLOCK_ 이미지를 순서대로 나열한 목록. (all clocks)"""
    ALL_ARROWS: List[Image]
    """모든 ARROW_ 이미지를 순서대로 나열한 목록. (all arrows)"""

    @overload
    def __init__(self, string: str) -> None:
        """어떤 LED가 켜져있는지 설명하는 문자열로부터 이미지를 생성합니다. (string)

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (string) 이미지를 설명하는 문자열."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """``width`` 열과 ``height`` 행의 비어있는 이미지를 생성합니다. (init)

:param width: (width) 선택 사항으로 이미지의 너비 설정
:param height: (height) 선택 사항으로 이미지의 높이 설정
:param buffer: (buffer) 선택 사항으로, 0-9 범위 정수로 된 ``width``x``height``의 어레이 또는 바이트로 이미지 초기 내용 설정

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """열의 수를 불러옵니다. (width)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """행의 수를 불러옵니다. (height)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """픽셀의 밝기를 설정합니다. (set pixel)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: (x) 열의 번호
:param y: (y) 행의 번호
:param value: (value) 0(어두움)과 9(밝음) 사이의 정수로 밝기를 설정합니다.

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """픽셀의 밝기를 불러옵니다. (get pixel)

Example: ``my_image.get_pixel(0, 0)``

:param x: (x) 열의 번호
:param y: (y) 행의 번호
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """사진을 왼쪽으로 옮겨 새로운 이미지를 생성합니다. (shift left)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: (n) 옮길 열의 수
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """옮길 열의 수 (shift right)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: (n) 옮길 열의 수
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """사진을 위쪽으로 옮겨 새로운 이미지를 생성합니다. (shift up)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: (n) 옮길 행의 수
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """사진을 아래쪽으로 옮겨 새로운 이미지를 생성합니다. (shift down)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: (n) 옮길 행의 수
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """사진을 크롭하고 새로운 이미지를 생성합니다. (crop)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: (x) 크롭 오프셋 열
:param y: (y) 크롭 오프셋 행
:param w: (w) 크롭 너비
:param h: (h) 크롭 높이
:return: The new image"""
        ...

    def copy(self) -> Image:
        """이미지와 정확히 같은 사본을 생성합니다. (copy)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """소스 이미지에 있는 픽셀을 밝기를 반전하여 새로운 이미지를 생성합니다. (invert)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """이미지의 모든 픽셀의 밝기를 설정합니다. (fill)

Example: ``my_image.fill(5)``

:param value: (value) 새로운 밝기를 0(어두움)과 9(밝기) 사이로 설정.

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """다른 이미지로부터 영역을 복사해 이 이미지로 가져옵니다. (blit)

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (src) 소스 이미지
:param x: (x) 소스 이미지 내 시작하는 열의 오프셋
:param y: (y) 소스 이미지 내 시작하는 행의 오프셋
:param w: (w) 복사할 열의 수
:param h: (h) 복사할 행의 번호
:param xdest: (xdest) 이 이미지에서 변형할 열의 오프셋
:param ydest: (ydest) 이 이미지에서 변형할 행의 오프셋

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
        """이미지에 해당하는 컴팩트 스트링(간소화된 문자열)을 불러옵니다. (repr)"""
        ...

    def __str__(self) -> str:
        """이미지에 해당하는 가독 문자열을 불러옵니다. (str)"""
        ...

    def __add__(self, other: Image) -> Image:
        """두 이미지의 각 픽셀의 밝기 값을 더해 새로운 이미지를 생성합니다. (add)

Example: ``Image.HEART + Image.HAPPY``

:param other: (other) 더할 이미지."""
        ...

    def __sub__(self, other: Image) -> Image:
        """두 이미지의 각 픽셀의 밝기 값을 빼 새로운 이미지를 생성합니다. (sub)

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (other) 뺄 이미지"""
        ...

    def __mul__(self, n: float) -> Image:
        """각 픽셀의 밝기 값을 ``n``만큼 곱해 새로운 이미지를 생성합니다. (mul)

Example: ``Image.HEART * 0.5``

:param n: (n) 배율의 값."""
        ...

    def __truediv__(self, n: float) -> Image:
        """각 픽셀의 밝기 값을 ``n``만큼 나누어 새로운 이미지를 생성합니다. (truediv)

Example: ``Image.HEART / 2``

:param n: (n) 나눌 값."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """``quiet``에서 박수 또는 함성 등 ``loud``로 소리 이벤트의 변화를 나타냅니다. (loud)"""
    QUIET: SoundEvent
    """``loud``에서 말소리 또는 배경 음악 등 ``quiet``으로 소리 이벤트의 변화를 나타냅니다. (quiet)"""

class Sound:
    """``audio.play(Sound.NAME)``을 사용해 내장된 소리를 호출합니다. (sound)"""
    GIGGLE: Sound
    """웃는 소리. (giggle)"""
    HAPPY: Sound
    """행복해하는 소리. (happy)"""
    HELLO: Sound
    """인사 소리. (hello)"""
    MYSTERIOUS: Sound
    """수상한 소리. (mysterious)"""
    SAD: Sound
    """슬퍼하는 소리. (sad)"""
    SLIDE: Sound
    """슬라이드 소리. (slide)"""
    SOARING: Sound
    """솟아오르는 소리. (soaring)"""
    SPRING: Sound
    """스프링 소리. (spring)"""
    TWINKLE: Sound
    """반짝이는 소리. (twinkle)"""
    YAWN: Sound
    """하품 소리. (yawn)"""