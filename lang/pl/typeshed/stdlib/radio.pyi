"""Komunikuj się pomiędzy micro:bitami za pomocą wbudowanego radia."""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Stała używana do wskazania przepustowości 1 MBit na sekundę."""
RATE_2MBIT: int
"""Stała używana do wskazania przepustowości 2 MBit na sekundę."""

def on() -> None:
    """Włącza radio

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Wyłącza radio, oszczędzając energię i pamięć.

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Konfiguruje radio.

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (default=32) definiuje maksymalną długość w bajtach wiadomości wysyłanej przez radio.
Może mieć długość do 251 bajtów (254 - 3 bajty dla S0, LENGTH i S1).
:param queue: (default=3) określa liczbę wiadomości, które mogą być przechowywane w kolejce przychodzących wiadomości.
Jeśli w kolejce na wiadomości przychodzące nie ma już wolnych miejsc, wiadomość przychodząca jest odrzucana.
:param channel: (default=7) wartość całkowita od 0 do 83 (włącznie), która definiuje dowolny „kanał”, do którego dostrojone jest radio.
Wiadomości będą wysyłane za pośrednictwem tego kanału i tylko wiadomości otrzymane za pośrednictwem tego kanału zostaną umieszczone w kolejce wiadomości przychodzących. Każdy stopień ma szerokość 1 MHz w oparciu o częstotliwość 2400 MHz.
:param power: (default=6) jest liczb całkowitą od 0 do 7 (włącznie) do oznaczenia siły sygnału używanego podczas nadawania wiadomości.
Im wyższa wartość, tym silniejszy jest sygnał, ale tym większa moc jest zużywana przez urządzenie. Numeracja przekłada się na pozycje w następującym wykazie wartości dBm (decybel miliwat): -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (default=0x75626974) dowolna nazwa wyrażona jako 32-bitowy adres, używana do filtrowania przychodzących pakietów na poziomie sprzętowym, zatrzymując tylko te, które odpowiadają ustawionemu adresowi.
Domyślnym ustawieniem używanym przez inne platformy powiązane z micro:bitem jest ustawienie domyślne używane tutaj.
:param group: (default=0) 8-bitowa wartość (0-255) używana wraz z ``address`` podczas filtrowania wiadomości.
Koncepcyjnie, "adres" jest jak adres domu/biura, a "grupa" jest jak osoba pod tym adresem, na który chcesz wysłać swoją wiadomość.
:param data_rate: (default=``radio.RATE_1MBIT``) wskazuje prędkość, z jaką odbywa się przesyłanie danych.
Może być jedną z następujących stałych zdefiniowanych w module ``radio``:``RATE_250KBIT``, ``RATE_1MBIT`` lub ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Resetuj ustawienia do ich wartości domyślnych.

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Wysyła wiadomość zawierającą bajty.

Example: ``radio.send_bytes(b'hello')``

:param message: Bajty do wysłania."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Otrzymuj następną przychodzącą wiadomość w kolejce wiadomości.

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Skopiuj następną wiadomość przychodzącą do kolejki wiadomości w buforze.

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: Bufor docelowy. Wiadomość jest obcinana, jeśli jest większa niż bufor.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Wysyła łańcuch wiadomości.

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: Łańcuch do wysłania."""
    ...

def receive() -> Optional[str]:
    """Działa dokładnie w taki sam sposób, jak ``receive_bytes``, ale zwraca cokolwiek zostało wysłane. (odbierz)

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Zwraca krotkę zawierającą trzy wartości reprezentujące następną wiadomość przychodzącą do kolejki wiadomości.

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