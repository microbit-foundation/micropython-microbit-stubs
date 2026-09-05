"""Bioráin, íomhánna, fuaimeanna, teocht agus toirt."""
from typing import Any, Callable, List, Optional, Tuple, Union, overload
from _typeshed import ReadableBuffer
from . import accelerometer as accelerometer
from . import audio as audio
from . import compass as compass
from . import display as display
from . import i2c as i2c
from . import microphone as microphone
from . import speaker as speaker
from . import spi as spi
from . import uart as uart

def run_every(callback: Optional[Callable[[], None]]=None, days: int=0, h: int=0, min: int=0, s: int=0, ms: int=0) -> Callable[[Callable[[], None]], Callable[[], None]]:
    """Sceideal chun feidhm a rith ag an eatramh a shonraítear leis na hargóintí ama **V2 amháin**. (rith gach)

Example: ``run_every(my_logging, min=5)``

``run_every`` can be used in two ways:

As a Decorator - placed on top of the function to schedule. For example::

    @run_every(h=1, min=20, s=30, ms=50)
    def my_function():
        # Do something here

As a Function - passing the callback as a positional argument. For example::

    def my_function():
        # Do something here
    run_every(my_function, s=30)

Each argument corresponds to a different time unit and they are additive.
So ``run_every(min=1, s=30)`` schedules the callback every minute and a half.

When an exception is thrown inside the callback function it deschedules the
function. To avoid this you can catch exceptions with ``try/except``.

:param callback: Feidhm chun glaoch ag an eatramh a sholáthraítear. Fág ar lár agus é á úsáid mar mhaisitheoir.
:param days: (laethanta) Socraíonn sé an marc lae don sceidealú.
:param h: Socraíonn sé an marc uair an chloig don sceidealú.
:param min: (íos) Socraíonn sé an marc nóiméad don sceidealú.
:param s: Socraigh an dara marc don sceidealú.
:param ms: Socraíonn sé an marc milleasoicind don sceidealú."""

def panic(n: int) -> None:
    """Téigh isteach i mód scaoill. (scaoll)

Example: ``panic(127)``

:param n: Slánuimhir treallach <= 255 chun stádas a léiriú.

Requires restart."""

def reset() -> None:
    """Atosaigh an bord. (athshocrú)"""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """Athraíonn luach ó raon go raon slánuimhir. (scála)

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: (luach) Uimhir le tiontú.
:param from_: (ó) A tuple a shainmhíniú ar an raon a thiontú ó.
:param to: (chuig) A tuple a shainmhíniú ar an raon a thiontú go.
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """Athraíonn luach ó raon go raon snámhphointe. (scála)

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: (luach) Uimhir le tiontú.
:param from_: (ó) Tupla chun an raon le tiontú uaidh a shainiú.
:param to: (chuig) Tupla chun an raon le tiontú chuige a shainiú.
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """Fan le haghaidh milleasoicindí ``n`` . (codladh)

Example: ``sleep(1000)``

:param n: Líon na milleasoicindí le fanacht

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """Faigh am reatha an bhoird. (am reatha)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """Faigh teocht an micro:bit i gcéimeanna Celsius. (teocht)"""

def set_volume(v: int) -> None:
    """Socraigh an t-imleabhar. (socraigh an toirt)

Example: ``set_volume(127)``

:param v: luach idir 0 (íseal) agus 255 (ard).

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """An rang do na cnaipí ``button_a`` agus ``button_b``. (cnaipe)"""

    def is_pressed(self) -> bool:
        """Seiceáil an bhfuil an cnaipe brúite. (brúite)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """Seiceáil ar brúdh an cnaipe ó thosaigh an gléas nó an uair dheireanach a glaodh ar an modh seo. (brúdh)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """Faigh iomlán reatha na gcnaipí, agus athshocraíonn sé an t-iomlán seo
náid sula bhfillfidh tú. (faigh brúiteanna)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""An cnaipe ar chlé ``Button`` réad. (cnaipe a)"""
button_b: Button
"""An cnaipe ceart ``Button`` réad. (cnaipe b)"""

class MicroBitDigitalPin:
    """Biorán digiteach.

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """Faigh luach digiteach an bhioráin. (léigh digiteach)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """Socraigh luach digiteach an bhioráin. (scríobh digiteach)

Example: ``pin0.write_digital(1)``

:param value: (luach) 1 chun an pionna a shocrú ard nó 0 chun an pionna a shocrú íseal"""
        ...

    def set_pull(self, value: int) -> None:
        """Socraigh an staid tarraingthe go ceann de thrí luach féideartha: ``PULL_UP``, ``PULL_DOWN`` nó ``NO_PULL``. (tarraingt socraithe)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (luach) An staid tarraingthe ón bioráin ábhartha, m.sh. ``pin0.PULL_UP``."""
        ...

    def get_pull(self) -> int:
        """Faigh an stát tarraingt ar pionna. (faigh socraithe)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """Filleann an modh pionna. (mód faighte)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """Aschuir comhartha PWM ar an bioráin, agus an timthriall dleachta comhréireach le ``value``. (scríobh analógach)

Example: ``pin0.write_analog(254)``

:param value: (luach) Slánuimhir nó uimhir snámhphointe idir 0 (0% timthriall dleachta) agus 1023 (dleacht 100%)."""

    def set_analog_period(self, period: int) -> None:
        """Socraigh tréimhse an chomhartha PWM atá á haschur go dtí ``period`` ina milleasoicindí. (socraigh tréimhse analógach)

Example: ``pin0.set_analog_period(10)``

:param period: (tréimhse) An tréimhse ina milleasoicindí le luach bailí íosta de 1ms."""

    def set_analog_period_microseconds(self, period: int) -> None:
        """Socraigh tréimhse an chomhartha PWM atá á haschur go dtí ``period`` i micrishoicindí. (micreasoicindí tréimhse analógacha a shocrú)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (tréimhse) An tréimhse i micrishoicindí le íosluach bailí de 256µs."""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """Bioráin le gnéithe analógacha agus digiteacha."""

    def read_analog(self) -> int:
        """Léigh an voltas a chuirtear i bhfeidhm ar an biorán. (léigh analógach)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """Pionna le gnéithe analógacha, digiteacha agus tadhaill."""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """Seiceáil an bhfuil teagmháil á déanamh leis an biorán. (i dteagmháil)

Example: ``pin0.is_touched()``

The default touch mode for the pins on the edge connector is ``resistive``.
The default for the logo pin **V2** is ``capacitive``.

**Resistive touch**
This test is done by measuring how much resistance there is between the
pin and ground.  A low resistance gives a reading of ``True``.  To get
a reliable reading using a finger you may need to touch the ground pin
with another part of your body, for example your other hand.

**Capacitive touch**
This test is done by interacting with the electric field of a capacitor
using a finger as a conductor. `Capacitive touch
<https://www.allaboutcircuits.com/technical-articles/introduction-to-capacitive-touch-sensing>`_
does not require you to make a ground connection as part of a circuit.

:return: ``True`` if the pin is being touched with a finger, otherwise return ``False``."""
        ...

    def set_touch_mode(self, value: int) -> None:
        """Socraigh an modh tadhaill don pionna. (socraigh mód tadhaill)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (luach) ``CAPACITIVE`` nó ``RESISTIVE`` ón pionna ábhartha."""
        ...
pin0: MicroBitTouchPin
"""Pionna le gnéithe digiteacha, analógacha agus tadhaill. (biorán0)"""
pin1: MicroBitTouchPin
"""Bioráin le gnéithe digiteacha, analógacha agus tadhaill. (biorán1)"""
pin2: MicroBitTouchPin
"""Bioráin le gnéithe digiteacha, analógacha agus tadhaill. (biorán2)"""
pin3: MicroBitAnalogDigitalPin
"""Bioráin le gnéithe digiteacha agus analógacha. (biorán3)"""
pin4: MicroBitAnalogDigitalPin
"""Bioráin le gnéithe digiteacha agus analógacha. (biorán4)"""
pin5: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán5)"""
pin6: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán6)"""
pin7: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán7)"""
pin8: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán8)"""
pin9: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán9)"""
pin10: MicroBitAnalogDigitalPin
"""Bioráin le gnéithe digiteacha agus analógacha. (biorán10)"""
pin11: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán11)"""
pin12: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán12)"""
pin13: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán 13)"""
pin14: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán14)"""
pin15: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán15)"""
pin16: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán16)"""
pin19: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán19)"""
pin20: MicroBitDigitalPin
"""Bioráin le gnéithe digiteacha. (biorán20)"""
pin_logo: MicroBitTouchPin
"""Biorán lógó íogair do theagmháil ar aghaidh an micro:bit, atá socraithe de réir réamhshocraithe go mód tadhaill toilleasach. (lógó bioráin)"""
pin_speaker: MicroBitAnalogDigitalPin
"""Biorán chun an cainteoir micro:bit a sheoladh. (cainteoir bioráin)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """Íomhá le taispeáint ar an taispeáint micro:bit LED. (íomhá)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """Íomhá chroí. (croí)"""
    HEART_SMALL: Image
    """Íomhá bheag chroí. (croí beag)"""
    HAPPY: Image
    """Íomhá aghaidhe sona. (sásta)"""
    SMILE: Image
    """Íomhá béil ag gáire. (aoibh gháire)"""
    SAD: Image
    """Íomhá aghaidhe brónach. (brónach)"""
    CONFUSED: Image
    """Íomhá aghaidhe mearbhall. (mearbhall)"""
    ANGRY: Image
    """Íomhá aghaidh feargach. (feargach)"""
    ASLEEP: Image
    """Íomhá aghaidhe codlata. (ina chodladh)"""
    SURPRISED: Image
    """Íomhá aghaidhe ionadh. (ionadh)"""
    SILLY: Image
    """Íomhá aghaidh amaideach. (amaideach)"""
    FABULOUS: Image
    """Íomhá aghaidhe spéaclaí gréine. (iontach)"""
    MEH: Image
    """Íomhá aghaidhe neamhbhrúite."""
    YES: Image
    """Cuir tic leis an íomhá. (tá)"""
    NO: Image
    """Íomhá croise. (níl)"""
    CLOCK12: Image
    """Íomhá le líne dírithe ar 12 a chlog. (clog12)"""
    CLOCK11: Image
    """Íomhá le líne dírithe ar 11 a chlog. (clog11)"""
    CLOCK10: Image
    """Íomhá le líne dírithe ar 10 a chlog. (clog10)"""
    CLOCK9: Image
    """Íomhá le líne dírithe go dtí 9 a chlog. (clog9)"""
    CLOCK8: Image
    """Íomhá le líne dírithe go dtí 8 a chlog. (clog8)"""
    CLOCK7: Image
    """Íomhá le líne dírithe go dtí 7 a chlog. (clog7)"""
    CLOCK6: Image
    """Íomhá le líne ag díriú go dtí 6 a chlog. (clog6)"""
    CLOCK5: Image
    """Íomhá le líne dírithe go dtí 5 a chlog. (clog5)"""
    CLOCK4: Image
    """Íomhá le líne dírithe go dtí 4 a chlog. (clog4)"""
    CLOCK3: Image
    """Íomhá le líne dírithe go dtí 3 a chlog. (clog3)"""
    CLOCK2: Image
    """Íomhá le líne ag díriú go dtí 2 a chlog. (clog2)"""
    CLOCK1: Image
    """Íomhá le líne ag díriú go dtí 1 a chlog. (clog1)"""
    ARROW_N: Image
    """Íomhá na saigheade dírithe ó thuaidh. (saighead n)"""
    ARROW_NE: Image
    """Íomhá na saigheade dírithe soir ó thuaidh. (saighead ne)"""
    ARROW_E: Image
    """Íomhá na saigheade dírithe ar an taobh thoir. (saighead e)"""
    ARROW_SE: Image
    """Íomhá na saigheade dírithe soir ó dheas. (saighead se)"""
    ARROW_S: Image
    """Íomhá na saigheade dírithe ó dheas. (saighead s)"""
    ARROW_SW: Image
    """Íomhá na saigheade dírithe siar ó dheas. (saighead sw)"""
    ARROW_W: Image
    """Íomhá den tsaighead atá dírithe siar. (saighead w)"""
    ARROW_NW: Image
    """Íomhá na saigheade dírithe siar ó thuaidh. (saighead nw)"""
    TRIANGLE: Image
    """Íomhá de thriantán ag pointeáil suas. (triantán)"""
    TRIANGLE_LEFT: Image
    """Íomhá de thriantán sa chúinne ar chlé. (triantán ar chlé)"""
    CHESSBOARD: Image
    """Soilse LEDs malartacha i bpatrún clár fichille. (clár fichille)"""
    DIAMOND: Image
    """Íomhá diamant. (diamant)"""
    DIAMOND_SMALL: Image
    """Íomhá diamant beag. (diamant beag)"""
    SQUARE: Image
    """Íomhá cearnóg. (cearnóg)"""
    SQUARE_SMALL: Image
    """Íomhá beag cearnach. (cearnach beag)"""
    RABBIT: Image
    """Íomhá coinín. (coinín)"""
    COW: Image
    """Íomhá bó. (bó)"""
    MUSIC_CROTCHET: Image
    """Íomhá nóta cróise. (croiséad ceoil)"""
    MUSIC_QUAVER: Image
    """Creathán nóta íomhá. (cuais cheoil)"""
    MUSIC_QUAVERS: Image
    """Íomhá de nótaí péire ochtú comhartha. (cuacha ceoil)"""
    PITCHFORK: Image
    """Íomhá forc pice. (forc-pice)"""
    XMAS: Image
    """Íomhá crann Nollag. (nollag)"""
    PACMAN: Image
    """Íomhá carachtar stuara PAC-Man."""
    TARGET: Image
    """Íomhá sprice. (sprioc)"""
    TSHIRT: Image
    """Íomhá T-léine. (léine-t)"""
    ROLLERSKATE: Image
    """Íomhá scátáil-rollála. (scátáil-rollála)"""
    DUCK: Image
    """Íomhá lacha. (lacha)"""
    HOUSE: Image
    """Íomhá tí. (teach)"""
    TORTOISE: Image
    """Íomhá turtar. (toirtís)"""
    BUTTERFLY: Image
    """Íomhá féileacán. (féileacán)"""
    STICKFIGURE: Image
    """Bata íomhá figiúr. (figiúr-maide)"""
    GHOST: Image
    """Íomhá taibhse. (taibhse)"""
    SWORD: Image
    """Íomhá chlaíomh. (claíomh)"""
    GIRAFFE: Image
    """Íomhá sioráf. (sioráf)"""
    SKULL: Image
    """Íomhá cloigeann. (cloigeann)"""
    UMBRELLA: Image
    """Íomhá scáth fearthainne. (scáth fearthainne)"""
    SNAKE: Image
    """Íomhá nathair. (nathair)"""
    SCISSORS: Image
    """Íomhá siosúr. (siosúr)"""
    ALL_CLOCKS: List[Image]
    """Liosta ina bhfuil na híomhánna CLOCK_ go léir in ord. (gach clog)"""
    ALL_ARROWS: List[Image]
    """Liosta ina bhfuil na híomhánna ARROW_ go léir in ord. (gach saighead)"""

    @overload
    def __init__(self, string: str) -> None:
        """Cruthaigh íomhá ó theaghrán ag cur síos ar na soilse atá lasta.

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (teaghrán) An teaghrán ag cur síos ar an íomhá."""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """Cruthaigh íomhá fholamh le colúin ``width`` agus sraitheanna ``height`` .

:param width: (leithead) Leithead roghnach na híomhá
:param height: (airde) Airde roghnach na híomhá
:param buffer: (maolán) Eagar roghnach nó bearta de ``width``×``height`` slánuimhreacha i raon 0-9 chun an íomhá a thúsú

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """Faigh líon na gcolún. (leithead)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """Faigh líon na sraitheanna. (airde)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """Socraigh gile picteilín. (socraigh picteilín)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: Uimhir an cholúin
:param y: Uimhir an ró
:param value: (luach) An ghile mar shlánuimhir idir 0 (dorcha) agus 9 (geal)

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """Faigh gile picteilín. (faigh picteilín)

Example: ``my_image.get_pixel(0, 0)``

:param x: Uimhir an cholúin
:param y: Uimhir na sraithe
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """Cruthaigh íomhá nua tríd an bpictiúr ar chlé a athrú. (shift ar chlé)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: Líon na gcolún atá le haistriú ag
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """Cruthaigh íomhá nua tríd an bpictiúr a athrú ar dheis. (shift ar dheis)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: Líon na gcolún le haistriú
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """Cruthaigh íomhá nua tríd an bpictiúr a athrú suas. (shift suas)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: Líon na rónna le hathrú ag
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """Cruthaigh íomhá nua tríd an bpictiúr a aistriú síos. (shift síos)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: Líon na rónna le haistriú
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """Cruthaigh íomhá nua tríd an bpictiúr a bearradh. (barr)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: An colún fritháireamh barr
:param y: An ró fritháireamh barr
:param w: An leithead barr
:param h: An airde barr
:return: The new image"""
        ...

    def copy(self) -> Image:
        """Cruthaigh cóip chruinn den íomhá. (cóip)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """Cruthaigh íomhá nua trí ghile na bpicteilíní a inbhéartú sa
íomhá foinseach. (inbhéartaithe)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """Socraigh gile na bpicteilíní go léir san íomhá. (líon)

Example: ``my_image.fill(5)``

:param value: (luach) An gile nua mar uimhir idir 0 (dorcha) agus 9 (geal).

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """Cóipeáil limistéar ó íomhá eile isteach san íomhá seo.

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: An íomhá fhoinseach
:param x: Fritháireamh an cholúin tosaigh san íomhá fhoinseach
:param y: Fritháireamh an ró tosaigh san íomhá foinseach
:param w: Líon na gcolún le cóipeáil
:param h: Líon na rónna le cóipeáil
:param xdest: Fritháireamh an cholúin le mionathrú san íomhá seo
:param ydest: Fritháireamh an ró le mionathrú san íomhá seo

Pixels outside the source image are treated as having a brightness of 0.

``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()``
and ``crop()`` can are all implemented by using ``blit()``.

For example, img.crop(x, y, w, h) can be implemented as::

    def crop(self, x, y, w, h):
        res = Image(w, h)
        res.blit(self, x, y, w, h)
        return res"""
        ...

    def __repr__(self) -> str:
        """Faigh léiriú teaghrán dlúth ar an íomhá."""
        ...

    def __str__(self) -> str:
        """Faigh léiriú teaghrán inléite ar an íomhá."""
        ...

    def __add__(self, other: Image) -> Image:
        """Cruthaigh íomhá nua trí na luachanna gile ón dá cheann a chur leis
íomhánna do gach picteilín. (suimigh)

Example: ``Image.HEART + Image.HAPPY``

:param other: (eile) An íomhá le cur leis."""
        ...

    def __sub__(self, other: Image) -> Image:
        """Cruthaigh íomhá nua trí luachanna gile an
íomhá eile ón íomhá seo.

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (eile) An íomhá a dhealú."""
        ...

    def __mul__(self, n: float) -> Image:
        """Cruthaigh íomhá nua trí ghile gach picteilín a iolrú faoi
``n``.

Example: ``Image.HEART * 0.5``

:param n: An luach a iolrú faoi."""
        ...

    def __truediv__(self, n: float) -> Image:
        """Cruthaigh íomhá nua trí ghile gach picteilín a roinnt ar
``n``.

Example: ``Image.HEART / 2``

:param n: An luach a roinnt ar."""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """Léiríonn sé aistriú imeachtaí fuaime, ó ``quiet`` go ``loud`` cosúil le bualadh nó béicíl. (ard)"""
    QUIET: SoundEvent
    """Léiríonn sé seo aistriú imeachtaí fuaime, ó ``loud`` go ``quiet`` cosúil le ceol labhartha nó cúlra. (ciúin)"""

class Sound:
    """Is féidir na fuaimeanna tógtha a ghlaoch ag baint úsáide as ``audio.play(Sound.NAME)``. (fuaim)"""
    GIGGLE: Sound
    """Fuaim scig-gháire. (scig-gháire)"""
    HAPPY: Sound
    """Fuaim shona. (sásta)"""
    HELLO: Sound
    """Fuaime beannacht. (dia duit)"""
    MYSTERIOUS: Sound
    """Fuaim mhistéireach. (mistéireach)"""
    SAD: Sound
    """Fuaim bhrónach. (brónach)"""
    SLIDE: Sound
    """Fuaim sleamhnáin. (sleamhnán)"""
    SOARING: Sound
    """Fuaim téagartha. (téagartha)"""
    SPRING: Sound
    """Fuaim an earraigh. (an t-earrach)"""
    TWINKLE: Sound
    """Fuaim drithligh. (drithligh)"""
    YAWN: Sound
    """Fuaim méanfach. (méanfach)"""