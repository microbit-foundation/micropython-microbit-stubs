"""Cumarsáid a dhéanamh idir micro:bit leis an raidió tógtha. (raidió)"""
from _typeshed import WriteableBuffer
from typing import Optional, Tuple
RATE_1MBIT: int
"""Tairiseach a úsáidtear chun tréchur 1 MBit an dara ceann a léiriú. (ráta 1mbit)"""
RATE_2MBIT: int
"""Tairiseach a úsáidtear chun tréchur 2 MBit an dara ceann a léiriú. (ráta 2mbit)"""

def on() -> None:
    """Casann sé an raidió air. (ar)

Example: ``radio.on()``

This needs to be explicitly called since the radio draws power and takes
up memory that you may otherwise need."""
    ...

def off() -> None:
    """Múchann sé an raidió, ag sábháil cumhachta agus cuimhne. (as)

Example: ``radio.off()``"""
    ...

def config(length: int=32, queue: int=3, channel: int=7, power: int=6, address: int=1969383796, group: int=0, data_rate: int=RATE_1MBIT) -> None:
    """Cumraigh an raidió. (cumraíocht)

Example: ``radio.config(group=42)``

The default configuration is suitable for most use.

:param length: (fad) Sainmhíníonn (réamhshocrú=32) an fad uasta, i mbéiteanna, de theachtaireacht a sheoltar tríd an raidió.
Féadfaidh sé a bheith suas le 251 beart ar fhad (254 - 3 beart do réamhrá S0, FAD agus S1).
:param queue: (scuaine) (réamhshocrú = 3) sonraítear líon na dteachtaireachtaí is féidir a stóráil ar an scuaine teachtaireachta isteach.
Mura bhfuil aon spásanna fágtha ar an scuaine le haghaidh teachtaireachtaí isteach, ansin tá an teachtaireacht ag teacht isteach thit.
:param channel: (cainéal) (réamhshocrú = 7) slánuimhir luach ó 0 go 83 (san áireamh) a shainmhíníonn "cainéal" treallach a bhfuil an raidió tiúnta leis.
Seolfar teachtaireachtaí tríd an gcainéal seo agus ní chuirfear ach teachtaireachtaí a fhaightear tríd an gcainéal seo ar an scuaine teachtaireachtaí atá ag teacht isteach. Tá gach céim 1MHz ar leithead, bunaithe ar 2400MHz.
:param power: (cumhacht) (réamhshocrú = 6) Is luach slánuimhir ó 0 go 7 (san áireamh) a chur in iúl ar an neart comhartha a úsáidtear nuair a chraoladh teachtaireacht.
Dá airde an luach is ea is láidre an comhartha, ach is é an gléas is mó a chaitheann an chumhacht. Aistríonn an t-uimhriú go poist sa liosta seo a leanas de luachanna dBm (decibel milliwatt): -30, -20, -16, -12, -8, -4, 0, 4.
:param address: (seoladh) (default=0x75626974) ainm treallach, arna shloinneadh mar sheoladh 32-giotán, a úsáidtear chun paicéid atá ag teacht isteach a scagadh ag leibhéal na crua-earraí, gan ach iad siúd a mheaitseáil leis an seoladh a shocraigh tú a choinneáil.
Is é an réamhshocrú a úsáideann ardáin eile a bhaineann le micro:bit an socrú réamhshocraithe a úsáidtear anseo.
:param group: (grúpa) (default=0) luach 8-giotán (0-255) a úsáidtear leis an ``address`` agus teachtaireachtaí á scagadh.
Go coincheapúil, tá "seoladh" cosúil le seoladh tí / oifige agus tá "grúpa" cosúil leis an duine ag an seoladh sin ar mian leat do theachtaireacht a sheoladh chuige.
:param data_rate: (ráta sonraí) (réamhshocrú=``radio.RATE_1MBIT``) an luas ag a dtarlaíonn tréchur sonraí.
Is féidir a bheith ar cheann de na tairisigh seo a leanas a shainmhínítear sa mhodúl ``radio`` : ``RATE_250KBIT``, ``RATE_1MBIT`` nó ``RATE_2MBIT``.

If ``config`` is not called then the defaults described above are assumed."""
    ...

def reset() -> None:
    """Athshocraigh na socruithe dá luachanna réamhshocraithe. (athshocrú)

Example: ``radio.reset()``

The defaults as as per the ``config`` function above."""
    ...

def send_bytes(message: bytes) -> None:
    """Seolann seo teachtaireacht ina bhfuil bearta. (seol bearta)

Example: ``radio.send_bytes(b'hello')``

:param message: (teachtaireacht) Na bearta le seoladh."""
    ...

def receive_bytes() -> Optional[bytes]:
    """Faigh an chéad teachtaireacht eile isteach ar an scuaine teachtaireachtaí. (bearta a fháil)

Example: ``radio.receive_bytes()``

:return: The message bytes if any, otherwise ``None``."""
    ...

def receive_bytes_into(buffer: WriteableBuffer) -> Optional[int]:
    """Cóipeáil an chéad teachtaireacht isteach eile ar an scuaine teachtaireachta isteach i maolán. (bearta a fháil isteach i)

Example: ``radio.receive_bytes_info(buffer)``

:param buffer: (maolán) An maolán sprice. Tá an teachtaireacht teasctha má tá sé níos mó ná an maolán.
:return: ``None`` if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
    ...

def send(message: str) -> None:
    """Seolann seo teaghrán teachtaireachta. (seol)

Example: ``radio.send('hello')``

This is the equivalent of ``radio.send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
prepended to the front (to make it compatible with other platforms that target the micro:bit).

:param message: (teachtaireacht) An sreangán le seoladh."""
    ...

def receive() -> Optional[str]:
    """Oibríonn sé ar an mbealach céanna le ``receive_bytes`` ach filleann sé cibé rud a seoladh. (faigh)

Example: ``radio.receive()``

Equivalent to ``str(receive_bytes(), 'utf8')`` but with a check that the the first
three bytes are ``b'\x01\x00\x01'`` (to make it compatible with other platforms that
may target the micro:bit).

:return: The message with the prepended bytes stripped and converted to a string.

A ``ValueError`` exception is raised if conversion to string fails."""
    ...

def receive_full() -> Optional[Tuple[bytes, int, int]]:
    """Tuairisceáin tupla ina bhfuil trí luach a léiríonn an chéad teachtaireacht eile ag teacht isteach ar an scuaine teachtaireacht. (faigh iomlán)

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