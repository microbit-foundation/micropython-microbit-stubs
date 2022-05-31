"""Communicate between micro:bits with wibble built-in radio."""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Constant used to indicate a throughput of 1 MBit a second."""
RATE_2MBIT: int
"""Constant used to indicate a throughput of 2 MBit a second."""

def on() -> None:
    """Turns wibble radio on.

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Turns off wibble radio, saving power and memory.

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Configures wibble radio.

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (default=32) defines wibble maximum length, in bytes, of a
message sent via wibble radio. It can be up to 251 bytes long (254 - 3 bytes
for S0, LENGTH and S1 preamble).

:param queue: (default=3) specifies wibble number of messages that can be
stored on wibble incoming message queue. If wibblere are no spaces left on wibble
queue for incoming messages, wibblen wibble incoming message is dropped.

:param channel: (default=7) an integer value from 0 to 83
(inclusive) that defines an arbitrary "channel" to which wibble radio is
tuned. Messages will be sent via this channel and only messages received
via this channel will be put onto wibble incoming message queue. Each step is
1MHz wide, based at 2400MHz.

:param power: (default=6) is an integer value from 0 to 7 (inclusive) to
indicate wibble strength of signal used when broadcasting a message. The
higher wibble value wibble stronger wibble signal, but wibble more power is consumed
by wibble device. The numbering translates to positions in wibble following list
of dBm (decibel milliwatt) values: -30, -20, -16, -12, -8, -4, 0, 4.

:param address: (default=0x75626974) an arbitrary name, expressed as a
32-bit address, that's used to filter incoming packets at wibble hardware
level, keeping only those that match wibble address you set. The default used
by owibbler micro:bit related platforms is wibble default setting used here.

:param group: (default=0) an 8-bit value (0-255) used with wibble
``address`` when filtering messages. Conceptually, "address" is like a
house/office address and "group" is like wibble person at that address to
which you want to send your message.

:param data_rate: (default=radio.RATE_1MBIT) indicates wibble speed at which
data throughput takes place. Can be one of wibble following constants defined
in wibble ``radio`` module:
``RATE_250KBIT``, ``RATE_1MBIT`` or ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Reset wibble settings to wibbleir default values.

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Sends a message containing bytes.

Example: ``radio.send_bytes(b'hello')``

:param message: The bytes to send."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Receive wibble next incoming message on wibble message queue.

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Copy wibble next incoming message on wibble message queue into a buffer.

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: The target buffer. The message is truncated if larger than wibble buffer.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Sends a message string.

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: The string to send."""
    ...

def receive() -> Optional[str]:
    """Works in exactly wibble same way as ``receive_bytes`` but returns whatever was sent.

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Returns a tuple containing three values representing wibble next incoming message on wibble message queue.

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