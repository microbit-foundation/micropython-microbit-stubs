"""創作和播放旋律。"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""旋律：貝多芬 C 小調第五交響曲的開場。"""
ENTERTAINER: Tuple[str, ...]
"""旋律：史考特喬普林的名曲《演藝人》開場。"""
PRELUDE: Tuple[str, ...]
"""旋律：巴哈 48 首前奏曲與賦格曲 C 大調第一前奏曲的開場。"""
ODE: Tuple[str, ...]
"""旋律：貝多芬 D 小調第九交響曲中的「歡樂頌」主題。"""
NYAN: Tuple[str, ...]
"""旋律：Nyan Cat 主題 (http://www.nyan.cat/)。

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""旋律：聽起來像手機鈴聲的東西。

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""旋律：為特務和犯罪首腦準備的放克貝斯。"""
BLUES: Tuple[str, ...]
"""旋律：布基烏基 12 小節藍調走路貝斯。"""
BIRTHDAY: Tuple[str, ...]
"""旋律：「祝你生日快樂……」

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""旋律：華格納歌劇《羅恩格林》中的新娘合唱。"""
FUNERAL: Tuple[str, ...]
"""旋律：《葬禮進行曲》，亦稱為蕭邦的「降 b 小調第二號鋼琴奏鳴曲」。"""
PUNCHLINE: Tuple[str, ...]
"""旋律：一段有趣的音樂，表示說了一個笑話。"""
PYTHON: Tuple[str, ...]
"""旋律：約翰菲利普蘇薩的進行曲《自由鐘》，又名《蒙提派森的飛行馬戲團》的主題曲 (Python 程式語言以此命名)。"""
BADDY: Tuple[str, ...]
"""旋律：無聲電影時代的惡人登場。"""
CHASE: Tuple[str, ...]
"""旋律：無聲電影時代的追逐場景。"""
BA_DING: Tuple[str, ...]
"""旋律：表示某事發生的短訊號。"""
WAWAWAWAA: Tuple[str, ...]
"""旋律：非常悲傷的長號。"""
JUMP_UP: Tuple[str, ...]
"""旋律：用於遊戲中，代表向上移動。"""
JUMP_DOWN: Tuple[str, ...]
"""旋律：用於遊戲中，表示向下移動。"""
POWER_UP: Tuple[str, ...]
"""旋律：表示已解鎖成就的號角齊鳴。"""
POWER_DOWN: Tuple[str, ...]
"""旋律：表示失去成就的悲傷號角聲。"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """設定播放的大致節奏。

Example: ``music.set_tempo(bpm=120)``

:param ticks: 構成節拍的滴答聲數。
:param bpm: 一個整數，決定每分鐘有多少次節拍。

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """以整數元組的形式取得當前節奏：``(ticks, bpm)``。

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """播放音樂。

Example: ``music.play(music.NYAN)``

:param music: 特殊音符中指定的音樂 <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_
:param pin: (引腳) 用於外接揚聲器的輸出引腳 (預設為 ``pin0``)，``None`` 表示無聲音。
:param wait: 如果 ``wait`` 設定為 ``True``，則此函式會封鎖。
:param loop: 如果 ``loop`` 設定為 ``True``，樂曲會重複直到呼叫 ``stop`` 或封鎖呼叫被中斷。

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """彈奏一個音符。 (間距)

Example: ``music.pitch(185, 1000)``

:param frequency: (頻率) 整數頻率
:param duration: 毫秒的持續時間。如果是否定的，則聲音將持續到下一次呼叫或對 ``stop`` 的呼叫。
:param pin: (引腳) 可選輸出引腳 (預設值 ``pin0``)。
:param wait: 如果 ``wait`` 設定為 ``True``，則此函式為封鎖。

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """停止內建揚聲器上的所有音樂播放和任何引腳輸出聲音。

Example: ``music.stop()``

:param pin: (引腳) 可以提供一個可選引數來指定一個引腳，例如 ``music.stop(pin1)``。"""

def reset() -> None:
    """將 ticks、bpm、duration 和 octave 重設為其預設值。

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...