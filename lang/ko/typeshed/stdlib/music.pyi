"""멜로디를 생성하고 재생합니다."""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""멜로디: 베토벤의 교향곡 제5번 다 단조 도입부입니다."""
ENTERTAINER: Tuple[str, ...]
"""멜로디: 스콧 조플린의 래그타임 고전 “The Entertainer” 도입부 일부입니다."""
PRELUDE: Tuple[str, ...]
"""멜로디: 요한 제바스티안 바흐의 48 Preludes and Fugues 다 장조 첫 전주곡 도입부입니다."""
ODE: Tuple[str, ...]
"""멜로디: 베토벤의 교향곡 제9번 라 단조 “Ode to Joy” 테마입니다."""
NYAN: Tuple[str, ...]
"""멜로디: Nyan Cat 테마입니다(http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""멜로디: 휴대폰 벨소리와 유사한 소리입니다.

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""멜로디: 비밀 요원과 천재 범죄자에 어울리는 펑키 베이스 라인입니다."""
BLUES: Tuple[str, ...]
"""멜로디: 부기 우기 12바 블루스 워킹 베이스입니다."""
BIRTHDAY: Tuple[str, ...]
"""멜로디: 생일 축하 노래입니다.

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melody: 바그너의 오페라 “로엔그린”의 결혼식 합창입니다."""
FUNERAL: Tuple[str, ...]
"""멜로디: “장송행진곡”이라고도 알려진 프레데리크 쇼팽의 피아노 소나타 제2번 B♭ 단조 Op. 35입니다."""
PUNCHLINE: Tuple[str, ...]
"""멜로디: 농담할 때 나오는 재미있는 멜로디입니다."""
PYTHON: Tuple[str, ...]
"""멜로디: 존 필립 수자의 “자유의 종” 행진곡입니다. “몬티 파이튼의 비행 서커스” 테마곡으로도 알려져 있습니다(Python 프로그래밍 언어는 몬티 파이튼의 이름에서 유래했습니다)."""
BADDY: Tuple[str, ...]
"""멜로디: 무성 영화 시대의 악당 등장 멜로디입니다."""
CHASE: Tuple[str, ...]
"""멜로디: 무성 영화 시대의 추격 장면 멜로디입니다."""
BA_DING: Tuple[str, ...]
"""멜로디:어떤 일이 일어났다는 것을 알려주는 짧은 신호음입니다."""
WAWAWAWAA: Tuple[str, ...]
"""멜로디: 아주 슬픈 트럼본 소리입니다."""
JUMP_UP: Tuple[str, ...]
"""멜로디: 게임에서 위로 움직이는 것을 표현하는 소리입니다."""
JUMP_DOWN: Tuple[str, ...]
"""멜로디: 게임에서 아래로 움직이는 것을 표현하는 소리입니다."""
POWER_UP: Tuple[str, ...]
"""멜로디: 업적 달성을 알리는 팡파르 소리입니다."""
POWER_DOWN: Tuple[str, ...]
"""멜로디: 업적 달성 실패를 의미하는 슬픈 팡파르 소리입니다."""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """플레이백의 빠르기를 대략적으로 설정합니다.

Example: ``music.set_tempo(bpm=120)``

:param ticks: 비트 하나를 구성하는 틱의 수입니다.
:param bpm: 분당 비트 수를 결정하는 정수입니다.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """현재 빠르기를 정수 튜플로 가져옵니다: ``(ticks, bpm)``.

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """음악을 재생합니다.

Example: ``music.play(music.NYAN)``

:param music: `별첨 <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_에 명시된 음악
:param pin: (핀) 외장 스피커에 사용할 출력 핀입니다(기본값 ``pin0``). ``None``으로 설정하면 소리가 재생되지 않습니다.
:param wait: ``wait``이 ``True``로 설정된 경우 이 기능은 블로킹 상태가 됩니다.
:param loop: ``loop``가 ``True``인 경우 ``stop``이 호출되거나 블로킹 호출이 인터럽트되기 전까지 계속 반복됩니다.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """음을 재생합니다. (앞-뒤 기울기)

Example: ``music.pitch(185, 1000)``

:param frequency: (진동수) 정수 진동수입니다.
:param duration: 밀리초 단위의 기간입니다. 음수인 경우 소리가 다음 호출 또는 ``stop`` 호출까지 계속 재생됩니다.
:param pin: (핀) 출력 핀입니다(기본값 ``pin0``)(선택 사항).
:param wait: ``wait``이 ``True``로 설정된 경우 이 기능은 블로킹 상태가 됩니다.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """내장 스피커와 핀으로 출력되는 모든 음악 플레이백을 멈춥니다.

Example: ``music.stop()``

:param pin: (핀) 핀을 특정하기 위한 인자입니다(예: ``music.stop(pin1)``)(선택 사항)."""

def reset() -> None:
    """틱, bpm, 기간 및 옥타브를 기본값으로 초기화합니다.

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...