"""创建并播放旋律。 (音乐)"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""旋律：《贝多芬 C 小调第五交响曲》开场曲。"""
ENTERTAINER: Tuple[str, ...]
"""旋律：斯科特·乔普林的拉格泰姆经典“演艺人”的开场片段。 (演艺人)"""
PRELUDE: Tuple[str, ...]
"""旋律：约翰·塞巴斯蒂安·巴赫48首前奏曲和赋格曲中 C 大调第一前奏曲的开场。 (序幕)"""
ODE: Tuple[str, ...]
"""旋律：贝多芬 D 小调第九交响曲中的“欢乐颂”主题。 (欢乐颂)"""
NYAN: Tuple[str, ...]
"""旋律：彩虹猫主题 (http://www.nyan.cat/)。 (彩虹猫)

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""旋律：听起来像手机铃声的乐曲。 (铃声)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""旋律：一曲为特工和犯罪主谋制作的 funky bass。 (朋克)"""
BLUES: Tuple[str, ...]
"""旋律：布吉伍吉 12 小节布鲁斯 walking bass。 (布鲁斯)"""
BIRTHDAY: Tuple[str, ...]
"""旋律：“祝你生日快乐……” (生日)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""旋律：瓦格纳歌剧《罗恩格林》中的新娘合唱。 (婚礼)"""
FUNERAL: Tuple[str, ...]
"""旋律：“葬礼进行曲”，也被称为弗雷德里克肖邦的 B♭ 小调第二钢琴奏鸣曲，Op. 35。 (哀乐)"""
PUNCHLINE: Tuple[str, ...]
"""旋律：一个有趣的片段，表示开了一个玩笑。 (笑点)"""
PYTHON: Tuple[str, ...]
"""旋律：约翰·菲利普·苏萨的进行曲《自由钟》，即《巨蟒剧团之飞翔的马戏团》的主题曲（Python 编程语言以此命名）。 (Python)"""
BADDY: Tuple[str, ...]
"""旋律：默片时代反面角色的入场曲。 (反面角色)"""
CHASE: Tuple[str, ...]
"""旋律：无声电影时代的追逐场景。 (追逐)"""
BA_DING: Tuple[str, ...]
"""旋律：表示某事发生的简短信号。"""
WAWAWAWAA: Tuple[str, ...]
"""旋律：非常悲伤的长号。"""
JUMP_UP: Tuple[str, ...]
"""旋律：用于游戏中，表示向上运动。 (向上跳)"""
JUMP_DOWN: Tuple[str, ...]
"""旋律：用于游戏中，表示向下运动。 (向下跳)"""
POWER_UP: Tuple[str, ...]
"""旋律：表示解锁成就的号角。 (能力增强)"""
POWER_DOWN: Tuple[str, ...]
"""旋律：表示失去成就的悲伤号角。 (能力减弱)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """设置播放的大致节奏。 (设置节奏)

Example: ``music.set_tempo(bpm=120)``

:param ticks: (刻度) 构成一个节拍的刻度数。
:param bpm: (每分钟节拍数) 一个整数，确定每分钟有多少拍。

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """以整数元组的形式获取当前节奏：``(ticks, bpm)``。 (获得节奏值)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """播放音乐。 (播放)

Example: ``music.play(music.NYAN)``

:param music: (音乐) `a special notation <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_中指定的音乐
:param pin: (引脚) 用于外接扬声器的输出引脚（默认为 ``pin0``），``None`` 表示无声音。
:param wait: (等待) 如果 ``wait`` 设置为 ``True``，则此函数阻塞。
:param loop: 如果 ``loop`` 设置为 ``True``，曲调会重复直到调用 ``stop`` 或阻塞调用被中断。

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """播放一个音符。 (音高)

Example: ``music.pitch(185, 1000)``

:param frequency: (频率) 整数频率
:param duration: (持续) 一毫秒的持续时间。如果是负的，则声音将持续到下一次调用或对 ``stop`` 的调用。
:param pin: (引脚) 可选输出引脚（默认值``pin0``）。
:param wait: (等待) 如果 ``wait`` 设置为 ``True``，则此函数阻塞。

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """停止内置扬声器播放任何音乐，并停止发出任何引脚输出的声音。 (停止)

Example: ``music.stop()``

:param pin: (引脚) 可以提供可选参数来指定一个引脚，如``music.stop(pin1)``。"""

def reset() -> None:
    """将 ticks、bpm、duration 和 octave重置为默认值。

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...