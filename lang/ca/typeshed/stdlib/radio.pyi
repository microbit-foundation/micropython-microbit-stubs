"""Comunicar-se entre micro:bits amb la ràdio integrada. (ràdio)"""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""La constant utilitzada per indicar un rendiment d'1 Mbit per segon. (velocitat de transmissió 1mbit)"""
RATE_2MBIT: int
"""La constant utilitzada per indicar un rendiment de 2 Mbit per segon. (velocitat de transmissió 2mbit)"""

def on() -> None:
    """Encén la ràdio.

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Apaga la ràdio, estalviant energia i memòria.

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Configura la ràdio.

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (llargada) (per defecte=32) defineix la longitud màxima, en bytes, d'un missatge enviat a través de la ràdio.
Pot tenir una longitud de fins a 251 bytes (254 - 3 bytes per al preàmbul S0, LENGTH i S1).
:param queue: (cua) (per defecte=3) especifica el nombre de missatges que es poden emmagatzemar a la cua de missatges entrants.
Si no queden espais a la cua per als missatges entrants, s'elimina el missatge entrant.
:param channel: (canal) (per defecte=7) un valor enter de 0 a 83 (inclosos) que defineix un "canal" arbitrari al qual està sintonitzada la ràdio.
Els missatges s'enviaran a través d'aquest canal i només els missatges rebuts per aquest canal es posaran a la cua de missatges entrants. Cada pas té una amplada d'1MHz, basat en 2400MHz.
:param power: (per defecte=6) és un valor enter de 0 a 7 (inclosos) per indicar la intensitat del senyal utilitzat quan s'emet un missatge.
Com més alt sigui el valor, més fort és el senyal, però més potència consumeix el dispositiu. La numeració es tradueix en posicions a la llista següent de valors en dBm (decibels mil·liwatts): -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (adreça) (per defecte=0x75626974) un nom arbitrari, expressat com una adreça de 32 bits, que s'utilitza per filtrar els paquets entrants a nivell de maquinari, conservant només els que coincideixen amb l'adreça que has establert.
La configuració predeterminada utilitzada per altres plataformes relacionades amb micro:bit és la configuració predeterminada que s'utilitza aquí.
:param group: (grup) (per defecte=0) un valor de 8 bits (0-255) utilitzat amb l'``address`` (adreça) en filtrar missatges.
Conceptualment, "adreça" és com una adreça de casa/oficina i "grup" és com la persona a aquesta adreça a la qual vols enviar el teu missatge.
:param data_rate: (velocitat de dades) (per defecte=``radio.RATE_1MBIT``) indica la velocitat a la qual es produeix la transmissió de les dades.
Pot ser una de les constants següents definides al mòdul ``radio``: ``RATE_250KBIT``, ``RATE_1MBIT`` o ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Restableix la configuració als seus valors predeterminats. (reiniciar)

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Envia un  missatge que conté bytes. (enviar bytes)

Example: ``radio.send_bytes(b'hello')``

:param message: (missatge) Els bytes a ser enviats."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Rebràs el següent missatge entrant a la cua de missatges. (rebre bytes)

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Copia el següent missatge entrant de la cua de missatges a una memòria intermèdia. (rebre bytes a)

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: (memòria intermèdia) La memòria intermèdia objectiu. El missatge es trunca si és més gran que la memòria intermèdia.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Envia una cadena de missatge. (envia)

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: (missatge) La cadena a enviar."""
    ...

def receive() -> Optional[str]:
    """Funciona exactament de la mateixa manera que ``receive_bytes`` però retorna el que s'ha enviat.

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Retorna una tupla que conté tres valors que representen el següent missatge entrant a la cua de missatges. (rebre ple)

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