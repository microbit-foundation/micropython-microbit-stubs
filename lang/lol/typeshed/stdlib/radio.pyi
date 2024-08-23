"""crwdns330720:0crwdne330720:0 (crwdns330718:0crwdne330718:0)"""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""crwdns330724:0crwdne330724:0 (crwdns330722:0crwdne330722:0)"""
RATE_2MBIT: int
"""crwdns330728:0crwdne330728:0 (crwdns330726:0crwdne330726:0)"""

def on() -> None:
    """crwdns330732:0crwdne330732:0 (crwdns330730:0crwdne330730:0)

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """crwdns330736:0crwdne330736:0 (crwdns330734:0crwdne330734:0)

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """crwdns330740:0crwdne330740:0 (crwdns330738:0crwdne330738:0)

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (crwdns330758:0crwdne330758:0) crwdns330760:0crwdne330760:0
:param queue: (crwdns330766:0crwdne330766:0) crwdns330768:0crwdne330768:0
:param channel: (crwdns330746:0crwdne330746:0) crwdns330748:0crwdne330748:0
:param power: (crwdns330762:0crwdne330762:0) crwdns330764:0crwdne330764:0
:param address: (crwdns330742:0crwdne330742:0) crwdns330744:0crwdne330744:0
:param group: (crwdns330754:0crwdne330754:0) crwdns330756:0``address``crwdne330756:0
:param data_rate: (crwdns330750:0crwdne330750:0) crwdns330752:0``radio.RATE_1MBIT``crwdnd330752:0``radio``crwdnd330752:0``RATE_250KBIT``crwdnd330752:0``RATE_1MBIT``crwdnd330752:0``RATE_2MBIT``crwdne330752:0

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """crwdns330772:0crwdne330772:0 (crwdns330770:0crwdne330770:0)

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """crwdns330776:0crwdne330776:0 (crwdns330774:0crwdne330774:0)

Example: ``radio.send_bytes(b'hello')``

:param message: (crwdns330778:0crwdne330778:0) crwdns330780:0crwdne330780:0"""
    ...

def receive_bytes() -> Optional[bytes]:
    """crwdns330784:0crwdne330784:0 (crwdns330782:0crwdne330782:0)

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """crwdns330788:0crwdne330788:0 (crwdns330786:0crwdne330786:0)

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: (crwdns330790:0crwdne330790:0) crwdns330792:0crwdne330792:0
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """crwdns330796:0crwdne330796:0 (crwdns330794:0crwdne330794:0)

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: (crwdns330798:0crwdne330798:0) crwdns330800:0crwdne330800:0"""
    ...

def receive() -> Optional[str]:
    """crwdns330804:0``receive_bytes``crwdne330804:0 (crwdns330802:0crwdne330802:0)

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """crwdns330808:0crwdne330808:0 (crwdns330806:0crwdne330806:0)

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