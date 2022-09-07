"""micro:bitでサウンドを再生します（V1との互換のために ``audio`` をインポートしてください）。 (audio)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """内蔵のサウンドまたはカスタムオーディオフレームを再生します。 (play)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (source) ``Sound`` モジュールに含まれる ``Sound.GIGGLE`` などの内蔵サウンド、または ``AudioFrame`` オブジェクトのイテラブルとしてのサンプルデータ。
:param wait: (wait) ``wait`` が ``True`` の場合、サウンドの再生が終わるまでこの関数がブロックします。
:param pin: (ピン) 出力端子をデフォルトの ``pin0`` から変えるためのオプション引数です。音を鳴らしたくない場合は ``pin=None`` を指定します。
:param return_pin: (return pin) スピーカーの２本ある線の一方を接続する先である GND を別の端子にしたい場合に使います。 **V2** ではこの指定を無視します。"""

def is_playing() -> bool:
    """オーディオが再生中であるかどうかを確認します。 (is playing)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """すべてのオーディオ再生を停止します。 (stop)

Example: ``audio.stop()``"""
    ...

class AudioFrame:
    """``AudioFrame`` オブジェクトは32項目のリストです。各項目の値は符号なしバイト(0と255の間の整数)です。 (audioframe)

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