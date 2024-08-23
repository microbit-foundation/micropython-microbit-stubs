"""Zmierz czas i dodaj opóźnienia do programów."""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """Opóźnij kilka sekund.

Example: ``time.sleep(1)``

:param seconds: Liczba sekund snu.
Użyj liczby zmiennopozycyjnej, aby spać przez ułamkową część sekund."""
    ...

def sleep_ms(ms: int) -> None:
    """Opóźnij o podaną liczbę milisekund.

Example: ``time.sleep_ms(1_000_000)``

:param ms: Liczba milisekund opóźnienia (>= 0)."""
    ...

def sleep_us(us: int) -> None:
    """Opóźnij o podaną liczbę milisekund.

Example: ``time.sleep_us(1000)``

:param us: Liczba milisekund opóźnienia (>= 0)."""
    ...

def ticks_ms() -> int:
    """Uzyskaj rosnący licznik milisekundowy z dowolnym punktem odniesienia,
który zawija się po pewnej wartości.

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """Uzyskaj rosnący licznik milisekundowy z dowolnym punktem odniesienia,
który zawija się po pewnej wartości.

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """Przesunięcie zaznacza wartość o podaną liczbę, która może być dodatnia lub
negatywny.
.

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: Wartość ticków
:param delta: Przesunięcie o liczbę całkowitą

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
    """Zmierz różnicę ticków między wartościami zwróconymi z
``time.ticks_ms()`` lub ``ticks_us()``, jako wartość ze znakiem, 
która może się zawijać.

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: Wartość do odejmowania od
:param ticks2: Wartość do odejmowania

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