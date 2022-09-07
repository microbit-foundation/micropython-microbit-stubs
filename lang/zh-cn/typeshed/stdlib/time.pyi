"""测量时间并给程序添加延迟。 (时间)"""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """延迟几秒钟。 (休眠)

Example: ``time.sleep(1)``

:param seconds: (seconds) 休眠的秒数。
使用浮点数休眠小数秒数。"""
    ...

def sleep_ms(ms: int) -> None:
    """延迟给定的毫秒数。 (休眠延迟以毫秒计算)

Example: ``time.sleep_ms(1_000_000)``

:param ms: (毫秒) 延迟的毫秒数 (>= 0)。"""
    ...

def sleep_us(us: int) -> None:
    """延迟给定的微秒数。 (休眠延迟以微秒计算)

Example: ``time.sleep_us(1000)``

:param us: (微秒) 延迟的微秒数 (>= 0)。"""
    ...

def ticks_ms() -> int:
    """获取一个具有任意参考点、递增的毫秒级计数器，该计数器在某个值之后能够绕回。 (毫秒级刻度)

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """获取一个具有任意参考点、递增的微秒级计数器，该计数器在某个值之后能够绕回。 (微秒级刻度)

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """给定数字的偏移刻度值，可以是正数或负数。 (增加刻度)

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: (刻度) 一个刻度值
:param delta: (delta) 整数偏移量

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
    """测量函数``time.ticks_ms()``或者函数``ticks_us()``返回值之间的刻度差。本参数为一个有可能绕回的带符号数值。 (刻度差)

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: (刻度1) 要被减的值
:param ticks2: (刻度2) 要减去的值

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