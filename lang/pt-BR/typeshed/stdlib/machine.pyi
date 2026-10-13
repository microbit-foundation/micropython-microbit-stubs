"""Serviços de Baixo Nível. (máquina)"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Obter um byte string com um identificador exclusivo de um board. (id único)

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Redefina o dispositivo de uma maneira semelhante ao botão RESET externo. (redefinir)

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Obtenha a frequência da CPU em hertz. (Freq:)

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Desativar solicitações de interrupção. (desativar irq)

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Reativar requisições de interrupção. (habilitar irq)

Example: ``machine.enable_irq(interrupt_state)``

:param state: (estado) O valor que foi retornado da chamada mais recente para a função ``disable_irq``."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Tempo de pulso em um pino. (tempo do pulso)

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: (alfinete) O pino a ser usado
:param pulse_level: (nível de pulso) 0 para usar um pulso baixo ou 1 para usar um pulso alto
:param timeout_us: (limite de tempo) tempo limite em microssegundos
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """A classe para as visualizações de memória ``mem8``, ``mem16`` e ``mem32``."""

    def __getitem__(self, address: int) -> int:
        """Acesso a um valor da memória. (obter item)

:param address: (Endereço) O endereço da memória.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Define um valor no endereço fornecido. (definir item)

:param address: (Endereço) O endereço da memória.
:param value: (Valor) O valor inteiro a ser definido."""
        ...
mem8: mem
"""Visualização de 8-bit (byte) da memória."""
mem16: mem
"""Visualização de 16-bit (byte) da memória."""
mem32: mem
"""Visão 32-bit da memória."""