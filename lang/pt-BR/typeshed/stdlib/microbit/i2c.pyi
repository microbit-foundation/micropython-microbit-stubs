"""Comunicar-se com dispositivos usando o protocolo de ônibus I²C."""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """Reinicializar uma periferia. (iniciar)

Example: ``i2c.init()``

:param freq: (Freq:) Frequência de relógio
:param sda: Pino ``sda`` (padrão 20)
:param scl: Pino ``scl`` (padrão 19)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """Escanear o ônibus para dispositivos. (escanear)

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """Ler ‘bytes’ de um dispositivo. (ler)

Example: ``i2c.read(0x50, 64)``

:param addr: O endereço 7 bits do dispositivo
:param n: O número de ‘bytes’ a ler
:param repeat: (Repetir) Se ``True``, nenhum bit de interrupção será enviado
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """Escrever ‘bytes’ para um dispositivo. (escrever)

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: O endereço 7 bits do dispositivo
:param buf: Uma memória temporária contendo os ‘bytes’ para escrever
:param repeat: (Repetir) Se ``True``, nenhum bit de interrupção será enviado"""
    ...