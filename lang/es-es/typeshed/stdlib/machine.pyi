"""Utilidades de bajo nivel. (máquina)"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """Obtiene una cadena de bytes con un identificador único de una placa. (id único)

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """Restablece el dispositivo de una forma similar a pulsar el botón externo RESET. (restablecer)

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """Obtiene la frecuencia de la CPU en hercios. (frec)

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """Desactiva las solicitudes de interrupción. (desactivar irq)

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """Reactiva las solicitudes de interrupción. (activar irq)

Example: ``machine.enable_irq(interrupt_state)``

:param state: (estado) Valor devuelto por la llamada más reciente a la función ``disable_irq``."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """Cronometra el estado de un pin. (cronometrar estado us)

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: Pin a usar
:param pulse_level: (nivel de estado) 0 para cronometrar un estado bajo o 1 para un estado alto
:param timeout_us: (tiempo de espera us) Tiempo de espera en microsegundos
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """Clase para las vistas de memoria ``mem8``, ``mem16`` y ``mem32``."""

    def __getitem__(self, address: int) -> int:
        """Accede a un valor de la memoria. (obtener elemento)

:param address: (dirección) La dirección de memoria.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """Establece un valor en la dirección dada. (configurar elemento)

:param address: (dirección) La dirección de memoria.
:param value: (valor) El valor entero a establecer."""
        ...
mem8: mem
"""Vista de memoria de 8 bits (byte)."""
mem16: mem
"""Vista de memoria de 16 bits."""
mem32: mem
"""Vista de memoria de 32 bits."""