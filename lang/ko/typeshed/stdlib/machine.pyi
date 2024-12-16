"""로우 레벨 유틸리티입니다."""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """보드의 고유 식별자가 있는 바이트 문자열을 불러옵니다.

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """외부 초기화 버튼을 누른 것과 유사한 방식으로 기기를 초기화합니다.

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """헤르츠로 표시된 CPU 진동수를 불러옵니다.

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """인터럽트 요청을 비활성화합니다.

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """인터럽트 요청을 재활성화합니다.

Example: ``machine.enable_irq(interrupt_state)``

:param state: ``disable_irq`` 함수에서 가장 최근에 호출된 값을 반환합니다."""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """핀 펄스 시간을 측정합니다.

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: (핀) 사용할 핀
:param pulse_level: (펄스 레벨) 로우 펄스의 시간을 측정하려면 0, 하이 펄스는 1
:param timeout_us: 마이크로초 시간 초과
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """``mem8``, ``mem16``, ``mem32`` 메모리 뷰 클래스"""

    def __getitem__(self, address: int) -> int:
        """메모리 값에 액세스합니다.

:param address: 메모리 주소입니다.
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """제공된 주소에 값을 설정합니다.

:param address: 메모리 주소입니다.
:param value: 설정할 정수값입니다."""
        ...
mem8: mem
"""8비트(바이트) 메모리 뷰입니다."""
mem16: mem
"""16비트 메모리 뷰입니다."""
mem32: mem
"""32비트 메모리 뷰입니다."""