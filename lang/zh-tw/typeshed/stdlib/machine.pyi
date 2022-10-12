"""低階公用程式。"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """取得具有開發板的唯一識別碼之位元組字串。

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """以類似於按下外部 RESET 按鍵的方式重置裝置。

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """取得以赫茲為單位的 CPU 頻率。 (頻率)

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """禁用中斷請求。 (禁用 irq)

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """重新啟用中斷請求。 (啟用 irq)

Example: ``machine.enable_irq(interrupt_state)``

:param state: 從最近一次調用 ``disable_irq`` 函式傳回的值。"""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """計時引腳上的脈衝。

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: (引腳) 要使用的引腳
:param pulse_level: 0 到計時低脈衝或 1 到計時高脈衝
:param timeout_us: 微秒逾時
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """``mem8``、``mem16`` 和 ``mem32`` 記憶體檢視的類別。"""

    def __getitem__(self, address: int) -> int:
        """從記憶體中存取一個值。

:param address: 記憶體位址。
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """在指定位址設定一個值。

:param address: 記憶體位址。
:param value: 要設定的整數值。"""
        ...
mem8: mem
"""8 位元 (位元組) 的記憶體檢視。"""
mem16: mem
"""16 位元的記憶體檢視。"""
mem32: mem
"""32 位元的記憶體檢視。"""