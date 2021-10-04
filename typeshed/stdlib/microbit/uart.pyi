"""The ``uart`` module lets you talk to a device connected to your board using
a serial interface.
"""

from . import MicroBitDigitalPin
from typing import Optional, Union

ODD: int
"""Odd partity"""

EVEN: int
"""Even parity"""

def init(
    baudrate: int = 9600,
    bits: int = 8,
    parity: Optional[int] = None,
    stop: int = 1,
    tx: MicroBitDigitalPin = None,
    rx: MicroBitDigitalPin = None,
) -> None:
    """Initialize serial communication with the specified parameters on the
    specified ``tx`` and ``rx`` pins. Note that for correct communication, the parameters
    have to be the same on both communicating devices.

    .. warning::

        Initializing the UART on external pins will cause the Python console on
        USB to become unaccessible, as it uses the same hardware. To bring the
        console back you must reinitialize the UART without passing anything for
        ``tx`` or ``rx`` (or passing ``None`` to these arguments).  This means
        that calling ``uart.init(115200)`` is enough to restore the Python console.

    The ``baudrate`` defines the speed of communication. Common baud
    rates include:

        * 9600
        * 14400
        * 19200
        * 28800
        * 38400
        * 57600
        * 115200

    The ``bits`` defines the size of bytes being transmitted, and the board
    only supports 8. The ``parity`` parameter defines how parity is checked,
    and it can be ``None``, ``microbit.uart.ODD`` or ``microbit.uart.EVEN``.
    The ``stop`` parameter tells the number of stop bits, and has to be 1 for
    this board.

    If ``tx`` and ``rx`` are not specified then the internal USB-UART TX/RX pins
    are used which connect to the USB serial converter on the micro:bit, thus
    connecting the UART to your PC.  You can specify any other pins you want by
    passing the desired pin objects to the ``tx`` and ``rx`` parameters.

    .. note::

        When connecting the device, make sure you "cross" the wires -- the TX
        pin on your board needs to be connected with the RX pin on the device,
        and the RX pin -- with the TX pin on the device. Also make sure the
        ground pins of both devices are connected.
    """
    ...

def any() -> bool:
    """Return ``True`` if any data is waiting, else ``False``."""
    ...

def read(nbytes: int = None) -> bytes:
    """Read bytes.  If ``nbytes`` is specified then read at most that many
    bytes, otherwise read as many bytes as possible.

    Return value: a bytes object or ``None`` on timeout.

    A bytes object contains a sequence of bytes. Because `ASCII <https://en.wikipedia.org/wiki/ASCII>`_
    characters can fit in single bytes this type of object is often used to
    represent simple text and offers methods to manipulate it as such, e.g.
    you can display the text using the ``print()`` function.

    You can also convert this object into a string object, and if there are
    non-ASCII characters present the encoding can be specified::

        msg_bytes = uart.read()
        msg_str = str(msg, 'UTF-8')

    .. note::

        The timeout for all UART reads depends on the baudrate and is otherwise
        not changeable via Python. The timeout, in milliseconds, is given by:
        ``microbit_uart_timeout_char = 13000 / baudrate + 1``

    .. note::

        The internal UART RX buffer is 64 bytes, so make sure data is read
        before the buffer is full or some of the data might be lost.

    .. warning::

        Receiving ``0x03`` will stop your program by raising a Keyboard
        Interrupt. You can enable or disable this using
        :func:`micropython.kbd_intr()`.
    """
    ...

def readinto(buf: bytearray, nbytes: int = None) -> Optional[int]:
    """Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
    that many bytes.  Otherwise, read at most ``len(buf)`` bytes.

    Return value: number of bytes read and stored into ``buf`` or ``None`` on
    timeout.
    """

def readline() -> Optional[bytes]:
    """Read a line, ending in a newline character.

    Return value: the line read or ``None`` on timeout. The newline character is
    included in the returned bytes.
    """

def write(buf: Union[bytes, bytearray]) -> Optional[int]:
    """Write the buffer to the bus, it can be a bytes object or a string::

        uart.write('hello world')
        uart.write(b'hello world')
        uart.write(bytes([1, 2, 3]))

    Return value: number of bytes written or ``None`` on timeout.
    """
