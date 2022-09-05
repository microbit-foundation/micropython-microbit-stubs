"""멜로디를 생성하고 재생합니다. (music)"""
from typing import Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""멜로디: 베토벤의 교향곡 5번 오프닝, C 마이너. (dadadadum)"""
ENTERTAINER: Tuple[str, ...]
"""멜로디: 스콧 조플린의 Ragtime classic “The Entertainer” 오프닝 일부. (entertainer)"""
PRELUDE: Tuple[str, ...]
"""멜로디: 요한 제바스티안 바흐의 48 Preludes and Fugues 첫 전주곡 오프닝 (prelude)"""
ODE: Tuple[str, ...]
"""멜로디: Beethoven의 교향곡 9번 “Ode to Joy” 테마, D 마이너. (ode)"""
NYAN: Tuple[str, ...]
"""멜로디: Nyan Cat 테마 (http://www.nyan.cat/). (nyan)

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""멜로디: 휴대폰 벨소리와 유사한 소리. (ringtone)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""멜로디: 비밀 요원과 천재 범죄자들을 위한 펑키 베이스 라인. (funk)"""
BLUES: Tuple[str, ...]
"""멜로디: 부기 우기 12바 블루스 워킹 베이스. (blues)"""
BIRTHDAY: Tuple[str, ...]
"""멜로디: “생일 축하합니다…” (birthday)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melody: 바그너의 오페라 “로엔그린”의 혼례의 합창. (wedding)"""
FUNERAL: Tuple[str, ...]
"""멜로디: “장송행진곡”이라고도 알려진 프레데리크 쇼팽의 피아노 소나타 2번 B♭ 마이너, Op. 35. (funeral)"""
PUNCHLINE: Tuple[str, ...]
"""멜로디: a fun fragment that signifies a joke has been made. (punchline)"""
PYTHON: Tuple[str, ...]
"""멜로디: 존 필립 수자의 “자유의 종” 행진곡. “몬티 파이튼의 비행 서커스” 테마곡으로도 알려짐(이에 따라 Python 프로그래밍 언어가 이름지어짐). (python)"""
BADDY: Tuple[str, ...]
"""멜로디: 무성 영화 시대의 악당 등장. (baddy)"""
CHASE: Tuple[str, ...]
"""멜로디: 무성 영화 시대의 추격 장면 (chase)"""
BA_DING: Tuple[str, ...]
"""멜로디: 무언가 일어났다는 걸 알려주는 짧은 신호. (ba ding)"""
WAWAWAWAA: Tuple[str, ...]
"""멜로디: 아주 슬픈 트럼본 소리. (wawawawaa)"""
JUMP_UP: Tuple[str, ...]
"""멜로디: 게임에서 위로 움직이는 걸 표현하는 소리. (jump up)"""
JUMP_DOWN: Tuple[str, ...]
"""멜로디: 게임에서 아래로 움직이는 걸 표현하는 소리. (jump down)"""
POWER_UP: Tuple[str, ...]
"""멜로디: 업적 달성을 의미하는 팡파레. (power up)"""
POWER_DOWN: Tuple[str, ...]
"""멜로디: 업적 실패를 의미하는 슬픈 팡파레. (power down)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """플레이백의 빠르기를 대략 설정합니다. (set tempo)

Example: ``music.set_tempo(bpm=120)``

:param ticks: (ticks) 비트 하나를 구성하는 틱의 수.
:param bpm: (bpm) 정수로 분당 비트 수를 결정합니다.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """현재 빠르기를 정수로 된 튜플로 가져옵니다: ``(ticks, bpm)``. (get tempo)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Union[MicroBitDigitalPin, None]=pin0, wait: bool=True, loop: bool=False) -> None:
    """음악을 재생합니다. (play)

Example: ``music.play(music.NYAN)``

:param music: (music) `별첨 <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_에 명시된 음악
:param pin: (핀) 외장 스피커에 사용할 출력 핀(기본 ``pin0``), ``None``으로 설정하면 소리가 재생되지 않습니다.
:param wait: (wait) ``wait``이 ``True``로 된 경우 이 기능은 블로킹 상태가 됩니다.
:param loop: (loop) ``loop``가 ``True``인 경우 ``stop``이 호출되거나 블로킹 호출이 인터럽트되기 전까지 계속 반복됩니다.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: MicroBitDigitalPin=pin0, wait: bool=True) -> None:
    """음을 재생합니다. (앞-뒤 기울기)

Example: ``music.pitch(185, 1000)``

:param frequency: (진동수) 정수로 된 진동수.
:param duration: (duration) 밀리초 단위의 기간. 음수인 경우 소리가 다음 호출 또는 ``stop`` 호출까지 계속 재생됩니다.
:param pin: (핀) 선택 사항의 출력 핀(기본 ``pin0``).
:param wait: (wait) ``wait``이 ``True``로 된 경우 이 기능은 블로킹 상태가 됩니다.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: MicroBitDigitalPin=pin0) -> None:
    """내장 스피커와 핀으로 출력되는 모든 음악 플레이백을 멈춥니다. (stop)

Example: ``music.stop()``

:param pin: (핀) 선택적으로 핀을 특정하기 위한 인자 예: ``music.stop(pin1)``."""

def reset() -> None:
    """틱, bpm, 기간 및 옥타브를 기본값으로 초기화합니다. (reset)

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...