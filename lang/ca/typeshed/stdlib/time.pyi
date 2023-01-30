"""Mesura el temps i afegeix retards als programes. (temps)"""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """Retarda uns segons. (dormir)

Example: ``time.sleep(1)``

:param seconds: (segons) El nombre de segons per posar en pausa.
Utilitza un nombre de coma flotant per posar en pausa durant una fracció de segons."""
    ...

def sleep_ms(ms: int) -> None:
    """Retard per a un nombre determinat de mil·lisegons. (retard en mil·lisegons)

Example: ``time.sleep_ms(1_000_000)``

:param ms: El nombre de mil·lisegons de retard (>= 0)."""
    ...

def sleep_us(us: int) -> None:
    """Retard per a un nombre determinat de microsegons.

Example: ``time.sleep_us(1000)``

:param us: El nombre de microsegons de retard (>= 0)."""
    ...

def ticks_ms() -> int:
    """Obté un comptador creixent de mil·lisegons amb un punt de referència arbitrari,
que es desborda després d'algun valor. (tics mil·lisegons)

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """Obté un comptador creixent de microsegons amb un punt de referència arbitrari,
que es desborda després d'algun valor. (tics microsegons)

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """Afegeix al valor de tics un desplaçament determinat, que pot ser positiu o
negatiu. (tics compensa)

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: Un valor de tics
:param delta: Un desplaçament enter

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
    """Mesura la diferència dels tics entre els valors retornats
``time.ticks_ms()`` o ``ticks_us()``, com a valor amb signe
que pot desbordar-se.

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: El valor a restar de
:param ticks2: El valor a restar

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