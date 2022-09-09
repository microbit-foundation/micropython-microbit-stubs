"""プリミティブデータ型のパックとアンパック。 (struct)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """指定した ``fmt`` で格納するために必要なバイト数を取得します。 (calcsize)

Example: ``struct.calcsize('hf')``

:param fmt: (fmt) フォーマット文字列。
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """フォーマット文字列にしたがって複数の値をパックします。 (pack)

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: (fmt) フォーマット文字列。
:param v1: (v1) 先頭の値。
:param *vn: (*vn) 残りの値。
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """フォーマット文字列にしたがって複数の値をパックします。 (pack into)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: (fmt) フォーマット文字列。
:param buffer: (buffer) 書き込み先のバッファ。
:param offset: (offset) バッファのオフセット。負の場合はバッファの最後からのオフセットになります。
:param v1: (v1) 先頭の値。
:param *vn: (*vn) 残りの値。"""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """フォーマット文字列にしたがってデータをアンパックします。 (unpack)

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: (fmt) フォーマット文字列。
:param data: (data) データ。
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """フォーマット文字列にしたがってバッファからデータをアンパックします。 (unpack from)

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: (fmt) フォーマット文字列。
:param buffer: (buffer) 読み込み元のバッファ。
:param offset: (offset) バッファのオフセット。負の場合はバッファの最後からのオフセットになります。
:return: A tuple of the unpacked values."""
    ...