"""crwdns330252:0crwdne330252:0 (crwdns330250:0crwdne330250:0)"""
from _typeshed import ReadableBuffer, WriteableBuffer
from ..microbit import pin13, pin14, pin15, MicroBitDigitalPin

def init(baudrate: int=1000000, bits: int=8, mode: int=0, sclk: MicroBitDigitalPin=pin13, mosi: MicroBitDigitalPin=pin15, miso: MicroBitDigitalPin=pin14) -> None:
    """crwdns330256:0crwdne330256:0 (crwdns330254:0crwdne330254:0)

Example: ``spi.init()``

For correct communication, the parameters have to be the same on both communicating devices.

:param baudrate: (crwdns330258:0crwdne330258:0) crwdns330260:0crwdne330260:0
:param bits: (crwdns330262:0crwdne330262:0) crwdns334412:0crwdne334412:0
:param mode: (crwdns330270:0crwdne330270:0) crwdns330272:0crwdne330272:0
:param sclk: (crwdns330278:0crwdne330278:0) crwdns330280:0crwdne330280:0
:param mosi: (crwdns330274:0crwdne330274:0) crwdns330276:0crwdne330276:0
:param miso: (crwdns330266:0crwdne330266:0) crwdns330268:0crwdne330268:0"""
    ...

def read(nbytes: int, out: int=0) -> bytes:
    """crwdns330284:0``nbytes``crwdnd330284:0``out``crwdne330284:0 (crwdns330282:0crwdne330282:0)

Example: ``spi.read(64)``

:param nbytes: (crwdns330286:0crwdne330286:0) crwdns330288:0crwdne330288:0
:param out: (crwdns360362:0crwdne360362:0) crwdns360364:0crwdne360364:0
:return: The bytes read."""
    ...

def write(buffer: ReadableBuffer) -> None:
    """crwdns330292:0crwdne330292:0 (crwdns330290:0crwdne330290:0)

Example: ``spi.write(bytes([1, 2, 3]))``

:param buffer: (crwdns330294:0crwdne330294:0) crwdns330296:0crwdne330296:0"""
    ...

def write_readinto(out: WriteableBuffer, in_: ReadableBuffer) -> None:
    """crwdns330300:0``out``crwdnd330300:0``in_``crwdne330300:0 (crwdns330298:0crwdne330298:0)

Example: ``spi.write_readinto(out_buffer, in_buffer)``

The length of the buffers should be the same. The buffers can be the same object.

:param out: (crwdns330306:0crwdne330306:0) crwdns330308:0crwdne330308:0
:param in_: (crwdns330302:0crwdne330302:0) crwdns330304:0crwdne330304:0"""
    ...