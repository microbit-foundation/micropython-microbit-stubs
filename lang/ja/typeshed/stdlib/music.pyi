"""メロディーの作成と再生。"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""メロディ: ベートーヴェンの交響曲第5番ハ短調の冒頭。"""
ENTERTAINER: Tuple[str, ...]
"""メロディ: スコット・ジョプリンのラグタイム・クラシック『ジ・エンターテイナー 』の冒頭。"""
PRELUDE: Tuple[str, ...]
"""メロディ: J・S・バッハの前奏曲とフーガ計48曲の前奏曲第1番ハ長調の冒頭。"""
ODE: Tuple[str, ...]
"""メロディ: ベートーヴェンの交響曲第9番ニ短調より『歓喜の歌』のテーマ。"""
NYAN: Tuple[str, ...]
"""メロディ: Nyan Cat テーマ (http://www.nyan.cat/)。

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""メロディ: 携帯電話の着信音のようなもの。

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""メロディ: スパイと犯罪の黒幕用のファンキーなベースライン。"""
BLUES: Tuple[str, ...]
"""メロディ: ブギー・ウーギーの 12 小節のブルース・ウォーキング・ベース。"""
BIRTHDAY: Tuple[str, ...]
"""メロディ:『ハッピーバースディトゥユー ...』

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""メロディ: ワグナーのオペラ『ローエングリン』より婚礼の合唱。"""
FUNERAL: Tuple[str, ...]
"""メロディ: フレデリック・ショパンのピアノソナタ第2番変ロ短調 作品35（別名『葬送』）。"""
PUNCHLINE: Tuple[str, ...]
"""メロディ: ジョークが言われたことを意味する楽しい音楽。"""
PYTHON: Tuple[str, ...]
"""メロディ: ジョン・フィリップ・スーザの『自由の鐘』（『空飛ぶモンティ・パイソン』のテーマともいう）（プログラミング言語Pythonの名前の由来となった）。"""
BADDY: Tuple[str, ...]
"""メロディ: 無声映画時代の悪役の登場。"""
CHASE: Tuple[str, ...]
"""メロディ: 無声映画時代のチェイスシーン。"""
BA_DING: Tuple[str, ...]
"""メロディ: 何かが起こったことを示す短い信号。"""
WAWAWAWAA: Tuple[str, ...]
"""メロディ: 非常に悲しいトロンボーン。"""
JUMP_UP: Tuple[str, ...]
"""メロディ: ゲームでの使用で、上方向の動きを示します。"""
JUMP_DOWN: Tuple[str, ...]
"""メロディ: ゲームでの使用で、下向きの動きを示します。"""
POWER_UP: Tuple[str, ...]
"""メロディ: アチーブメントを達成したことを示すファンファーレ。"""
POWER_DOWN: Tuple[str, ...]
"""メロディ: アチーブメントを達成しなかったことを示すファンファーレ。"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """再生するためのおおよそのテンポを設定します。

Example: ``music.set_tempo(bpm=120)``

:param ticks: 1ビートを構成するティック数。
:param bpm: 毎分のビート数を決定する整数。

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """現在のテンポを整数のタプル ``(ticks, bpm)`` として取得します。

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """ミュージックを再生します。

Example: ``music.play(music.NYAN)``

:param music: `特別な表記 <https://microbit-micropython.readthedocs.io/ja/v2-docs/music.html#musical-notation>`_ で指定されたミュージック
:param pin: (ピン) 外部スピーカー用出力端子（デフォルトは ``pin0``）。音を鳴らしたくない場合は ``None`` を指定します。
:param wait: ``wait`` を ``True`` に設定した場合、この関数がブロックします。
:param loop: ``loop`` が ``True`` の場合、曲は ``stop`` が呼び出されるか、ブロックコールが中断されるまで繰り返し再生されます。

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """音符を再生します。

Example: ``music.pitch(185, 1000)``

:param frequency: 周波数を示す整数値
:param duration: 持続時間をミリ秒単位で指定します。負の場合、次の呼び出しか ``stop`` の呼び出しまで再生が続きます。
:param pin: オプションの出力端子（デフォルトは ``pin0``）。
:param wait: ``wait`` を ``True`` に設定した場合、この関数がブロックします。

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """内蔵スピーカーやサウンドを出力する端子から鳴らしているすべてのミュージック再生を停止します。

Example: ``music.stop()``

:param pin: オプションの引数には、たとえば ``music.stop(pin1)`` などの端子を指定できます。"""

def reset() -> None:
    """ティック、bpm、持続時間、オクターブをデフォルト値にリセットします。

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...