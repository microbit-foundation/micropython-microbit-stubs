"""pack and unpack primitive data types

Supported size/byte order prefixes: ``@``, ``<``, ``>``, ``!``.

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``s``, ``P``, ``f``, ``d`` (the latter 2 depending
on the floating-point support).

.. admonition:: Difference to CPython
   :class: attention

   Whitespace is not supported in format strings.
"""

from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Return the number of bytes needed to store the given *fmt*."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Pack the values *v1*, *v2*, ... according to the format string *fmt*.
    The return value is a bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: bytearray, offset: int, v1: Any, *vn: Any) -> None:
    """Pack the values *v1*, *v2*, ... according to the format string *fmt*
    into a *buffer* starting at *offset*. *offset* may be negative to count
    from the end of *buffer*.
    """
    ...

def unpack(fmt: str, data: Union[bytes, bytearray]) -> Tuple:
    """Unpack from the *data* according to the format string *fmt*.
    The return value is a tuple of the unpacked values.
    """
    ...

def unpack_from(fmt: str, buffer: Union[bytes, bytearray], offset: int = 0) -> Tuple:
    """Unpack from the *data* starting at *offset* according to the format string
    *fmt*. *offset* may be negative to count from the end of *buffer*. The return
    value is a tuple of the unpacked values.
    """
    ...
