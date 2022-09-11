"""Reproducir sonidos usando el micro:bit (importar ``audio`` para compatibilidad con V1)."""
from ..microbit import MicroBitDigitalPin, Sound, pin0
from typing import Iterable, Union

def play(source: Union[Iterable[AudioFrame], Sound], wait: bool=True, pin: MicroBitDigitalPin=pin0, return_pin: Union[MicroBitDigitalPin, None]=None) -> None:
    """Reproduce un sonido predefinido o pistas de audio personalizadas. (reproducir)

Example: ``audio.play(Sound.GIGGLE)``

:param source: (origen) Un ``Sound`` predefinido como ``Sound.GIGGLE`` o datos de muestra como un iterable de objetos ``AudioFrame``.
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

class AudioFrame:
    """Un objeto ``AudioFrame`` es una lista de 32 muestras, cada una de las cuales es un byte
sin signo (número entero entre 0 y 255).

It takes just over 4 ms to play a single frame.

Example::

    frame = AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8"""

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: int, value: int) -> None:
        ...

    def __getitem__(self, key: int) -> int:
        ...