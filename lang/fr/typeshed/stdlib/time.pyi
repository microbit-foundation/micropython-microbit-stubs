"""Mesurer le temps et ajouter des retards aux programmes."""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """Temporiser d'un certain nombre de secondes.

Example: ``time.sleep(1)``

:param seconds: Le nombre de secondes pendant lesquelles dormir.
Utiliser un nombre à virgule flottante pour dormir pendant un nombre fractionnaire de secondes."""
    ...

def sleep_ms(ms: int) -> None:
    """Temporiser pour un nombre donné de millisecondes.

Example: ``time.sleep_ms(1_000_000)``

:param ms: Le nombre de millisecondes à attendre (>= 0)."""
    ...

def sleep_us(us: int) -> None:
    """Temporiser pour un nombre donné de microsecondes.

Example: ``time.sleep_us(1000)``

:param us: Le nombre de microsecondes à attendre (>= 0)."""
    ...

def ticks_ms() -> int:
    """Obtenir un compteur croissant en millisecondes avec un point de référence arbitraire.
Le compteur revient à zéro après une certaine valeur.

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """Obtenir un compteur croissant en microsecondes avec un point de référence arbitraire.
Le compteur revient à zéro après une certaine valeur.

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """Décaler les ticks par un nombre donné, positif ou négatif.

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: Une valeur de ticks
:param delta: Un entier représentant le décalage

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
    """Mesurer la différence des ticks entre les valeurs retournées par
``time.ticks_ms()`` ou ``ticks_us()``, sous la forme d'une valeur signée
qui peut passer plusieurs fois par zéro.

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: La valeur à partir de laquelle soustraire
:param ticks2: La valeur à soustraire

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