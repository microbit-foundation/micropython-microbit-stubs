"""Odtwarzaj dźwięki za pomocą micro:bita (importuj ``audio`` dla kompatybilności V1)."""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Odtwórz wbudowany dźwięk, efekt dźwiękowy lub niestandardowe ramki audio.

Example: ``audio.play(Sound.GIGGLE)``

:param source: Wbudowany ``Sound``, taki jak ``Sound.GIGGLE``, ``SoundEffect`` lub przykładowe dane jako iteracja obiektów ``AudioFrame``.
:param wait: Jeśli ``wait`` jest ``True``, ta funkcja będzie blokować, aż dźwięk zostanie zakończony.
:param pin: Opcjonalny argument do określenia pinu wyjściowego może być użyty do nadpisania domyślnej wartości ``pin0``. Jeśli nie chcemy, aby żaden dźwięk nie był odtwarzany, możemy użyć ``pin=None``.
:param return_pin: Określa pin łącznika różnicowego, aby podłączyć płytkę do zewnętrznego głośnika zamiast do ziemi. Jest to ignorowane dla **V2**."""

def is_playing() -> bool:
    """Sprawdź, czy dźwięk jest odtwarzany.

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Zatrzymaj odtwarzania audio.

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Efekt dźwiękowy, utworzony przez zestaw parametrów skonfigurowanych za pomocą konstruktora lub atrybutów."""
    WAVEFORM_SINE: ClassVar[int]
    """Opcja sinusoidalnej fali używana dla parametru ``waveform``."""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Opcja fali piłokształtnej używana dla parametru ``waveform``."""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """Opcja fali trójkątnej używana dla parametru ``waveform``."""
    WAVEFORM_SQUARE: ClassVar[int]
    """Opcja fali kwadratowj używana dla parametru ``waveform``."""
    WAVEFORM_NOISE: ClassVar[int]
    """Opcja szumu używana dla parametru ``waveform``."""
    SHAPE_LINEAR: ClassVar[int]
    """Opcja interpolacji liniowej używana dla parametru ``shape``."""
    SHAPE_CURVE: ClassVar[int]
    """Opcja interpolacji krzywej używana dla parametru ``shape``."""
    SHAPE_LOG: ClassVar[int]
    """Opcja interpolacji logarytmicznej używana dla parametru ``shape``."""
    FX_NONE: ClassVar[int]
    """Opcja braku efektu użyta dla parametru ``fx``."""
    FX_TREMOLO: ClassVar[int]
    """Opcja efektu Tremelo użyta dla parametru ``fx``."""
    FX_VIBRATO: ClassVar[int]
    """Opcja efektu Vibrato użyta dla parametru ``fx``."""
    FX_WARBLE: ClassVar[int]
    """Opcja efektu Warble użyta dla parametru ``fx``."""
    freq_start: int
    """Częstotliwość początkowa w hercach (Hz), liczba między ``0`` i ``9999``"""
    freq_end: int
    """Częstotliwość końcowa w hercach (Hz), liczba między ``0`` i ``9999``"""
    duration: int
    """Czas trwania dźwięku w milisekundach, liczba pomiędzy ``0`` i ``9999``"""
    vol_start: int
    """Wartość głośności początkowej, liczba między ``0`` i ``255``"""
    vol_end: int
    """Wartość głośności końcowej, liczba między ``0`` i ``255``"""
    waveform: int
    """Rodzaj kształtu fali, jedna z tych wartości:``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (losowo generowany szum)"""
    fx: int
    """Efekt do dodania do dźwięku, jedna z następujących wartości: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE`` lub ``FX_NONE``"""
    shape: int
    """Rodzaj krzywej interpolacji między częstotliwością początkową i końcową, różne kształty fal mają różne szybkości zmian częstotliwości. Jedna z następujących wartości: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Utwórz nowy efekt dźwiękowy.

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: Częstotliwość początkowa w hercach (Hz), liczba między ``0`` i ``9999``.
:param freq_end: Częstotliwość końcowa w hercach (Hz), liczba między ``0`` i ``9999``.
:param duration: Czas trwania dźwięku w milisekundach, liczba między ``0`` i ``9999``.
:param vol_start: Początkowa wartość głośności, liczba pomiędzy ``0`` i ``255``.
:param vol_end: Końcowa wartość głośności, liczba pomiędzy ``0`` i ``255``.
:param waveform: Rodzaj kształtu fali, jedna z tych wartości: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (losowo generowany szum).
:param fx: Efekt do dodania do dźwięku, jedna z następujących wartości: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE`` lub ``FX_NONE``.
:param shape: Rodzaj krzywej interpolacji między częstotliwością początkową i końcową, różne kształty fal mają różne szybkości zmian częstotliwości. Jedna z następujących wartości: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Utwórz kopię ``SoundEffect``.

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Obiekt ``AudioFrame`` jest listą 32 próbek, z których każda jest niepodpisanym bajtem (liczba całkowita między 0 a 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Zastąp dane w tym ``AudioFrame`` danymi z innej instancji ``AudioFrame``.

Example: ``my_frame.copyfrom(source_frame)``

:param other: Instancja ``AudioFrame``, z której skopiowane są dane."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...