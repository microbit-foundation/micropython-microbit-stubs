"""低级实用程序。 (机器)"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """获取具有板的唯一标识符的字节字符串。

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """以类似于按下外部 RESET （重置）按钮的方式重置设备。

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """以赫兹为单位获取 CPU 频率。

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """禁止中断请求。

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """重新启用中断请求。

Example: ``machine.enable_irq(interrupt_state)``

:param state: 最近一次调用 ``disable_irq`` 函数得到的返回值。"""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """对引脚上的脉冲计时。

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: (引脚) 要使用的引脚
:param pulse_level: 0 来计时低脉冲或 1 来计时高脉冲。
:param timeout_us: 微秒超时
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """``mem8``、 ``mem16`` 和 ``mem32`` 内存视图的类。"""

    def __getitem__(self, address: int) -> int:
        """从内存中获取一个值。

:param address: (地址) 内存地址。
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """在给定地址处设置一个值。

:param address: (地址) 内存地址。
:param value: 要设置的整数值。"""
        ...
mem8: mem
"""8 位(字节) 内存视图。"""
mem16: mem
"""16 位内存视图。"""
mem32: mem
"""32 位内存视图。"""