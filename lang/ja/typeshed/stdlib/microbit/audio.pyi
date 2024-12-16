"""micro:bitでサウンドを再生します（V1との互換のために ``audio`` をインポートしてください）。"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """内蔵サウンド、サウンド効果、カスタム化したオーディオフレームのいずれかを再生します。

Example: ``audio.play(Sound.GIGGLE)``

:param source: ``Sound.GIGGLE`` などの内蔵の``Sound``、``SoundEffect``、``AudioFrame`` オブジェクトのイテラブルであるサンプルデータのいずれか。
:param wait: ``wait`` が ``True`` の場合、サウンドの再生が終わるまでこの関数がブロックします。
:param pin: (ピン) 出力端子をデフォルトの ``pin0`` から変えるためのオプション引数です。音を鳴らしたくない場合は ``pin=None`` を指定します。
:param return_pin: グランドではなく外部スピーカーに接続する差動エッジコネクタの端子
を指定します。**V2** ではこの指定を無視します。"""

def is_playing() -> bool:
    """オーディオが再生中であるかどうかを確認します。

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """すべてのオーディオ再生を停止します。

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """コンストラクタや属性で設定したパラメータのセットで構成されるサウンド効果。"""
    WAVEFORM_SINE: ClassVar[int]
    """``waveform`` パラメータに指定できる「サイン波」オプション。"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """``waveform`` パラメータに指定できる「のこぎり波」オプション。"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """``waveform`` パラメータに指定できる「三角波」オプション。"""
    WAVEFORM_SQUARE: ClassVar[int]
    """``waveform`` パラメータに指定できる「矩形波」オプション。"""
    WAVEFORM_NOISE: ClassVar[int]
    """``waveform`` パラメータに指定できる「ノイズ」オプション。"""
    SHAPE_LINEAR: ClassVar[int]
    """``shape`` パラメータに指定できる「リニア補間」オプション。"""
    SHAPE_CURVE: ClassVar[int]
    """``shape`` パラメータに指定できる「カーブ補間」オプション。"""
    SHAPE_LOG: ClassVar[int]
    """``shape`` パラメータに指定できる「対数補間」オプション。"""
    FX_NONE: ClassVar[int]
    """``fx`` パラメータに指定できる「効果なし」オプション。"""
    FX_TREMOLO: ClassVar[int]
    """``fx`` パラメータに指定できる「トレモロ効果」オプション。"""
    FX_VIBRATO: ClassVar[int]
    """``fx`` パラメータに指定できる「ビブラート効果」オプション。"""
    FX_WARBLE: ClassVar[int]
    """``fx`` パラメータに指定できる「ワブル効果」オプション。"""
    freq_start: int
    """開始周波数。単位はヘルツ(Hz)で、``0``から``9999``の範囲の数値です。"""
    freq_end: int
    """終了周波数。単位はヘルツ(Hz)で、``0``から``9999``の範囲の数値です。"""
    duration: int
    """サウンドの長さ。``0`` から``9999``の範囲の数値です。"""
    vol_start: int
    """開始音量。``0``から``255``の範囲の数値です。"""
    vol_end: int
    """終了音量。``0``から``255``の範囲の数値です。"""
    waveform: int
    """波形の種類。次の値のいずれか: ``WAVEFORM_SINE``、 ``WAVEFORM_SAWTOOTH``、``WAVEFORM_TRIANGLE``、 ``WAVEFORM_SQUARE``、``WAVEFORM_NOISE`` (ランダムに生成したノイズ)"""
    fx: int
    """サウンドに追加する効果。次の値のいずれか: ``FX_TREMOLO``、``FX_VIBRATO``、``FX_WARBLE``、``FX_NONE``"""
    shape: int
    """開始周波数と終了周波数の補間曲線の種類で、波形の違いにより周波数の変化率が異なります。次の値のうちのいずれか: ``SHAPE_LINEAR``、``SHAPE_CURVE``、``SHAPE_LOG``"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """新しいサウンド効果を作成します。

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: 開始周波数。単位はヘルツ(Hz)で、``0``から``9999``の範囲の数値です。
:param freq_end: 終了周波数。単位はヘルツ(Hz)で、``0``から``9999``の範囲の数値です。
:param duration: サウンドの長さ。単位はミリ秒で、``0`` から``9999``の範囲の数値です。
:param vol_start: 開始音量。``0``から``255``の範囲の数値です。
:param vol_end: 終了音量。``0``から``255``の範囲の数値です。
:param waveform: 波形の種類。次の値のいずれか: ``WAVEFORM_SINE``、 ``WAVEFORM_SAWTOOTH``、``WAVEFORM_TRIANGLE``、 ``WAVEFORM_SQUARE``、``WAVEFORM_NOISE`` (ランダムに生成したノイズ)。
:param fx: サウンドに追加する効果。次の値のいずれか: ``FX_TREMOLO``、``FX_VIBRATO``、``FX_WARBLE``、``FX_NONE``
:param shape: 開始周波数と終了周波数の補間曲線の種類で、波形の違いにより周波数の変化率が異なります。次の値のうちのいずれか: ``SHAPE_LINEAR``、``SHAPE_CURVE``、``SHAPE_LOG``"""

    def copy(self) -> SoundEffect:
        """この ``SoundEffect`` のコピーを作成します。

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """``AudioFrame`` オブジェクトは32個のサンプルからなるリストです。それぞのサンプルは符号なしバイト（0〜255の整数）です。

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """この ``AudioFrame`` のデータを、別の ``AudioFrame`` インスタンスのデータで上書きします。

Example: ``my_frame.copyfrom(source_frame)``

:param other: コピーするデータを持つ ``AudioFrame`` インスタンス。"""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...