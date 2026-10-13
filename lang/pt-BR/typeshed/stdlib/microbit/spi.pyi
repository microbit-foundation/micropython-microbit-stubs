"""Comunique-se com dispositivos usando o ônibus de serial de ‘interface’ periférica (SPI)."""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """Inicializar comunicação SPI. (iniciar)

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: (Taxa de transmissão) A velocidade da comunicação.
:param bits: A largura em bits de cada transferência. Atualmente, apenas ``bits=8`` é suportada. No entanto, isto pode mudar no futuro.
:param mode: (modo) Determina a combinação de fase e polaridade do relógio — `ver tabela ‘online’ <https://microbit-micropython.readthedocs.io/en/v2-docs/spi.html#microbit.spi.init>`_.
:param sclk: Pino sclk (padrão 13)
:param mosi: Pino mosi (padrão 15)
:param miso: Pino miso (padrão 14)"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """Leia no máximo ``nbytes`` enquanto escreve continuamente o ‘byte’ dado por ``out``. (ler)

Example: ``spi.read(64)``

:param nbytes: Número máximo de ‘bytes’ para ler.
:param out: O valor do ‘byte’ para escrever (padrão 0).
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """Escrever ‘bytes’ para o ônibus. (escrever)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (Tampão) Uma memória temporária para ler dados dela."""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """Escreva a memória temporária ``out`` no ônibus e leia qualquer resposta para a memória temporária ``in_``. (Escrever e ler)

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: A memória temporária para escrever qualquer resposta.
:param in_: A memória temporária para ler os dados dela."""
    ...