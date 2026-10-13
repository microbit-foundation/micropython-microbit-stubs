"""Criar e tocar melodias. (música)"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Melodia: a abertura da 5ª Sinfonia de Beethoven em C menor."""
ENTERTAINER: Tuple[str, ...]
"""Melodia: o fragmento inicial do clássico Ragtime de Scott Joplin "The Entertainer"."""
PRELUDE: Tuple[str, ...]
"""Melodia: a abertura do primeiro Prelúdio em Dó Maior das 48 Prelúdios e Fugas de J.S. Bach. (prelúdio)"""
ODE: Tuple[str, ...]
"""Melodia: o tema da "Ode à Alegria" da 9ª Sinfonia de Beethoven em Ré menor."""
NYAN: Tuple[str, ...]
"""Melodia: o tema do Nyan Cat (http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Melodia: algo que soa como um toque de celular. (toque)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Melodia: uma linha de baixo funk para agentes secretos e mestres do crime."""
BLUES: Tuple[str, ...]
"""Melodia: um walking bass de 12 compassos no estilo boogie-woogie."""
BIRTHDAY: Tuple[str, ...]
"""Melodia: "Parabéns pra você..." (aniversário)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melodia: a marcha nupcial da ópera "Lohengrin" de Wagner. (casamento)"""
FUNERAL: Tuple[str, ...]
"""Melodia: a "marcha fúnebre", também conhecida como Sonata para Piano Nº 2 em Si♭ menor, Op. 35, de Frédéric Chopin."""
PUNCHLINE: Tuple[str, ...]
"""Melodia: um fragmento divertido que indica que uma piada foi feita."""
PYTHON: Tuple[str, ...]
"""Melodia: a marcha "Liberty Bell" de John Philip Sousa, também conhecida como o tema de "Monty Python's Flying Circus" (que inspirou o nome da linguagem de programação Python)."""
BADDY: Tuple[str, ...]
"""Melodia: entrada de um vilão da era do cinema mudo. (vilão)"""
CHASE: Tuple[str, ...]
"""Melodia: cena de perseguição da era do cinema mudo. (perseguição)"""
BA_DING: Tuple[str, ...]
"""Melodia: um sinal curto para indicar que algo aconteceu."""
WAWAWAWAA: Tuple[str, ...]
"""Melodia: um trombone muito triste."""
JUMP_UP: Tuple[str, ...]
"""Melodia: para uso em um jogo, indicando movimento ascendente. (pular para cima)"""
JUMP_DOWN: Tuple[str, ...]
"""Melodia: para uso em um jogo, indicando movimento descendente. (pular para baixo)"""
POWER_UP: Tuple[str, ...]
"""Melodia: uma fanfarra para indicar que uma conquista foi desbloqueada. (aumentar a energia)"""
POWER_DOWN: Tuple[str, ...]
"""Melodia: uma fanfarra triste para indicar que uma conquista foi perdida. (reduzir a energia)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Define o tempo aproximado para a reprodução. (definir tempo)

Example: ``music.set_tempo(bpm=120)``

:param ticks: O número de ticks que constituem um batimento.
:param bpm: Um inteiro que determina quantos batimentos por minuto.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Obtém o tempo atual como uma tupla de inteiros: ``(ticks, bpm)``. (obter tempo)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Toca música. (reproduzir)

Example: ``music.play(music.NYAN)``

:param music: (música) música especificada em uma notação especial <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_
:param pin: (alfinete) o pino de saída para uso com um alto-falante externo (padrão ``pin0``), ``None`` para sem som.
:param wait: Se ``wait`` estiver definido como ``True``, esta função é bloqueadora.
:param loop: (laço) Se ``loop`` estiver definido como ``True``, a melodia se repete até que ``stop`` seja chamado ou a chamada bloqueadora seja interrompida.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Tocar uma nota. (inclinação)

Example: ``music.pitch(185, 1000)``

:param frequency: (Frequência) Uma frequência inteira.
:param duration: (duração) Uma duração em milissegundos. Se for negativa, o som será contínuo até a próxima chamada ou uma chamada para ``stop``.
:param pin: (alfinete) Pino de saída opcional (padrão ``pin0``).
:param wait: Se ``wait`` estiver definido como ``True``, esta função é bloqueadora.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Interrompe toda a reprodução de música no alto-falante embutido e em qualquer pino que esteja emitindo som. (parar)

Example: ``music.stop()``

:param pin: (alfinete) Um argumento opcional pode ser fornecido para especificar um pino, por exemplo, ``music.stop(pin1)``."""

def reset() -> None:
    """Redefine os ticks, bpm, duração e oitava para seus valores padrão. (redefinir)

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...