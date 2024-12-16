"""Kommunikation zwischen micro:bits mit dem integrierten Funk."""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Konstante zur Angabe eines Durchsatzes von 1\xa0MBit pro Sekunde."""
RATE_2MBIT: int
"""Konstante zur Angabe eines Durchsatzes von 2\xa0MBit pro Sekunde."""

def on() -> None:
    """Schaltet den Funk ein.

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Schaltet den Funk aus, um Strom und Speicherplatz zu sparen.

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Konfiguriert den Funk.

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (default=32) legt die maximale Länge einer über Funk gesendeten Nachricht in Bytes fest. Sie kann bis zu 251 Bytes lang sein (254 - 3 Bytes für S0, LENGTH und S1-Präambel).
:param queue: (default=3) gibt die Anzahl der Nachrichten an, die in der Warteschlange für eingehende Nachrichten gespeichert werden können. Wenn in der Warteschlange kein Platz mehr für eingehende Nachrichten ist, wird die eingehende Nachricht verworfen.
:param channel: (default=7) ein Integer-Wert zwischen 0 und 83 (einschließlich), der einen beliebigen "Kanal" definiert, auf den der Funk eingestellt ist.
Nachrichten werden über diesen Kanal gesendet und nur Nachrichten, die über diesen Kanal empfangen werden, werden in die Warteschlange der eingehenden Nachricht aufgenommen. Jeder Schritt ist 1MHz breit, beginnend mit 2400MHz.
:param power: (default=6) ist ein ganzzahliger Wert von 0 bis 7 (einschließlich), der die Stärke des Signals angibt, das beim Senden einer Nachricht verwendet wird. Je höher der Wert, desto stärker ist das Signal, aber desto mehr Strom wird vom Gerät verbraucht. Die Nummerierung entspricht den Positionen in der folgenden Liste von dBm-Werten (Dezibel Milliwatt): -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (adresse) (default=0x75626974) ein beliebiger Name, ausgedrückt als 32-Bit-Adresse, der verwendet wird, um eingehende Pakete auf der Hardware-Ebene zu filtern und nur diejenigen zu behalten, die mit der eingestellten Adresse übereinstimmen. 
Die Standardeinstellung, die von anderen micro:bit-verwandten Plattformen verwendet wird, wird auch hier verwendet.
:param group: (default=0) ein 8-Bit-Wert (0-255), der zusammen mit ``address`` beim Filtern von Nachrichten verwendet wird. "address" ist wie eine Haus-/Büroadresse und "group" ist wie die Person an dieser Adresse, an die die Nachricht gesendet werden soll.
:param data_rate: (default=``radio.RATE_1MBIT``) zeigt die Geschwindigkeit an, mit der der Datendurchsatz stattfindet.
Kann eine der folgenden Konstanten sein, die im Modul ``radio`` definiert sind: ``RATE_250KBIT``, ``RATE_1MBIT`` oder ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Setzt die Einstellungen auf ihre Standardwerte zurück. (zurücksetzen)

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Sendet eine Nachricht bestehend aus Bytes.

Example: ``radio.send_bytes(b'hello')``

:param message: Die zu sendenden Bytes."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Empfängt die nächste eingehende Nachricht in der Nachrichtenwarteschlange.

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Kopiert die nächste eingehende Nachricht in der Nachrichtenwarteschlange in einen Puffer.

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: (Puffer) Der Zielpuffer. Die Nachricht wird abgeschnitten, wenn sie größer als der Puffer ist.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Sendet eine Nachricht als String.

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: Der zu sendende String."""
    ...

def receive() -> Optional[str]:
    """Funktioniert genauso wie ``receive_bytes``, gibt aber zurück, was gesendet wurde.

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Gibt ein Tupel mit drei Werten zurück, die die nächste eingehende Nachricht in der Nachrichtenwarteschlange darstellen.

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