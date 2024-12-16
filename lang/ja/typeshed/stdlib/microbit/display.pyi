"""5×5 LED ディスプレイ上にテキスト、イメージ、アニメーションを表示します。"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """``x`` 列 ``y`` 行の LEDの明るさを取得します。

Example: ``display.get_pixel(0, 0)``

:param x: ディスプレイの列 (0..4)
:param y: ディスプレイの行 (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """``x`` 列 ``y`` 行の LEDの明るさを設定します。

Example: ``display.set_pixel(0, 0, 9)``

:param x: ディスプレイの列 (0..4)
:param y: ディスプレイの行 (0..4)
:param value: 0（オフ）から 9（明るい）までの明るさ"""
    ...

def clear() -> None:
    """すべての LED の明るさを 0（オフ）に設定します。

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """イメージ、文字、数字をLEDディスプレイに表示します。

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: 表示する文字列、数値、イメージ、イメージのリスト。
:param delay: それぞれの文字、数字、イメージは ``delay`` ミリ秒間隔で表示されます。
:param wait: ``wait`` が ``True`` である場合、アニメーションが終了するまで関数がブロックし、 そうでない場合にはバックグラウンドで実行されます。
:param loop: ``loop`` が ``True`` である場合、アニメーションを永遠に繰り返します。
:param clear: ``clear`` が ``True`` である場合、シーケンスの終了後にディスプレイをクリアします。

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """LEDディスプレィ上に数値やテキストをスクロール表示します。

Example: ``display.scroll('micro:bit')``

:param text: スクロールする文字列。``text`` が整数か浮動小数点数であれば、まず ``str()`` を使って文字列に変換します。
:param delay: ``delay`` パラメータはテキストのスクロール速度を制御します。
:param wait: ``wait`` が ``True`` である場合、アニメーションが終了するまで関数がブロックし、 そうでない場合にはバックグラウンドで実行されます。
:param loop: ``loop`` が ``True`` である場合、アニメーションを永遠に繰り返します。
:param monospace: ``monospace`` が ``True`` である場合、文字の幅が 5 ピクセルになり、そうでない場合にはスクロール時の文字間の幅が 1 ピクセルになります。

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """ディスプレイをオンにします。

Example: ``display.on()``"""
    ...

def off() -> None:
    """LEDディスプレイをオフにします（ディスプレイを無効にすることにより、GPIO端子を他の目的に再利用できるようになります）。

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """LEDディスプレイが有効であるかどうかを確認します。

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """ディスプレイのまわりの光量を読み取ります。

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...