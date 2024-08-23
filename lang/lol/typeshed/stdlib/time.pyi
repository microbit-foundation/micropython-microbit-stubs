"""crwdns331124:0crwdne331124:0 (crwdns331122:0crwdne331122:0)"""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """crwdns331128:0crwdne331128:0 (crwdns331126:0crwdne331126:0)

Example: ``time.sleep(1)``

:param seconds: (crwdns331130:0crwdne331130:0) crwdns331132:0crwdne331132:0"""
    ...

def sleep_ms(ms: int) -> None:
    """crwdns331136:0crwdne331136:0 (crwdns331134:0crwdne331134:0)

Example: ``time.sleep_ms(1_000_000)``

:param ms: (crwdns331138:0crwdne331138:0) crwdns331140:0crwdne331140:0"""
    ...

def sleep_us(us: int) -> None:
    """crwdns331144:0crwdne331144:0 (crwdns331142:0crwdne331142:0)

Example: ``time.sleep_us(1000)``

:param us: (crwdns331146:0crwdne331146:0) crwdns331148:0crwdne331148:0"""
    ...

def ticks_ms() -> int:
    """crwdns331152:0crwdne331152:0 (crwdns331150:0crwdne331150:0)

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """crwdns331156:0crwdne331156:0 (crwdns331154:0crwdne331154:0)

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """crwdns331160:0crwdne331160:0 (crwdns331158:0crwdne331158:0)

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: (crwdns331166:0crwdne331166:0) crwdns331168:0crwdne331168:0
:param delta: (crwdns331162:0crwdne331162:0) crwdns331164:0crwdne331164:0

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
    """crwdns331172:0``time.ticks_ms()``crwdnd331172:0``ticks_us()``crwdne331172:0 (crwdns331170:0crwdne331170:0)

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: (crwdns331174:0crwdne331174:0) crwdns331176:0crwdne331176:0
:param ticks2: (crwdns331178:0crwdne331178:0) crwdns331180:0crwdne331180:0

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