"""Comunicar entre micro:bits usando o rádio embutido. (rádio)"""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Constante usada para indicar uma taxa de transferência de 1 Mbit por segundo. (taxa de 1mbit)"""
RATE_2MBIT: int
"""Constante usada para indicar uma taxa de transferência de 2 Mbit por segundo. (taxa 2mbit)"""

def on() -> None:
    """Liga o rádio. (ligado)

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Desliga o rádio, economizando energia e memória. (desligado)

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Configura o rádio. (configuração)

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (comprimento) (default=32) define o comprimento máximo, em bytes, de uma mensagem enviada via rádio. Pode ter até 251 bytes de comprimento (254 - 3 bytes para os preâmbulos S0, LENGTH e S1).
:param queue: (fila) (default=3) especifica o número de mensagens que podem ser armazenadas na fila de mensagens recebidas. Se não houver mais espaço na fila para mensagens recebidas, a mensagem que chega será descartada.
:param channel: (canal) (padrão=7) um valor inteiro de 0 a 83 (inclusive) que define um "canal" arbitrário para o qual o rádio está sintonizado.  
As mensagens serão enviadas por este canal e apenas as mensagens recebidas por ele serão colocadas na fila de mensagens recebidas. Cada passo tem 1 MHz de largura, com base em 2400 MHz.
:param power: (poder/energia) (default=6) é um valor inteiro de 0 a 7 (inclusive) para indicar a intensidade do sinal usado ao transmitir uma mensagem. Quanto maior o valor, mais forte é o sinal, mas mais energia é consumida pelo dispositivo. A numeração se traduz nas posições da seguinte lista de valores em dBm (decibel miliwatt): -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (Endereço) (padrão=0x75626974) um nome arbitrário, expresso como um endereço de 32 bits, usado para filtrar pacotes de entrada no nível de hardware, mantendo apenas aqueles que correspondem ao endereço definido.
O padrão utilizado por outras plataformas relacionadas ao micro:bit é a configuração padrão utilizada aqui.
:param group: (grupo) (default=0) um valor de 8 bits (0-255) usado com o ``address`` ao filtrar mensagens. Conceitualmente, "endereço" é como um endereço de casa/escritório e "grupo" é como a pessoa naquele endereço para a qual você deseja enviar sua mensagem.
:param data_rate: (taxa de dados) (padrão=``radio.RATE_1MBIT``) indica a velocidade na qual a transferência de dados ocorre.  
Pode ser uma das seguintes constantes definidas no módulo ``radio``: ``RATE_250KBIT``, ``RATE_1MBIT`` ou ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Redefina as configurações para seus valores padrão. (redefinir)

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Envia uma mensagem contendo bytes. (enviar bytes)

Example: ``radio.send_bytes(b'hello')``

:param message: (mensagem) Os bytes para enviar."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Recebe a próxima mensagem recebida na fila de mensagens. (receber bytes)

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Copia a próxima mensagem recebida na fila de mensagens para um buffer. (receber bytes em)

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: (Tampão) O buffer de destino. A mensagem é truncada se for maior que o buffer.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Envia uma string de mensagem. (enviar)

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: (mensagem) A string a ser enviada."""
    ...

def receive() -> Optional[str]:
    """Funciona exatamente da mesma forma que ``receive_bytes``, mas retorna tudo o que foi enviado. (receber)

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Retorna uma tupla contendo três valores que representam a próxima mensagem recebida na fila de mensagens. (receber completo)

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