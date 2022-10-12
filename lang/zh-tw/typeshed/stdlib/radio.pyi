"""使用內建無線電在 micro:bits 之間進行通訊。 (無線電)"""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""常數用於指示每秒 1 MBit 的輸送量。"""
RATE_2MBIT: int
"""常數用於指示每秒 2 MBit 的輸送量。"""

def on() -> None:
    """開啟無線電。

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """關閉無線電，節省電量和記憶體。

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """設定無線電。

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (default=32) 定義透過無線電傳送的訊息的最大長度 (以位元組為單位)。
最長可達 251 個位元組 (S0、LENGTH 和 S1 前序編碼為 254 - 3 個位元組)。
:param queue: (default=3) 指定可以存儲在傳入訊息佇列中的訊息數。
如果佇列中沒有空間可留給傳入訊息，則捨棄傳入訊息。
:param channel: (default=7) 一個從 0 到 83 (包含) 的整數值，定義無線電調整到的任意 "channel"。
訊息將透過此頻道傳送，只有透過此頻道接收的訊息，才會放入傳入訊息佇列。
每一步都是 1MHz 寬，以 2400MHz 為基礎。
:param power: (default=6) 是一個從 0 到 7 (包含) 的整數值，表示無線電訊息時使用的訊號功率。
數值越高，訊號越強，但裝置消耗的功率越多。編號轉換為下列 dBm (分貝毫瓦) 數值列表中的位置：-30、-20、-16、-12、-8、-4、0、4。
:param address: (default=0x75626974) 任意名稱，表示為 32 位元位址，用於在硬體等級篩選傳入的資料套件，僅保留與您設定的位址相符的那些。
其他 micro:bit 相關平台使用的預設設定，則是此處使用的預設設定。
:param group: (default=0) 篩選訊息時與 ``address`` 一起使用的 8 位元值 (0-255)。
從概念上講，"address" 就像一個家庭/辦公室地址，而 "group" 就像您要向該地址傳送訊息的人。
:param data_rate: (default=``radio.RATE_1MBIT``) 表示資料輸送量發生的速度。
可以是 ``radio`` 模組中定義的下列常數之一：``RATE_250KBIT``、``RATE_1MBIT`` 或 ``RATE_2MBIT``。

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """將設定重設為其預設值。

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """傳送包含位元組的訊息。

Example: ``radio.send_bytes(b'hello')``

:param message: 要傳送的位元組。"""
    ...

def receive_bytes() -> Optional[bytes]:
    """接收訊息佇列中的下一則傳入訊息。

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """將訊息佇列中的下一則傳入訊息複製到緩衝區。

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: 目標緩衝區。如果訊息大小大於緩衝區，則訊息會被截斷。
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """傳送訊息字串。

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: 要傳送的字串。"""
    ...

def receive() -> Optional[str]:
    """工作方式與 ``receive_bytes`` 完全相同，但會傳回傳送的任何內容。

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """傳回一個包含三個數值的元組，用來代表訊息佇列中的下一則傳入訊息。

Example: ``radio.receive_full()``

If there are no pending messages then ``None`` is returned.

The three values in the tuple represent:

- the next incoming message on the message queue as bytes.
- the RSSI (signal strength): a value between 0 (strongest) and -255 (weakest) as measured in dBm.
- a microsecond timestamp: the value returned by ``time.ticks_us()`` when the message was received.

For example::

    details = radio.receive_full()
    if details:
        msg, rssi, timestamp = details

This function is useful for providing information needed for triangulation
and/or trilateration with other micro:bit devices.

:return: ``None`` if there is no message, otherwise a tuple of length three with the bytes, strength and timestamp values."""
    ...