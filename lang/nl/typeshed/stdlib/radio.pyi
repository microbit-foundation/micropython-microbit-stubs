"""Communiceer tussen micro:bits met de ingebouwde radio."""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Constante gebruikt om een doorvoer van 1 MBit per seconde aan te geven."""
RATE_2MBIT: int
"""Constante gebruikt om een doorvoer van 2 MBit per seconde aan te geven."""

def on() -> None:
    """Zet de radio aan. (aan)

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Schakelt de radio uit, bespaar stroom en geheugen. (uit)

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Configureert de radio. (configuratie)

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (lengte) (default=32) definieert de maximale lengte, in bytes, van een bericht dat via de radio wordt verzonden.
Het kan maximaal 251 bytes lang zijn (254 - 3 bytes voor S0, LENGTH en S1 preamble).
:param queue: (wachtrij) (standaard=3) geeft het aantal berichten aan dat in de wachtrij van het inkomende bericht kan worden opgeslagen.
Als er geen ruimte meer is in de wachtrij voor binnenkomende berichten, dan valt het inkomende bericht weg.
:param channel: (kanaal) (default=7) een integer waarde van 0 tot 83 (inclusief) die een willekeurig "kanaal" definieert waaraan de radio wordt afgestemd.
Berichten worden via dit kanaal verzonden en alleen via dit kanaal worden berichten in de wachtrij van het inkomende berichten geplaatst. Elke stap is 1 MHz breed, gebaseerd op 2400MHz.
:param power: (vermogen) (default=6) is een integer waarde van 0 tot 7 (inclusief) om de sterkte van het signaal aan te geven dat wordt gebruikt bij het uitzenden van een bericht.
Hoe hoger de waarde, des te sterker het signaal, maar hoe meer stroom het apparaat verbruikt. De nummering vertaalt naar posities in de volgende lijst van dBm (decibel milliwatt) waarden: -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (adres) (default=0x75626974) een willekeurige naam, uitgedrukt als een 32-bits adres, wordt gebruikt om inkomende pakketten op hardware-niveau te filteren, waarbij alleen de pakketten worden bewaard die overeenkomen met het adres dat je zelf instelt.
De standaard gebruiker door andere micro:bit gerelateerde platforms is de standaard instelling die hier wordt gebruikt.
:param group: (groep) (standaard=0) een 8-bit waarde (0-255) gebruikt met de ``address`` bij het filteren van berichten.
Conceptueel, "adres" is als een huis/kantooradres en "groep" is als de persoon op dat adres waarnaar je je bericht wilt sturen.
:param data_rate: (Gegevens snelheid) (default=``radio.RATE_1MBIT``) geeft aan hoe snel de doorvoer van gegevens plaatsvindt.
Kan een van de volgende constanten zijn gedefinieerd in de ``radio`` module: ``RATE_250KBIT``, ``RATE_1MBIT`` of ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Reset alle instellingen naar hun standaardwaarde.

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Stuurt een bericht met bytes. (verstuur bytes)

Example: ``radio.send_bytes(b'hello')``

:param message: (bericht) De te verzenden bytes."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Ontvang het volgende inkomende bericht in de wachtrij van het bericht. (ontvang bytes)

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Kopieer het volgende inkomende bericht in de wachtrij van het bericht naar een buffer. (ontvang bytes in)

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: De doel buffer. Het bericht wordt ingekort als het groter is dan de buffer.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Stuurt een berichtenreeks. (verzenden)

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: (bericht) De te verzenden tekenreeks."""
    ...

def receive() -> Optional[str]:
    """Werkt op precies dezelfde manier als ``receive_bytes`` , maar retourneert wat er verzonden is. (ontvang)

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Geeft als resultaat een dup met drie waarden die het volgende inkomende bericht in de wachtrij van het bericht weergeven. (Ontvang vol)

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