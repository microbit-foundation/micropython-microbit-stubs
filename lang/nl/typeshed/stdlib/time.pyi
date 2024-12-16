"""Meet tijd en voeg vertragingen toe aan programma's. (tijd)"""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """Vertraag een aantal seconden. (slapen)

Example: ``time.sleep(1)``

:param seconds: (seconden) Het aantal seconden om voor te slapen.
Gebruik een floating-point nummer om te slapen voor een fractioneel aantal seconden."""
    ...

def sleep_ms(ms: int) -> None:
    """Vertraging voor een bepaald aantal milliseconden. (slaap ms)

Example: ``time.sleep_ms(1_000_000)``

:param ms: Het aantal milliseconden vertraging (>= 0)."""
    ...

def sleep_us(us: int) -> None:
    """Vertraging voor een bepaald aantal microseconden. (slaap us)

Example: ``time.sleep_us(1000)``

:param us: Het aantal microseconden vertraging (>= 0)."""
    ...

def ticks_ms() -> int:
    """Krijg een toenemende milliseconde teller met een willekeurig referentiepunt, dat omwikkeld na een waarde.

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """Krijg een toenemende milliseconde teller met een willekeurig referentiepunt, dat omwikkeld na een waarde.

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """Waarde van de offset ticks door een bepaald getal, die ofwel positief ofwel
negatief kan zijn. (ticks toevoegen)

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: (tikken) Een ticks waarde
:param delta: Een integer verschuiving

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
    """Meet het verschil in ticks tussen waarden die worden geretourneerd door ``time.ticks_ms()`` of ``ticks_us()``, als een ondertekende waarde die rond kan lopen.

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: De waarde om van af te trekken
:param ticks2: De waarde om af te trekken

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