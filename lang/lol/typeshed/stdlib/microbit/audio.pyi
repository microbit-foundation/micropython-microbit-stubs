"""crwdns329964:0``audio``crwdne329964:0 (crwdns329962:0crwdne329962:0)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """crwdns335834:0crwdne335834:0 (crwdns329966:0crwdne329966:0)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (crwdns329978:0crwdne329978:0) crwdns335836:0``Sound``crwdnd335836:0``Sound.GIGGLE``crwdnd335836:0``SoundEffect``crwdnd335836:0``AudioFrame``crwdne335836:0
:param wait: (crwdns329982:0crwdne329982:0) crwdns329984:0``wait``crwdnd329984:0``True``crwdne329984:0
:param pin: (crwdns329970:0crwdne329970:0) crwdns329972:0``pin0``crwdne329972:0
:param return_pin: (crwdns329974:0crwdne329974:0) crwdns329976:0crwdne329976:0"""

def is_playing() -> bool:
    """crwdns329988:0crwdne329988:0 (crwdns329986:0crwdne329986:0)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """crwdns329992:0crwdne329992:0 (crwdns329990:0crwdne329990:0)

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """crwdns335840:0crwdne335840:0 (crwdns335838:0crwdne335838:0)"""
    WAVEFORM_SINE: ClassVar[int]
    """crwdns335844:0``waveform``crwdne335844:0 (crwdns335842:0crwdne335842:0)"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """crwdns335848:0``waveform``crwdne335848:0 (crwdns335846:0crwdne335846:0)"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """crwdns335852:0``waveform``crwdne335852:0 (crwdns335850:0crwdne335850:0)"""
    WAVEFORM_SQUARE: ClassVar[int]
    """crwdns335856:0``waveform``crwdne335856:0 (crwdns335854:0crwdne335854:0)"""
    WAVEFORM_NOISE: ClassVar[int]
    """crwdns335860:0``waveform``crwdne335860:0 (crwdns335858:0crwdne335858:0)"""
    SHAPE_LINEAR: ClassVar[int]
    """crwdns335864:0``shape``crwdne335864:0 (crwdns335862:0crwdne335862:0)"""
    SHAPE_CURVE: ClassVar[int]
    """crwdns335868:0``shape``crwdne335868:0 (crwdns335866:0crwdne335866:0)"""
    SHAPE_LOG: ClassVar[int]
    """crwdns335872:0``shape``crwdne335872:0 (crwdns335870:0crwdne335870:0)"""
    FX_NONE: ClassVar[int]
    """crwdns335876:0``fx``crwdne335876:0 (crwdns335874:0crwdne335874:0)"""
    FX_TREMOLO: ClassVar[int]
    """crwdns335880:0``fx``crwdne335880:0 (crwdns335878:0crwdne335878:0)"""
    FX_VIBRATO: ClassVar[int]
    """crwdns335884:0``fx``crwdne335884:0 (crwdns335882:0crwdne335882:0)"""
    FX_WARBLE: ClassVar[int]
    """crwdns335888:0``fx``crwdne335888:0 (crwdns335886:0crwdne335886:0)"""
    freq_start: int
    """crwdns335892:0``0``crwdnd335892:0``9999``crwdne335892:0 (crwdns335890:0crwdne335890:0)"""
    freq_end: int
    """crwdns335896:0``0``crwdnd335896:0``9999``crwdne335896:0 (crwdns335894:0crwdne335894:0)"""
    duration: int
    """crwdns335900:0``0``crwdnd335900:0``9999``crwdne335900:0 (crwdns335898:0crwdne335898:0)"""
    vol_start: int
    """crwdns335904:0``0``crwdnd335904:0``255``crwdne335904:0 (crwdns335902:0crwdne335902:0)"""
    vol_end: int
    """crwdns335908:0``0``crwdnd335908:0``255``crwdne335908:0 (crwdns335906:0crwdne335906:0)"""
    waveform: int
    """crwdns335912:0``WAVEFORM_SINE``crwdnd335912:0``WAVEFORM_SAWTOOTH``crwdnd335912:0``WAVEFORM_TRIANGLE``crwdnd335912:0``WAVEFORM_SQUARE``crwdnd335912:0``WAVEFORM_NOISE``crwdne335912:0 (crwdns335910:0crwdne335910:0)"""
    fx: int
    """crwdns335916:0``FX_TREMOLO``crwdnd335916:0``FX_VIBRATO``crwdnd335916:0``FX_WARBLE``crwdnd335916:0``FX_NONE``crwdne335916:0 (crwdns335914:0crwdne335914:0)"""
    shape: int
    """crwdns335920:0``SHAPE_LINEAR``crwdnd335920:0``SHAPE_CURVE``crwdnd335920:0``SHAPE_LOG``crwdne335920:0 (crwdns335918:0crwdne335918:0)"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """crwdns335924:0crwdne335924:0 (crwdns335922:0crwdne335922:0)

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: (crwdns335934:0crwdne335934:0) crwdns335936:0``0``crwdnd335936:0``9999``crwdne335936:0
:param freq_end: (crwdns335930:0crwdne335930:0) crwdns335932:0``0``crwdnd335932:0``9999``crwdne335932:0
:param duration: (crwdns335926:0crwdne335926:0) crwdns335928:0``0``crwdnd335928:0``9999``crwdne335928:0
:param vol_start: (crwdns335950:0crwdne335950:0) crwdns335952:0``0``crwdnd335952:0``255``crwdne335952:0
:param vol_end: (crwdns335946:0crwdne335946:0) crwdns335948:0``0``crwdnd335948:0``255``crwdne335948:0
:param waveform: (crwdns335954:0crwdne335954:0) crwdns335956:0``WAVEFORM_SINE``crwdnd335956:0``WAVEFORM_SAWTOOTH``crwdnd335956:0``WAVEFORM_TRIANGLE``crwdnd335956:0``WAVEFORM_SQUARE``crwdnd335956:0``WAVEFORM_NOISE``crwdne335956:0
:param fx: (crwdns335938:0crwdne335938:0) crwdns335940:0``FX_TREMOLO``crwdnd335940:0``FX_VIBRATO``crwdnd335940:0``FX_WARBLE``crwdnd335940:0``FX_NONE``crwdne335940:0
:param shape: (crwdns335942:0crwdne335942:0) crwdns335944:0``SHAPE_LINEAR``crwdnd335944:0``SHAPE_CURVE``crwdnd335944:0``SHAPE_LOG``crwdne335944:0"""

    def copy(self) -> SoundEffect:
        """crwdns335960:0``SoundEffect``crwdne335960:0 (crwdns335958:0crwdne335958:0)

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """crwdns329996:0``AudioFrame``crwdne329996:0 (crwdns329994:0crwdne329994:0)

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """crwdns335964:0``AudioFrame``crwdnd335964:0``AudioFrame``crwdne335964:0 (crwdns335962:0crwdne335962:0)

Example: ``my_frame.copyfrom(source_frame)``

:param other: (crwdns335966:0crwdne335966:0) crwdns335968:0``AudioFrame``crwdne335968:0"""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...