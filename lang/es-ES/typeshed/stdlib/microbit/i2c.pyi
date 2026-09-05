"""Comunicarse con dispositivos que usan el protocolo de bus I²C."""
from _typeshed import ReadableBuffer
from ..microbit import MicroBitDigitalPin, pin19, pin20
from typing import List

def init(freq: int=100000, sda: MicroBitDigitalPin=pin20, scl: MicroBitDigitalPin=pin19) -> None:
    """Reinicia un periférico. (inic)

Example: ``i2c.init()``

:param freq: (frec) frecuencia del reloj
:param sda: pin ``sda`` (por defecto, 20)
:param scl: pin ``scl`` (por defecto, 19)

On a micro:bit V1 board, changing the I²C pins from defaults will make
the accelerometer and compass stop working, as they are connected
internally to those pins. This warning does not apply to the **V2**
revision of the micro:bit as this has `separate I²C lines <https://tech.microbit.org/hardware/i2c/>`_
for the motion sensors and the edge connector."""
    ...

def scan() -> List[int]:
    """Escanea el bus para buscar dispositivos. (escanear)

Example: ``i2c.scan()``

:return: A list of 7-bit addresses corresponding to those devices that responded to the scan."""
    ...

def read(addr: int, n: int, repeat: bool=False) -> bytes:
    """Lee bytes de un dispositivo. (leer)

Example: ``i2c.read(0x50, 64)``

:param addr: (dir) La dirección de 7 bits del dispositivo
:param n: El número de bytes a leer
:param repeat: (repetir) Si es ``True`` (verdadero), no se enviará ningún bit de parada
:return: The bytes read"""
    ...

def write(addr: int, buf: ReadableBuffer, repeat: bool=False) -> None:
    """Escribe bytes en un dispositivo. (escribir)

Example: ``i2c.write(0x50, bytes([1, 2, 3]))``

:param addr: (dir) La dirección de 7 bits del dispositivo
:param buf: (búf) Un búfer que contiene los bytes a escribir
:param repeat: (repetir) Si es ``True`` (verdadero), no se enviará ningún bit de parada"""
    ...