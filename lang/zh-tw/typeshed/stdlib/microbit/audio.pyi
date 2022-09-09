"""使用 micro:bit 播放聲音 (匯入 ``audio`` 與 V1 相容)。 (audio)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """播放內建聲音或自訂音訊幀。 (play)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (source) 內建 ``Sound`` 例如 ``Sound.GIGGLE`` 或作為 ``AudioFrame`` 對象的可迭代樣本資料。
:param wait: (wait) 如果 ``wait`` 為 ``True``，此函式將會封鎖，直到聲音完成。
:param pin: (引腳
) 指定輸出引腳的可選引數可用於覆寫預設值 ``pin0``。如果我們不想播放任何聲音，我們可以使用 ``pin=None``。
:param return_pin: (return pin) 指定差分邊緣連接器引腳，以連接到外部揚聲器而不是接地。在 **V2** 修訂版中，這將會被忽略。"""

def is_playing() -> bool:
    """檢查是否正在播放聲音。 (is playing)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """停止所有音訊播放。 (stop)

Example: ``audio.stop()``"""
    ...

class AudioFrame:
    """``AudioFrame`` 物件是 32 個樣本的列表，每個樣本都是一個無符號位元組 (0 到 255 之間的整數)。 (audioframe)

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...