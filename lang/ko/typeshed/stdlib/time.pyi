"""시간을 측정하고 프로그램에 지연을 부여합니다."""
from typing import Union

def sleep(seconds: Union[int, float]) -> None:
    """초 단위로 지연을 부여합니다.

Example: ``time.sleep(1)``

:param seconds: 절전 상태를 설정할 초 단위입니다.
초 단위 미만으로 절전 상태를 설정하려면 부동 소수점 수를 사용하세요."""
    ...

def sleep_ms(ms: int) -> None:
    """밀리초 단위로 지연을 부여합니다.

Example: ``time.sleep_ms(1_000_000)``

:param ms: 밀리초 단위의 지연 시간입니다(>= 0)."""
    ...

def sleep_us(us: int) -> None:
    """마이크로초 단위로 지연을 부여합니다.

Example: ``time.sleep_us(1000)``

:param us: 마이크로초 단위의 지연 시간입니다(>= 0)."""
    ...

def ticks_ms() -> int:
    """임의의 레퍼런스 포인트가 있는 점진적으로 증가하는 밀리초 카운터로, 일부 값을 따라 래핑합니다.

Example: ``time.ticks_ms()``

:return: The counter value in milliseconds."""
    ...

def ticks_us() -> int:
    """임의의 레퍼런스 포인트가 있는 점진적으로 증가하는 마이크로초 카운터로, 일부 값을 따라 래핑합니다.

Example: ``time.ticks_us()``

:return: The counter value in microseconds."""
    ...

def ticks_add(ticks: int, delta: int) -> int:
    """주어진 숫자에 따라 틱 값을 오프셋으로 사용합니다. 양수나 음수일 수 있습니다.

Example: ``time.ticks_add(time.ticks_ms(), 200)``

Given a ticks value, this function allows to calculate ticks
value delta ticks before or after it, following modular-arithmetic
definition of tick values.

:param ticks: 틱 값
:param delta: 정수 오프셋

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
    """``time.ticks_ms()`` 또는 ``ticks_us()``에서 반환된 값 사이의 틱 차이를 측정합니다. 서명된 값은 래핑될 수 있습니다.

Example: ``time.ticks_diff(scheduled_time, now)``

:param ticks1: 뺄 값
:param ticks2: 뺄 값

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