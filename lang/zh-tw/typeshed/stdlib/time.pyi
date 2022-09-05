"""測量時間並為程式增加延遲。 (時間)"""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """延遲秒數。 (睡眠)

Example: ``time.sleep(1)``

:param seconds: (秒) 睡眠的秒數。
使用浮點數代替分數來計算秒數。"""
    ...

def sleep_ms(ms: int) -> None:
    """延遲指定的毫秒數。 (睡眠 ms)

Example: ``time.sleep_ms(1_000_000)``

:param ms: (ms) 延遲的毫秒數 (>= 0)。"""
    ...

def sleep_us(us: int) -> None:
    """延遲指定的微秒數。 (睡眠 us)

Example: ``time.sleep_us(1000)``

:param us: (us) 延遲的微秒數 (>= 0)。"""
    ...

def ticks_ms() -> int:
    """取得具有任意參考點的遞增毫秒計數器，該計數器會在某個值之後繞回。 (tick ms)

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """取得具有任意參考點的遞增微秒計數器，該計數器會在某個值之後繞回。 (tick us)

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """特定數字的偏移 tick 值，可以是正數或負數。 (ticks add)

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: (ticks) A ticks value
:param delta: (delta) 整數偏移量

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
    """測量從 ``time.ticks_ms()`` 或 ``ticks_us()`` 返回值之間的 tick 差異，有符號值
可能會繞回。 (tick diff)

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: (tick 1) 要減去的值
:param ticks2: (tick 2) 要減去的值

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