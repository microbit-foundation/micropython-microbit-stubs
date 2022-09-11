"""時間の測定とプログラムの遅延。"""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """指定した秒数だけ遅延します。

Example: ``time.sleep(1)``

:param seconds: スリープする秒数。
秒より細かい精度で指定したい場合は浮動小数点数を使ってください。"""
    ...

def sleep_ms(ms: int) -> None:
    """指定したミリ秒だけ遅延します。

Example: ``time.sleep_ms(1_000_000)``

:param ms: 遅延するミリ秒数（>= 0）。"""
    ...

def sleep_us(us: int) -> None:
    """指定したマイクロ秒だけ遅延します。

Example: ``time.sleep_us(1000)``

:param us: 遅延するマイクロ秒数（>= 0）。"""
    ...

def ticks_ms() -> int:
    """呼出し時点での稼働時間をミリ秒単位で取得します。稼働時間は最大値に達するとラップアラウンドします。

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """呼出し時点での稼働時間をマイクロ秒単位で取得します。稼働時間は最大値に達するとラップアラウンドします。

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """与えた数をティック値からのオフセットとして加算した値を返します。引数の値は正でも負でもかまいません。

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: ティック値
:param delta: 整数オフセット

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
    """``time.ticks_ms()`` や ``ticks_us()`` 関数の戻り値（ラップアラウンドする可能性のある符号付きの値）の間のティック値の差を計算します。

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: 引かられる方の値
:param ticks2: 引く方の値

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