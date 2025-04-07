"""シリアルペリフェラルインターフェイス（SPI）バスを使ってデバイスと通信します。"""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """SPI通信を初期化します。

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: 通信速度。
:param bits: 送信時のビット幅。現在のところは ``bits=8`` だけをサポート。しかし、これは将来的に変更するかもしれません。
:param mode: クロックの極性と位相の組み合わせを決定します - `オンラインの表を参照 <https://microbit-micropython.readthedocs.io/ja/v2-docs/spi.html#microbit.spi.init>`_ 。
:param sclk: sclk 端子（デフォルトは 13）
:param mosi: mosi 端子（デフォルトは 15）
:param miso: miso 端子（デフォルトは 14）"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """最大 ``nbytes`` バイトを読み取りながら、``out`` で指定された 1 バイトを書き続ける

Example: ``spi.read(64)``

:param nbytes: 読み取る最大バイト数。
:param out: 書き込むバイト値（初期値は'0'）
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """デバイスにバイト列を書き込みます。

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: データの読み取り元のバッファ。"""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """``out`` バッファをバスに書き込み、任意のレスポンスを ``in_`` バッファに読み取ります。

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: レスポンスの書き込みバッファ。
:param in_: データの読み取り元のバッファ。"""
    ...