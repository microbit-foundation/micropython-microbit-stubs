"""Crear y reproducir melodías. (música)"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Melodía: apertura de la "Sinfonía n.º 5 en do menor" de Beethoven."""
ENTERTAINER: Tuple[str, ...]
"""Melodía: fragmento inicial del clásico Ragtime de Scott Joplin “The Entertainer”."""
PRELUDE: Tuple[str, ...]
"""Melodía: apertura del primer "Preludio en do mayor" de los 48 Preludios y Fugas de J. S. Bach. (preludio)"""
ODE: Tuple[str, ...]
"""Melodía: tema “Oda a la alegría” de la "Sinfonía n.º 9 en re menor" de Beethoven. (oda)"""
NYAN: Tuple[str, ...]
"""Melodía: el tema de Nyan Cat (http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Melodía: algo que suena como un tono de llamada de un teléfono móvil. (tono de llamada)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Melodía: una línea de bajo funky para agentes secretos y maestros criminales."""
BLUES: Tuple[str, ...]
"""Melodía: "walking bass" con un blues boogie-woogie de 12 compases."""
BIRTHDAY: Tuple[str, ...]
"""Melodía: “Cumpleaños feliz” (cumpleaños)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Melodía: coro nupcial de la ópera de Wagner "Lohengrin". (boda)"""
FUNERAL: Tuple[str, ...]
"""Melodía: “Marcha fúnebre”, conocida también como "Sonata para piano n.º 2 en si bemol menor, Op. 35" de Frédéric Chopin."""
PUNCHLINE: Tuple[str, ...]
"""Melodía: un fragmento divertido que representa que se ha hecho un chiste. (remate)"""
PYTHON: Tuple[str, ...]
"""Melodía: la marcha de John Philip Sousa “Liberty Bell”, también conocida por ser el tema del “Monty Python Flying Circus” (de donde obtiene su nombre el lenguaje de programación Python)."""
BADDY: Tuple[str, ...]
"""Melodía: entrada de un malote en la época del cine mudo. (malote)"""
CHASE: Tuple[str, ...]
"""Melodía: escena de persecución en la época del cine mudo. (persecución)"""
BA_DING: Tuple[str, ...]
"""Melodía: una señal corta para indicar que algo ha pasado."""
WAWAWAWAA: Tuple[str, ...]
"""Melodía: un trombón muy triste."""
JUMP_UP: Tuple[str, ...]
"""Melodía: para usar en un juego, indicando un movimiento ascendente. (saltar arriba)"""
JUMP_DOWN: Tuple[str, ...]
"""Melodía: para usar en un juego, indicando un movimiento descendente. (saltar abajo)"""
POWER_UP: Tuple[str, ...]
"""Melodía: una fanfarria para indicar un logro desbloqueado. (subida de potencia)"""
POWER_DOWN: Tuple[str, ...]
"""Melodía: una fanfarria triste para indicar un logro perdido. (bajada de potencia)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Establece el ritmo aproximado de la reproducción. (configurar tempo)

Example: ``music.set_tempo(bpm=120)``

:param ticks: (tics) El número de tics que constituyen un ritmo.
:param bpm: Un entero que determina el número de compases por minuto.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Obtiene el ritmo actual como una tupla de enteros: ``(ticks, bpm)``. (obtener tempo)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Reproduce música. (reproducir)

Example: ``music.play(music.NYAN)``

:param music: (música) música especificada en `una notación especial <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>`_
:param pin: pin de salida para usar con un altavoz externo (por defecto ``pin0``), ``None`` para que no haya sonido.
:param wait: (esperar) Si ``wait`` se configura como ``True`` (verdadero), esta función estará bloqueando.
:param loop: (bucle) Si ``loop`` se configura como ``True`` (verdadero), la melodía se repite hasta que se llama a ``stop`` o se interrumpe la llamada de bloqueo.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Reproduce una nota. (tono)

Example: ``music.pitch(185, 1000)``

:param frequency: (frecuencia) Una frecuencia entera
:param duration: (duración) La duración en milisegundos. Si es negativa, el sonido continuará hasta la siguiente llamada o una llamada a ``stop``.
:param pin: Pin de salida opcional (por defecto, ``pin0``).
:param wait: (esperar) Si ``wait`` se configura como ``True`` (verdadero), esta función estará bloqueando.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Detiene la reproducción de toda la música en el altavoz integrado y en cualquier pin que esté emitiendo sonido. (detener)

Example: ``music.stop()``

:param pin: Se puede proporcionar un argumento opcional para especificar un pin; por ejemplo, ``music.stop(pin1)``."""

def reset() -> None:
    """Restablece los valores de "ticks", "bpm", "duration" y "octave" a sus valores por defecto. (restablecer)

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...