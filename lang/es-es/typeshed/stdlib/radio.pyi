"""Comunicarse entre micro:bits con la radio incorporada."""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Constante utilizada para indicar un rendimiento de 1 Mb por segundo. (tasa de 1 mbit)"""
RATE_2MBIT: int
"""Constante utilizada para indicar un rendimiento de 2 Mb por segundo. (tasa de 2 mbit)"""

def on() -> None:
    """Enciende la radio. (encender)

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Apaga la radio, ahorrando energía y memoria. (apagado)

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Configura la radio.

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (longitud) (valor predeterminado = 32) define la longitud máxima, en bytes, de un mensaje enviado a través de la radio.
Puede tener hasta 251 bytes de largo (254 - 3 bytes para preámbulos S0, LENGTH y S1).
:param queue: (cola) (valor predeterminado = 3) especifica el número de mensajes que pueden almacenarse en la cola de mensajes entrantes.
Si no quedan espacios en la cola para los mensajes entrantes, el mensaje entrante será eliminado.
:param channel: (canal) (valor predeterminado = 7) un valor entero de 0 a 83 (inclusive) que define un "canal" arbitrario en el cual la radio está sintonizada.
Los mensajes se enviarán a través de este canal y solo los mensajes recibidos a través de este canal se pondrán en la cola de mensajes entrantes. Cada paso es de 1 MHz de ancho, basado en 2400 MHz.
:param power: (potencia) (valor predeterminado = 6) es un valor entero de 0 a 7 (inclusive) para indicar la fuerza de la señal usada al transmitir un mensaje.
Cuanto más alto sea el valor, más fuerte es la señal, pero más energía consume el dispositivo. La numeración se traduce a posiciones en la siguiente lista de valores de dBm (decibelio-milivatio): -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (dirección) (valor predeterminado = 0x75626974) un nombre arbitrario, expresado como una dirección de 32 bits, que se usa para filtrar los paquetes entrantes a nivel de hardware, manteniendo solo aquellos que coincidan con la dirección que has establecido.
El valor predeterminado utilizado por otras plataformas relacionadas con el micro:bit es la configuración predeterminada utilizada aquí.
:param group: (grupo) (valor predeterminado = 0) un valor de 8 bits (0 - 255) usado con el valor de ``address`` al filtrar mensajes.
Conceptualmente, "address" (dirección) es como una dirección de casa u oficina y "group" (grupo) es la persona que está en esa dirección y a la que quieres enviar un mensaje.
:param data_rate: (tasa de datos) (valor predeterminado = ``radio.RATE_1MBIT``) indica la velocidad a la que se lleva a cabo el procesamiento de datos.
Puede ser una de las siguientes constantes definidas en el módulo ``radio``: ``RATE_250KBIT``, ``RATE_1MBIT`` o ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Restablece la configuración a sus valores predeterminados. (restablecer)

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Envía un mensaje que contiene bytes. (enviar bytes)

Example: ``radio.send_bytes(b'hello')``

:param message: (mensaje) Los bytes a enviar."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Recibe el siguiente mensaje entrante en la cola de mensajes. (recibir bytes)

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Copia el siguiente mensaje entrante de la cola de mensajes en un búfer. (recibir bytes en)

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: (búfer) El búfer de destino. El mensaje se trunca si es más grande que el búfer.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Envía una cadena de mensaje. (enviar)

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: (mensaje) La cadena a enviar."""
    ...

def receive() -> Optional[str]:
    """Funciona exactamente del mismo modo que ``receive_bytes``, pero devuelve lo que se envió. (recibir)

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Devuelve una tupla de tres valores que representan el siguiente mensaje entrante de la cola de mensajes. (recibir completo)

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