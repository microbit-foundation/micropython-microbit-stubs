"""Kommunikation mit Geräten über die serielle Schnittstelle (SPI)."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """SPI-Kommunikation initialisieren.

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: Die Übertragungsgeschwindigkeit.
:param bits: Die Breite in Bits jeder Übertragung. Derzeit wird nur ``bits=8`` unterstützt. Dies kann sich jedoch in Zukunft ändern.
:param mode: Legt die Kombination aus Taktpolarität und Phase fest - `siehe Online-Tabelle <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: SCLK Pin (standardmäßig 13)
:param mosi: MOSI Pin (standardmäßig 15)
:param miso: miso pin (Voreinstellung 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """Bytes lesen.

Example: ``spi.read(64)``

:param nbytes: Maximum der zu lesenden Bytes.
:param out: Wert der zu schreibenden Bytes (Standard 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Schreibt Bytes auf den Bus. (schreiben)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (Puffer) Ein Puffer, von dem Daten gelesen werden."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Schreibe den ``out`` Zwischenspeicher (Buffer) auf den Bus und lies jede Antwort in den ``in_`` Buffer.

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: Der Puffer, in den eine Antwort geschrieben werden soll.
:param in_: Der Puffer, von dem Daten gelesen werden."""
    ...