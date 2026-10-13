"""Medir o tempo e adicionar atrasos aos programas. (tempo)"""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """Atrasar por um número de segundos. (dormir)

Example: ``time.sleep(1)``

:param seconds: (segundos) O número de segundos para pausar.  
Use um número de ponto flutuante para pausar por um número fracionário de segundos."""
    ...

def sleep_ms(ms: int) -> None:
    """Atrasar pelo número especificado de milissegundos. (pausar em ms)

Example: ``time.sleep_ms(1_000_000)``

:param ms: O número de milissegundos de atraso (>= 0)."""
    ...

def sleep_us(us: int) -> None:
    """Atrasar pelo número especificado de microssegundos. (pausar em us)

Example: ``time.sleep_us(1000)``

:param us: O número de microssegundos de atraso (>= 0)."""
    ...

def ticks_ms() -> int:
    """Obter um contador de milissegundos crescente com um ponto de referência arbitrário, que se reinicia após um determinado valor.

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """Obter um contador de microssegundos crescente com um ponto de referência arbitrário, que se reinicia após um determinado valor.

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """Deslocar o valor de ticks por um número dado, que pode ser positivo ou negativo. (adicionar ticks)

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: Um valor de ticks.
:param delta: Um deslocamento inteiro.

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
    """Medir a diferença de ticks entre os valores retornados por ``time.ticks_ms()`` ou ``ticks_us()``, como um valor com sinal que pode se reiniciar.

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: O valor a ser subtraído.
:param ticks2: O valor a ser subtraído.

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