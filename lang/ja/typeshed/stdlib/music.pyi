"""メロディーの作成と再生。 (music)"""
from typing import Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""メロディ: ベートーヴェンの第5番交響曲第5番のオープニング曲。 (dadadadum)"""
ENTERTAINER: Tuple[str, ...]
"""メロディ: スコット・ジョプリンのラグタイム・クラシック "The Entertainer" のオープニング部分。 (entertainer)"""
PRELUDE: Tuple[str, ...]
"""メロディ: J.S.バッハの 48 のプレリュードとフーガの C メジャーの第1回プレリュードのオープニング。 (prelude)"""
ODE: Tuple[str, ...]
"""メロディ: ベートーヴェンの交響曲第9番から「歓喜の歌」のテーマ。 (ode)"""
NYAN: Tuple[str, ...]
"""メロディ: Nyan Cat テーマ (http://www.nyan.cat/)。 (nyan)

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""メロディ: 携帯電話の着信音のようなもの。 (ringtone)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""メロディ: シークレット・エージェントと犯罪の黒幕のためのファンキーなベースライン。 (funk)"""
BLUES: Tuple[str, ...]
"""メロディ: ブギー・ウーギーの 12 小節のブルース・ウォーキング・ベース。 (blues)"""
BIRTHDAY: Tuple[str, ...]
"""メロディ: 「ハッピーバースディトゥユー ...」 (birthday)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""メロディ: ワグナーのオペラ「ローエングリン」のブライダルコーラス。 (wedding)"""
FUNERAL: Tuple[str, ...]
"""メロディ: フレデリック・ショパンのピアノソナタ第2番「B♭マイナー」の別名「葬儀の行進」35。 (funeral)"""
PUNCHLINE: Tuple[str, ...]
"""メロディ: ジョークが行われたことを意味する楽しい部分。 (punchline)"""
PYTHON: Tuple[str, ...]
"""メロディ: John Philip Sousa さんの行進曲「Liberty Bell」、別名「空飛ぶモンティ・パイソン」 (python)"""
BADDY: Tuple[str, ...]
"""メロディ: 無声映画時代の悪役の登場。 (baddy)"""
CHASE: Tuple[str, ...]
"""メロディ: 無声映画時代のチェイスシーン。 (chase)"""
BA_DING: Tuple[str, ...]
"""メロディ: 何かが起こったことを示す短い信号。 (ba ding)"""
WAWAWAWAA: Tuple[str, ...]
"""メロディ: 非常に悲しいトロンボーン。 (wawawawaa)"""
JUMP_UP: Tuple[str, ...]
"""メロディ: ゲームでの使用で、上方向の動きを示します。 (jump up)"""
JUMP_DOWN: Tuple[str, ...]
"""メロディ: ゲームでの使用で、下向きの動きを示します。 (jump down)"""
POWER_UP: Tuple[str, ...]
"""メロディ: パワーが解放されたことを示すファンファーレ。 (power up)"""
POWER_DOWN: Tuple[str, ...]
"""メロディ: パワーが失われたことを示すための悲しい運命。 (power down)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """再生するためのおおよそのテンポを設定します。 (set tempo)

Example: ``music.set_tempo(bpm=120)``

:param ticks: (ticks) 1ビートを構成するティック数。
:param bpm: (bpm) 毎分のビート数を決定する整数。

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """現在のテンポを整数のタプル ``(ticks, bpm)`` として取得します。 (get tempo)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Union[MicroBitDigitalPin, None]=pin0, wait: bool=True, loop: bool=False) -> None:
    """ミュージックを再生します。 (play)

Example: ``music.play(music.NYAN)``

:param music: (music) `特別な表記 <https://microbit-micropython.readthedocs.io/ja/v2-docs/music.html#musical-notation>`_ で指定されたミュージック
:param pin: (ピン) 外部スピーカーをつなぐ出力端子(デフォルト ``pin0``)。音を鳴らしたくない場合は ``None`` を指定します。
:param wait: (wait) ``wait`` を ``True`` に設定した場合、この関数がブロックします。
:param loop: (loop) ``loop`` が ``True`` の場合、曲は ``stop`` が呼び出されるか、ブロックコールが中断されるまで繰り返し再生されます。

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: MicroBitDigitalPin=pin0, wait: bool=True) -> None:
    """音符を再生します。 (pitch)

Example: ``music.pitch(185, 1000)``

:param frequency: (frequency) 周波数を示す整数値
:param duration: (duration) 持続時間をミリ秒単位で指定します。負の場合、次の呼び出しか ``stop`` の呼び出しまで再生が続きます。
:param pin: (pin) 出力端子を指定するオプション引数(デフォルト ``pin0``)。
:param wait: (wait) ``wait`` を ``True`` に設定した場合、この関数がブロックします。

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: MicroBitDigitalPin=pin0) -> None:
    """内蔵スピーカーやサウンドを出力する端子から鳴らしているすべてのミュージック再生を停止します。 (stop)

Example: ``music.stop()``

:param pin: (pin) オプションの引数にはスピーカの繋がれている端子を指定します。たとえば ``music.stop(pin1)`` などと指定します。"""

def reset() -> None:
    """ticks、bpm、duration、octave をデフォルト値にリセットします。 (reset)

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...