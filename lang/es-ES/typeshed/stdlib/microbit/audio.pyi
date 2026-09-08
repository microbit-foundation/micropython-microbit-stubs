"""Reproducir sonidos usando el micro:bit (importar ``audio`` para compatibilidad con V1)."""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Reproduce un sonido integrado, un efecto de sonido o marcos de audio personalizados. (reproducir)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (origen) Un ``Sound`` integrado como ``Sound.GIGGLE``, un ``SoundEffect`` o datos de muestra como un iterable de objetos ``AudioFrame``.
:param wait: (esperar) Si ``wait`` es ``True`` (verdadero), la función se bloqueará hasta que el sonido finalice.
:param pin: Se puede usar un argumento opcional para especificar el pin de salida, reemplazando el valor predeterminado de ``pin0``. Si no queremos que se reproduzca ningún sonido, podemos usar ``pin=None``.
:param return_pin: (devolver pin) Especifica un pin de conector de borde diferencial para conectarse a un altavoz externo en lugar de tierra. Esto se ignora para la revisión **V2**."""

def is_playing() -> bool:
    """Comprueba si se está reproduciendo un sonido. (reproduciendo)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Detiene la reproducción de audio. (detener)

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Un efecto de sonido, compuesto por un conjunto de parámetros configurados a través del constructor o atributos. (efectosonido)"""
    WAVEFORM_SINE: ClassVar[int]
    """Opción de onda senoidal utilizada para el parámetro ``waveform``. (forma de onda senoidal)"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Opción de onda con diente de sierra usada para el parámetro ``waveform``. (forma de onda diente de sierra)"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """Opción de onda triangular usada para el parámetro ``waveform``. (forma de onda triangular)"""
    WAVEFORM_SQUARE: ClassVar[int]
    """Opción de onda cuadrada usada para el parámetro ``waveform``. (forma de onda cuadrada)"""
    WAVEFORM_NOISE: ClassVar[int]
    """Opción de ruido usada para el parámetro ``waveform``. (forma de onda de ruido)"""
    SHAPE_LINEAR: ClassVar[int]
    """Opción de interpolación lineal usada para el parámetro ``shape``. (forma lineal)"""
    SHAPE_CURVE: ClassVar[int]
    """Opción de interpolación de curva usada para el parámetro ``shape``. (forma curva)"""
    SHAPE_LOG: ClassVar[int]
    """Opción de interpolación logarítmica usada para el parámetro ``shape``. (registro de forma)"""
    FX_NONE: ClassVar[int]
    """Ninguna opción de efecto usada para el parámetro ``fx``. (fx ninguno)"""
    FX_TREMOLO: ClassVar[int]
    """Opción de efecto Trémolo usada para el parámetro ``fx``. (fx trémolo)"""
    FX_VIBRATO: ClassVar[int]
    """Opción de efecto vibrato utilizada para el parámetro ``fx``."""
    FX_WARBLE: ClassVar[int]
    """Opción de efecto gorjeo utilizada para el parámetro ``fx``. (fx gorjeo)"""
    freq_start: int
    """Frecuencia de inicio en Hertz (Hz), un número entre ``0`` y ``9999`` (frecuencia de inicio)"""
    freq_end: int
    """Frecuencia final en Hertz (Hz), un número entre ``0`` y ``9999`` (frecuencia final)"""
    duration: int
    """Duración del sonido en milisegundos, un número entre ``0`` y ``9999`` (duración)"""
    vol_start: int
    """Valor de volumen inicial, un número entre ``0`` y ``255`` (volumen de inicio)"""
    vol_end: int
    """Valor final del volumen, un número entre ``0`` y ``255`` (volumen final)"""
    waveform: int
    """Tipo de forma ondulada, uno de estos valores: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (ruido generado aleatoriamente) (forma de onda)"""
    fx: int
    """Efecto para añadir en el sonido, uno de los siguientes valores: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``o ``FX_NONE``"""
    shape: int
    """El tipo de curva de interpolación entre las frecuencias de inicio y final, diferentes formas de onda tienen diferentes tasas de cambio en la frecuencia. Uno de los siguientes valores: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG`` (forma)"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Crea un nuevo efecto de sonido.

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: (frecuencia de inicio) Frecuencia de inicio en Hertz (Hz), un número entre ``0`` y ``9999``.
:param freq_end: (frecuencia final) Frecuencia final en Hertz (Hz), un número entre ``0`` y ``9999``.
:param duration: (duración) Duración del sonido en milisegundos, un número entre ``0`` y ``9999``.
:param vol_start: (volumen inicial) Valor de volumen inicial, un número entre ``0`` y ``255``.
:param vol_end: (volumen final) Valor de volumen final, un número entre ``0`` y ``255``.
:param waveform: (forma de onda) Tipo de forma de onda, uno de estos valores: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (ruido generado aleatoriamente).
:param fx: Efecto para añadir en el sonido, uno de los siguientes valores: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``o ``FX_NONE``.
:param shape: (forma) El tipo de curva de interpolación entre las frecuencias de inicio y final, diferentes formas de onda tienen diferentes tasas de cambio en la frecuencia. Uno de los siguientes valores: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Crea una copia de este ``SoundEffect``. (copiar)

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Un objeto ``AudioFrame`` es una lista de 32 muestras, cada una de las cuales es un byte
sin signo (número entero entre 0 y 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Sobrescribe los datos de este ``AudioFrame`` con los datos de otra instancia ``AudioFrame``. (copiadesde)

Example: ``my_frame.copyfrom(source_frame)``

:param other: (otro) Instancia ``AudioFrame`` desde la que copiar los datos."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...