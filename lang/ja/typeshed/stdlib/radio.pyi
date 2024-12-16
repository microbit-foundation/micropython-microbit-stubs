"""内蔵の無線通信を使ったmicro:bit間の通信。"""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""1 MBit/秒のスループットを示すために使われる定数。"""
RATE_2MBIT: int
"""2 MBit/秒のスループットを示すために使われる定数。"""

def on() -> None:
    """無線通信をオンにします。

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """無線通信をオフにして、電力とメモリを節約します。

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """無線通信を設定します。

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (デフォルト=32)\u3000無線を介して送信されるメッセージのバイト単位の最大長を設定します。
最大で 251 バイト（S0、長さ、S1 プリアンブルは254 から 3 を引いたバイト数）に設定できます。
:param queue: (デフォルト=3)\u3000受信メッセージキューに格納できるメッセージの数を指定します。
着信メッセージのキューに空きがない場合、着信メッセージは捨てられます。
:param channel: (デフォルト=7)\u3000無線が同調されている任意の「チャネル」を定義するもので、0 から 83 までの整数値を設定できます。メッセージはこのチャネル経由で送信され、このチャネル経由で受信したメッセージだけが受信メッセージキューに入れられます。各ステップは 1MHz 幅で、2400MHz を基準にしています。
:param power: (デフォルト=6)\u3000メッセージをブロードキャストするときに使用される信号の強度を示すもので、0 から 7 までの整数値（指定の値を含む。）を設定できです。
値が高いほど信号は強くなりますが、デバイスが消費する電力が大きくなります。指定の番号は次のリストの dBm（デシベルミリワット）値の位置に変換されます: -30, -20, -16, -12, -8, -4, 0, 4 。
:param address: (デフォルト=0x75626974)\u300032 ビットのアドレスとして表される任意の名前であり、ハードウェアレベルで着信パケットをフィルタリングするために使用されます。フィルタリングはユーザーが設定したアドレスと一致するもののみを維持します。
他のmicro:bit関連のプラットフォームで使われるデフォルトは、ここで使われるデフォルト設定となっています。
:param group: (デフォルト=0)\u30008ビットの値（0〜255）であり、 ``address`` フィルタしたメッセージで使います。
概念的に「address」は自宅/事務所の住所のようなものであり、「group」はその住所のメッセージを受け取人のようなものです。
:param data_rate: (デフォルト=``radio.RATE_1MBIT``)\u3000データスループットが起こる速度を示しています。
``radio`` モジュールに定義されている定数 ``RATE_250KBIT``、``RATE_1MBIT``、``RATE_2MBIT`` のいずれかを指定します。

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """設定をデフォルト値にリセットします。

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """バイト列を含んだメッセージを送信します。

Example: ``radio.send_bytes(b'hello')``

:param message: 送信するバイト列。"""
    ...

def receive_bytes() -> Optional[bytes]:
    """メッセージキューにある次の着信メッセージを受信します。

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """メッセージキューにある次の着信メッセージをバッファにコピーします。

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: メッセージを格納するバッファ。メッセージがバッファより大きい場合、メッセージの収まらない部分が切り捨てられます。
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """メッセージ文字列を送信します。

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: 送信する文字列。"""
    ...

def receive() -> Optional[str]:
    """``receive_bytes`` と同じように動作しますが、送信されてきたものはすべて返します。

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """メッセージキューにある次の受信メッセージを表す3つの値をタプルで返します。

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