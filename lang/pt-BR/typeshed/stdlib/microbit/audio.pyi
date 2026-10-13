"""Reproduzir sons usando o micro:bit (importe ``audio`` para compatibilidade V1). (áudio)"""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import ClassVar, Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound, SoundEffect], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Reproduza um som embutido, efeito de som ou quadros de áudio personalizados. (reproduzir)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (fonte) Um ``Sound`` embutido, como o ``Sound.GIGGLE``, um ``SoundEffect`` ou dados de amostra como um iterável de objetos ``AudioFrame``.
:param wait: Se ``wait`` for ``True``, esta função irá bloquear até que o som esteja completo.
:param pin: (alfinete) Um argumento opcional para especificar o pino de saída pode ser usado para substituir o padrão do ``pin0``. Se não queremos que nenhum som reproduza, nós podemos usar ``pin=None``.
:param return_pin: (Pino de retorno) Especifica um pino de conector de aresta diferencial para se conectar a um alto-falante externo em vez de solo. Isto é ignorado para a revisão **V2**."""

def is_playing() -> bool:
    """Verifique se um som está tocando. (Está tocando)

Example: ``audio.is_playing()``

:return: ``True`` if audio is playing, otherwise ``False``."""
    ...

def stop() -> None:
    """Parar reprodução de áudio. (parar)

Example: ``audio.stop()``"""
    ...

class SoundEffect:
    """Um efeito sonoro, composto por um conjunto de parâmetros configurados através do construtor ou atributos. (Efeito sonoro)"""
    WAVEFORM_SINE: ClassVar[int]
    """Opção de onda senoidal usada para o parâmetro ``waveform``. (Forma de onda senoidal)"""
    WAVEFORM_SAWTOOTH: ClassVar[int]
    """Opção de onda dente de serra usada para o parâmetro ``waveform``. (onda dente de serra)"""
    WAVEFORM_TRIANGLE: ClassVar[int]
    """Opção de onda triangular usada para o parâmetro ``waveform``. (onda triangular)"""
    WAVEFORM_SQUARE: ClassVar[int]
    """Opção de onda quadrada usada para o parâmetro ``waveform``. (onda quadrada)"""
    WAVEFORM_NOISE: ClassVar[int]
    """Opção de ruído usada para o parâmetro ``waveform``. (onda de ruído)"""
    SHAPE_LINEAR: ClassVar[int]
    """Opção de interpolação linear usada para o parâmetro ``shape``. (forma linear)"""
    SHAPE_CURVE: ClassVar[int]
    """Opção de interpolação curva usada para o parâmetro ``shape``. (forma curva)"""
    SHAPE_LOG: ClassVar[int]
    """Opção de interpolação logarítmica usada para o parâmetro ``shape``. (forma logarítmica)"""
    FX_NONE: ClassVar[int]
    """Opção sem efeito usada para o parâmetro ``fx``. (fx nenhum)"""
    FX_TREMOLO: ClassVar[int]
    """Opção de efeito tremolo usada para o parâmetro ``fx``."""
    FX_VIBRATO: ClassVar[int]
    """Opção de efeito vibrato usada para o parâmetro ``fx``."""
    FX_WARBLE: ClassVar[int]
    """Opção de efeito de trêmulo usada para o parâmetro ``fx``. (fx passivo)"""
    freq_start: int
    """Frequência inicial em Hertz (Hz), um número entre ``0`` e ``9999`` (incio freq)"""
    freq_end: int
    """Frequência final em Hertz (Hz), um número entre ``0`` e ``9999``. (freq final)"""
    duration: int
    """Duração do som em milissegundos, um número entre ``0`` e ``9999``. (duração)"""
    vol_start: int
    """Valor do volume inicial, um número entre ``0`` e ``255``. (vol inicial)"""
    vol_end: int
    """Valor do volume final, um número entre ``0`` e ``255``. (vol final)"""
    waveform: int
    """Tipo de forma de onda, um destes valores: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (ruído gerado aleatoriamente). (forma de onda)"""
    fx: int
    """Efeito a ser adicionado ao som, um dos seguintes valores: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE`` ou ``FX_NONE``."""
    shape: int
    """O tipo da curva de interpolação entre as frequências inicial e final; diferentes formas de onda têm diferentes taxas de mudança na frequência. Um dos seguintes valores: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG`` (forma)"""

    def __init__(self, freq_start: int=500, freq_end: int=2500, duration: int=500, vol_start: int=255, vol_end: int=0, waveform: int=WAVEFORM_SQUARE, fx: int=FX_NONE, shape: int=SHAPE_LOG):
        """Criar um novo efeito sonoro. (iniciar)

Example: ``my_effect = SoundEffect(duration=1000)``

All the parameters are optional, with default values as shown above, and
they can all be modified via attributes of the same name. For example, we
can first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attributes ``my_effect.duration = 500``.

:param freq_start: (incio freq) Frequência inicial em Hertz (Hz), um número entre ``0`` e ``9999``.
:param freq_end: (freq final) Frequência final em Hertz (Hz), um número entre ``0`` e ``9999``.
:param duration: (duração) Duração do som em milissegundos, um número entre ``0`` e ``9999``.
:param vol_start: (vol inicial) Valor do volume inicial, um número entre ``0`` e ``255``.
:param vol_end: (vol final) Valor do volume final, um número entre ``0`` e ``255``.
:param waveform: (forma de onda) Tipo de forma de onda, um dos seguintes valores: ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (ruído gerado aleatoriamente).
:param fx: Efeito a ser adicionado ao som, um dos seguintes valores: ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE`` ou ``FX_NONE``.
:param shape: (forma) O tipo da curva de interpolação entre as frequências inicial e final; diferentes formas de onda têm diferentes taxas de mudança na frequência. Um dos seguintes valores: ``SHAPE_LINEAR``, ``SHAPE_CURVE``, ``SHAPE_LOG``."""

    def copy(self) -> SoundEffect:
        """Criar uma cópia deste ``SoundEffect``. (Copiar)

Example: ``sound_2 = sound_1.copy()``

:return: A copy of the SoundEffect."""

class AudioFrame:
    """Um objeto de ``AudioFrame`` é uma lista de 32 amostras cada uma das quais é um ‘byte’
não assinado (número inteiro entre 0 e 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def copyfrom(self, other: AudioFrame) -> None:
        """Substituir os dados neste ``AudioFrame`` com os dados de outra instância do ``AudioFrame``. (Cópia de)

Example: ``my_frame.copyfrom(source_frame)``

:param other: (outro) Instância ``AudioFrame`` de onde copiar os dados."""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...