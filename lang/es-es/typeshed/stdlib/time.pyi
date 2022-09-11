"""Mide el tiempo y añade retardos a los programas. (tiempo)"""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """Retarda varios segundos. (dormir)

Example: ``time.sleep(1)``

:param seconds: (segundos) El número de segundos de retardo.
Usa un número de coma flotante para generar un retardo durante un número fraccional de segundos."""
    ...

def sleep_ms(ms: int) -> None:
    """Genera un retardo para el número dado de milisegundos. (dormir ms)

Example: ``time.sleep_ms(1_000_000)``

:param ms: El número de milisegundos de retardo (>= 0)."""
    ...

def sleep_us(us: int) -> None:
    """Genera un retardo para el número dado de microsegundos. (dormir us)

Example: ``time.sleep_us(1000)``

:param us: El número de microsegundos de retardo (>= 0)."""
    ...

def ticks_ms() -> int:
    """Obtiene un contador en milisegundos creciente con un punto de referencia arbitrario que se reinicia después de algún valor. (tics ms)

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """Obtiene un contador en microsegundos creciente con un punto de referencia arbitrario que se reinicia después de algún valor. (tics us)

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """Valor de desplazamiento de tics por un número determinado, el cual puede ser positivo o
negativo. (añadir tics)

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: (tics) Un valor de tics
:param delta: Un desplazamiento entero

Example::

    # Find out what ticks value there was 100ms ago
    print(ticks_add(time.ticks_ms(), -100))

    # Calculate deadline for operation and test for it
    deadline = ticks_add(time.ticks_ms(), 200)
    while ticks_diff(deadline, time.ticks_ms()) > 0:
        do_a_little_of_something()

    # Find out TICKS_MAX used by this port
    print(ticks_add(0, -1))"""
    ...

def ticks_diff(ticks1: int, ticks2: int) -> int:
    """Mide la diferencia de tics entre los valores devueltos por ``time.ticks_ms()`` o ``ticks_us()`` como un valor con signo que se puede reiniciar. (diferencia de tics)

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: (tics1) El valor del que restar
:param ticks2: (tics2) El valor a restar

The argument order is the same as for subtraction operator,
``ticks_diff(ticks1, ticks2)`` has the same meaning as ``ticks1 - ticks2``.

``ticks_diff()`` is designed to accommodate various usage
patterns, among them:

Polling with timeout. In this case, the order of events is known, and you
will deal only with positive results of :func:`time.ticks_diff()`::

    # Wait for GPIO pin to be asserted, but at most 500us
    start = time.ticks_us()
    while pin.value() == 0:
        if time.ticks_diff(time.ticks_us(), start) > 500:
            raise TimeoutError


Scheduling events. In this case, :func:`time.ticks_diff()` result may be
negative if an event is overdue::

    # This code snippet is not optimized
    now = time.ticks_ms()
    scheduled_time = task.scheduled_time()
    if ticks_diff(scheduled_time, now) > 0:
        print("Too early, let's nap")
        sleep_ms(ticks_diff(scheduled_time, now))
        task.run()
    elif ticks_diff(scheduled_time, now) == 0:
        print("Right at time!")
        task.run()
    elif ticks_diff(scheduled_time, now) < 0:
        print("Oops, running late, tell task to run faster!")
        task.run(run_faster=True)"""
    ...