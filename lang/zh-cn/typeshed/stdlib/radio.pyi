"""使用内置无线电在 micro:bit 之间进行通信。 (无线电)"""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""用于表示每秒 1 兆字节吞吐量的常数。 (速率 1Mbit)"""
RATE_2MBIT: int
"""用于表示每秒 2 兆字节吞吐量的常数。 (速率 2Mbit)"""

def on() -> None:
    """打开无线电。 (打开)

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """关闭无线电以节省电量和内存。 (关闭)

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """配置无线电。 (配置)

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (长度) （默认值32）以字节为单位，定义了通过无线电传输消息的最大长度。
其长度可达 251 字节（S0、LENGTH 和 S1 前导码：254-3 字节）。
:param queue: (队列) （默认值3）规定了传入消息队列中可以存储的消息数量。
如果队列中没有多余的空间留给传入的消息，那么传入的消息就会被丢弃。
:param channel: (信道) （缺省值7）范围为从0到83（含83）的整数，用于定义一任意“信道”，以便将无线电调到该信道。信息通过该信道发送，并且只有通过该信道接收到的消息才被放到传入消息队列中。每一步的宽度为 1 MHz，基于 2400 MHz。
:param power: (幂数) （默认值6）用于表示广播消息时所使用信号强度的整数值，其范围为从0到7（包含7）。
该值越大，信号越强，但设备消耗的功率也越大。其编码转换为以下 dBm（分贝毫瓦）值列表中的不同值：-30, -20, -16, -12, -8, -4, 0, 4。
:param address: (地址) (default=0x75626974) 任意名称，表示为 32 位地址，用于在硬件级别过滤传入的数据包，仅保留与您设置的地址匹配的数据包。
其他 micro:bit 相关平台使用的默认设置与此处的默认设置相同。
:param group: (群组) （默认值0）过滤消息时与 ``address`` 一起使用的 8 位的数值（0-255）。
从概念上讲，"address”就像房屋或办公室的地址，而“group”就像住在该地址，并且你想给他或她发消息的那个人。
:param data_rate: (数据传输速率) （默认值``radio.RATE_1MBIT``）表示数据吞吐速度。
可以是``radio``模块中定义的以下常数之一：``RATE_250KBIT``、``RATE_1MBIT`` 或 ``RATE_2MBIT``。

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """将设置重设为默认值。

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """发送一条包含字节的消息。 (发送字节)

Example: ``radio.send_bytes(b'hello')``

:param message: (消息) 待发送的字节。"""
    ...

def receive_bytes() -> Optional[bytes]:
    """接收消息队列中的下一条传入消息。 (接收字节)

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """将消息队列中的下一条传入消息复制到缓冲区。 (接收传入的字节)

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: (缓冲区) 目标缓冲区。如果消息大小大于缓冲区，则消息会被截断。
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """发送消息字符串。 (发送)

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: (消息) 待发送的字符串。"""
    ...

def receive() -> Optional[str]:
    """按照与``receive_bytes``完全相同的工作方式，但是返回所发送的内容。 (接收)

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """返回一个包含三个数值的元组，用来代表消息队列中的下一条传入消息。 (接受完整消息)

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