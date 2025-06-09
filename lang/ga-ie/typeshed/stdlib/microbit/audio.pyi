"""Seinn fuaimeanna ag baint úsáide as an micro:bit (allmhairiú ``audio`` le haghaidh comhoiriúnacht V1). (fuaime)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Seinn fuaim-tógtha i, éifeacht fuaime nó frámaí fuaime saincheaptha. (seinn)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (foinse) ``Sound`` ionsuite amhail ``Sound.GIGGLE``, ``SoundEffect`` nó sonraí samplacha mar athrá ar réada ``AudioFrame``.
:param wait: (fan) Má tá ``wait`` ``True``, blocálfaidh an fheidhm seo go dtí go mbeidh an fhuaim críochnaithe.
:param pin: (biorán) Is féidir argóint roghnach chun an bioráin aschuir a shonrú a úsáid chun mainneachtain ``pin0``a shárú. Mura dteastaíonn aon fhuaim uainn is féidir linn ``pin=None``a úsáid.
:param return_pin: (biorán fillte) Sonraíonn bioráin cónascaire imeall difreálach chun ceangal le cainteoir seachtrach in ionad na talún. Déantar neamhaird air seo don athbhreithniú **V2**."""

def is_playing() -> bool:
    """Seiceáil an bhfuil fuaim á seinm. (ag seinm)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Stop gach athsheinm fuaime. (stad)

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Éifeacht fuaime, comhdhéanta ag sraith paraiméadar cumraithe tríd an cruthaitheoir nó tréithe. (éifeachtfuaime)"""
    WAVEFORM_SINE: ClassVar[int]
    """Rogha tonn sine a úsáidtear don pharaiméadar ``waveform`` . (tonnchruth síneas)"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Rogha tonn fiacail sábha a úsáidtear don pharaiméadar ``waveform`` . (tonnfhad fiacail sábha)"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """Rogha tonn triantáin a úsáidtear don pharaiméadar ``waveform`` . (triantán tonnchrutha)"""
    WAVEFORM_SQUARE: ClassVar[int]
    """Rogha tonn cearnach a úsáidtear don pharaiméadar ``waveform`` . (cearnóg tonnfhoirme)"""
    WAVEFORM_NOISE: ClassVar[int]
    """Rogha torainn a úsáidtear don pharaiméadar ``waveform`` . (torann tonnfhoirme)"""
    SHAPE_LINEAR: ClassVar[int]
    """Rogha idirshuíomh líneach a úsáidtear don pharaiméadar ``shape`` . (cruth líneach)"""
    SHAPE_CURVE: ClassVar[int]
    """Rogha idirshuíomh cuar a úsáidtear don pharaiméadar ``shape`` . (cruth cuar)"""
    SHAPE_LOG: ClassVar[int]
    """Rogha idirshuíomh logartamach a úsáidtear don pharaiméadar ``shape`` . (log cruth)"""
    FX_NONE: ClassVar[int]
    """Níl aon rogha éifeachta in úsáid don pharaiméadar ``fx`` . (fx aon cheann)"""
    FX_TREMOLO: ClassVar[int]
    """Rogha éifeachta Tremolo a úsáidtear don pharaiméadar ``fx`` . (tremolo fx)"""
    FX_VIBRATO: ClassVar[int]
    """Rogha éifeachta Vibrato a úsáidtear don pharaiméadar ``fx`` ."""
    FX_WARBLE: ClassVar[int]
    """Rogha éifeacht warble a úsáidtear le haghaidh an paraiméadar ``fx`` ."""
    freq_start: int
    """Tosaigh minicíocht i Hertz (Hz), uimhir idir ``0`` agus ``9999`` (tús minicíochta)"""
    freq_end: int
    """Minicíocht deiridh i Heirts (Hz), uimhir idir ``0`` agus ``9999`` (deireadh freq)"""
    duration: int
    """Fad na fuaime i milleasoicindí, uimhir idir ``0`` agus ``9999`` (fad)"""
    vol_start: int
    """Tosaigh luach toirte, uimhir idir ``0`` agus ``255`` (tús vol)"""
    vol_end: int
    """Luach toirte deiridh, uimhir idir ``0`` agus ``255`` (deireadh imleabhair)"""
    waveform: int
    """Cineál cruth waveform, ceann de na luachanna seo: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (torann a ghintear go randamach) (tonnchruth)"""
    fx: int
    """Éifeacht le cur leis an bhfuaim, ceann amháin de na luachanna seo a leanas: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, nó ``FX_NONE``"""
    shape: int
    """An cineál cuar idirshuíomh idir na minicíochtaí tosaigh agus deiridh, tá cruthanna tonn éagsúla rátaí éagsúla athraithe i minicíocht. Ceann de na luachanna seo a leanas: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG`` (cruth)"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Cruthaigh éifeacht fuaime nua.

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: (tús minicíochta) Tosaigh minicíocht i Hertz (Hz), uimhir idir ``0`` agus ``9999``.
:param freq_end: (deireadh minicíochta) Minicíocht deiridh i Hertz (Hz), uimhir idir ``0`` agus ``9999``.
:param duration: (fad) Fad na fuaime i milleasoicindí, uimhir idir ``0`` agus ``9999``.
:param vol_start: (tús toirte) Tosaigh luach toirte, uimhir idir ``0`` agus ``255``.
:param vol_end: (deireadh an toirte) Luach deiridh an toirte, uimhir idir ``0`` agus ``255``.
:param waveform: (tonnfhoirm) Cineál cruth waveform, ceann de na luachanna seo: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (torann a ghintear go randamach).
:param fx: Éifeacht le cur leis an bhfuaim, ceann amháin de na luachanna seo a leanas: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, nó ``FX_NONE``.
:param shape: (cruth) An cineál cuar idirshuíomh idir na minicíochtaí tosaigh agus deiridh, tá cruthanna tonn éagsúla rátaí éagsúla athraithe i minicíocht. Ceann de na luachanna seo a leanas: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Cruthaigh cóip den ``SoundEffect``seo. (cóip)

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Is éard is réad ``AudioFrame`` ann ná liosta de 32 sampla ar beart gan síniú gach ceann acu
(slánuimhir idir 0 agus 255). (fráma fuaime)

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Forscríobh na sonraí sa ``AudioFrame`` seo leis na sonraí ó shampla ``AudioFrame`` eile. (cóipeáil ó)

Example: ``my_frame.copyfrom(source_frame)``

:param other: (eile) ``AudioFrame`` ásc as ar féidir na sonraí a chóipeáil."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...