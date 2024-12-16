"""低レベルユーティリティ"""
from typing import Any
from .microbit import MicroBitDigitalPin

def unique_id() -> bytes:
    """ボードの一意の識別子を持つバイト列を取得します。

Example: ``machine.unique_id()``

:return: An identifier that varies from one board instance to another."""
    ...

def reset() -> None:
    """外部のRESETボタンを押したと同様にデバイスをリセットします。

Example: ``machine.reset()``"""
    ...

def freq() -> int:
    """CPU周波数をヘルツ単位で取得します。

Example: ``machine.freq()``

:return: The CPU frequency."""
    ...

def disable_irq() -> Any:
    """割り込み要求を無効にします。

Example: ``interrupt_state = machine.disable_irq()``

:return: the previous IRQ state which should be considered an opaque value

The return value should be passed to the ``enable_irq`` function to restore
interrupts to their original state."""
    ...

def enable_irq(state: Any) -> None:
    """割り込み要求を再度有効にします。

Example: ``machine.enable_irq(interrupt_state)``

:param state: ``disable_irq`` 関数の最も最近の呼び出しから返された値。"""
    ...

def time_pulse_us(pin: MicroBitDigitalPin, pulse_level: int, timeout_us: int=1000000) -> int:
    """端子のパルス時間を計測します。

Example: ``time_pulse_us(pin0, 1)``

If the current input value of the pin is different to ``pulse_level``, the
function first waits until the pin input becomes equal to
``pulse_level``, then times the duration that the pin is equal to
``pulse_level``. If the pin is already equal to ``pulse_level`` then timing
starts straight away.

:param pin: (ピン) 計測対象の端子
:param pulse_level: 低パルスの時間計測で 0、高パルスの時間計測で 1 を指定
:param timeout_us: マイクロ秒単位のタイムアウト時間
:return: The duration of the pulse in microseconds, or -1 for a timeout waiting for the level to match ``pulse_level``, or -2 on timeout waiting for the pulse to end"""
    ...

class mem:
    """``mem8``、``mem16``、``mem32`` メモリビューのクラス。"""

    def __getitem__(self, address: int) -> int:
        """メモリにある値を参照します。

:param address: メモリのアドレス。
:return: The value at that address as an integer."""
        ...

    def __setitem__(self, address: int, value: int) -> None:
        """指定アドレスに値を設定します。

:param address: メモリのアドレス。
:param value: 設定する整数値。"""
        ...
mem8: mem
"""メモリの8ビット（バイト）ビュー。"""
mem16: mem
"""メモリの16ビットビュー。"""
mem32: mem
"""メモリの32ビットビュー。"""