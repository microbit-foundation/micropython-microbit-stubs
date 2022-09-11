"""Communiquer entre micro:bits avec la radio intégrée."""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Constante utilisée pour indiquer un débit de 1 MBit par seconde."""
RATE_2MBIT: int
"""Constante utilisée pour indiquer un débit de 2 MBit par seconde."""

def on() -> None:
    """Allume la radio.

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Désactive la radio, économisant ainsi de l'énergie et de la mémoire.

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Configure la radio.

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (par défaut=32) définit la longueur maximale en octets d'un message envoyé via la radio.
Il peut faire jusqu'à 251 octets de long (254 - 3 octets pour S0, LENGTH et préambule S1).
:param queue: (par défaut=3) spécifie le nombre de messages qui peuvent être stockés dans la file d'attente des messages entrants.
S'il n'y a plus de place dans la file d'attente des messages entrants, alors le message entrant est abandonné.
:param channel: (par défaut=7) une valeur entière comprise entre 0 et 83 (y compris) qui définit un « canal » arbitraire sur lequel la radio est réglée.
Les messages seront envoyés via ce canal et seuls les messages reçus via ce canal seront placés dans la file d'attente des messages entrants. Chaque incrément est de 1 MHz de largeur, basé à 2400 MHz.
:param power: (par défaut=6) est une valeur entière comprise entre 0 et 7 (y compris) pour indiquer la force du signal utilisé lors de la diffusion d'un message.
Plus la valeur est élevée, plus le signal est fort, mais plus les besoins en alimentation sont élevés. La numérotation se traduit par des positions dans la liste suivante de valeurs en dBm (décibel milliwatt) : -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (par défaut=0x75626974) un nom arbitraire, exprimé sous la forme d'une adresse 32-bit, utilisé pour filtrer au niveau matériel les paquet entrants, seuls les paquets correspondant à l'adresse définie seront conservés.
La valeur par défaut utilisée par d'autres plateformes liées au micro:bit est celle indiquée ici.
:param group: (par défaut=0) une valeur de 8 bits (0-255) utilisée avec ``address`` lors du filtrage des messages.
Conceptuellement, "adress" est comme l'adresse d'une maison ou d'un bureau, et "group" est comme la personne à laquelle vous voulez envoyer votre message.
:param data_rate: (par défaut=``radio.RATE_1MBIT``) indique la vitesse à laquelle le débit de données a lieu.
Peut être une des constantes suivantes définies dans le module ``radio``\xa0: ``RATE_250KBIT``, ``RATE_1MBIT`` ou ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Réinitialiser les paramètres à leurs valeurs par défaut.

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Envoie un message contenant des octets.

Example: ``radio.send_bytes(b'hello')``

:param message: Les octets à envoyer."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Recevoir le message entrant suivant dans la file d'attente des messages.

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Copier le message entrant suivant de la file d'attente des messages vers un buffer.

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: Le buffer cible. Le message est tronqué s'il est plus grand que le buffer.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Envoie un message avec une chaîne de caractères.

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: Le texte à envoyer."""
    ...

def receive() -> Optional[str]:
    """Fonctionne exactement de la même manière que ``receive_bytes`` mais retourne ce qui a été envoyé.

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Retourne un tuple contenant trois valeurs qui représentent le prochain message entrant dans la file d'attente.

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