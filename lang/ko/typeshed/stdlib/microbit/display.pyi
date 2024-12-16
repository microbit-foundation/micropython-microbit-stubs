"""5×5 LED 디스플레이에 텍스트, 이미지, 애니메이션을 표시합니다."""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """열 ``x``와 행 ``y``의 LED의 밝기를 불러옵니다.

Example: ``display.get_pixel(0, 0)``

:param x: 디스플레이 열(0..4)
:param y: 디스플레이 행(0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """열 ``x``와 행 ``y``의 LED의 밝기를 설정합니다.

Example: ``display.set_pixel(0, 0, 9)``

:param x: 디스플레이 열(0..4)
:param y: 디스플레이 행(0..4)
:param value: 0(꺼짐)과 9(밝음) 사이의 밝기"""
    ...

def clear() -> None:
    """모든 LED의 밝기를 0(꺼짐)으로 설정합니다.

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """LED 디스플레이에 이미지, 글자 또는 숫자를 표시합니다.

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: 표시할 문자열, 숫자, 이미지 또는 이미지 목록입니다.
:param delay: ``delay``밀리초의 지연 시간을 두고 각 글자, 숫자 또는 이미지가 표시됩니다.
:param wait: ``wait``가 ``True``인 경우 이 기능은 애니메이션이 종료될 때까지 차단됩니다. 그렇지 않은 경우 애니메이션이 백그라운드에서 재생됩니다.
:param loop: ``loop``가 ``True``인 경우 애니메이션이 무한 반복됩니다.
:param clear: ``clear``가 ``True``인 경우 디스플레이는 시퀀스가 종료된 후 내용을 지웁니다.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """LED 디스플레이의 숫자 또는 텍스트를 스크롤합니다.

Example: ``display.scroll('micro:bit')``

:param text: 스크롤할 문자열. 만약 ``text``가 정수 또는 부동수인 경우 먼저 ``str()``을 사용해 변환됩니다.
:param delay: ``delay`` 매개변수는 텍스트 스크롤링 속도를 조절합니다.
:param wait: ``wait``가 ``True``인 경우 이 기능은 애니메이션이 종료될 때까지 차단됩니다. 그렇지 않은 경우 애니메이션이 백그라운드에서 재생됩니다.
:param loop: ``loop``가 ``True``인 경우 애니메이션이 무한 반복됩니다.
:param monospace: ``monospace``가 ``True``인 경우 스크롤 중에 모든 글자는 5열의 픽셀만큼의 너비를 소모하며, 그렇지 않은 경우 글자 사이에 정확히 1열의 픽셀의 공백이 존재합니다.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """LED 디스플레이를 켭니다.

Example: ``display.on()``"""
    ...

def off() -> None:
    """LED 디스플레이를 끕니다(디스플레이를 비활성화하면 GPIO 핀을 다른 목적으로 재사용할 수 있습니다).

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """LED 디스플레이가 활성화되어있는지 확인합니다.

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """밝기 레벨을 읽습니다.

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...