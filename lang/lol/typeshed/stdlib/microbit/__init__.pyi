"""crwdns329148:0crwdne329148:0 (crwdns329146:0crwdne329146:0)"""
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
    """crwdns335788:0crwdne335788:0 (crwdns329150:0crwdne329150:0)

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

:param callback: (crwdns329154:0crwdne329154:0) crwdns335790:0crwdne335790:0
:param days: (crwdns329158:0crwdne329158:0) crwdns335792:0crwdne335792:0
:param h: (crwdns329162:0crwdne329162:0) crwdns335794:0crwdne335794:0
:param min: (crwdns329166:0crwdne329166:0) crwdns335796:0crwdne335796:0
:param s: (crwdns329174:0crwdne329174:0) crwdns335800:0crwdne335800:0
:param ms: (crwdns329170:0crwdne329170:0) crwdns335798:0crwdne335798:0"""

def panic(n: int) -> None:
    """crwdns329180:0crwdne329180:0 (crwdns329178:0crwdne329178:0)

Example: ``panic(127)``

:param n: (crwdns329182:0crwdne329182:0) crwdns329184:0crwdne329184:0

Requires restart."""

def reset() -> None:
    """crwdns329188:0crwdne329188:0 (crwdns329186:0crwdne329186:0)"""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[int, int]) -> int:
    """crwdns336078:0crwdne336078:0 (crwdns336076:0crwdne336076:0)

Example: ``volume = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))``

For example, to convert an accelerometer X value to a speaker volume.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.

    temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

:param value: (crwdns336088:0crwdne336088:0) crwdns336090:0crwdne336090:0
:param from_: (crwdns336080:0crwdne336080:0) crwdns336082:0crwdne336082:0
:param to: (crwdns336084:0crwdne336084:0) crwdns336086:0crwdne336086:0
:return: The ``value`` converted to the ``to`` range."""

@overload
def scale(value: float, from_: Tuple[float, float], to: Tuple[float, float]) -> float:
    """crwdns336094:0crwdne336094:0 (crwdns336092:0crwdne336092:0)

Example: ``temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))``

For example, to convert temperature from a Celsius scale to Fahrenheit.

If one of the numbers in the ``to`` parameter is a floating point
(i.e a decimal number like ``10.0``), this function will return a
floating point number.
If they are both integers (i.e ``10``), it will return an integer::

    returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

:param value: (crwdns336104:0crwdne336104:0) crwdns336106:0crwdne336106:0
:param from_: (crwdns336096:0crwdne336096:0) crwdns336098:0crwdne336098:0
:param to: (crwdns336100:0crwdne336100:0) crwdns336102:0crwdne336102:0
:return: The ``value`` converted to the ``to`` range."""

def sleep(n: float) -> None:
    """crwdns329192:0``n``crwdne329192:0 (crwdns329190:0crwdne329190:0)

Example: ``sleep(1000)``

:param n: (crwdns329194:0crwdne329194:0) crwdns329196:0crwdne329196:0

One second is 1000 milliseconds, so::

    microbit.sleep(1000)

will pause the execution for one second."""

def running_time() -> int:
    """crwdns329200:0crwdne329200:0 (crwdns329198:0crwdne329198:0)

:return: The number of milliseconds since the board was switched on or restarted."""

def temperature() -> int:
    """crwdns329204:0crwdne329204:0 (crwdns329202:0crwdne329202:0)"""

def set_volume(v: int) -> None:
    """crwdns329208:0crwdne329208:0 (crwdns329206:0crwdne329206:0)

Example: ``set_volume(127)``

:param v: (crwdns329210:0crwdne329210:0) crwdns329212:0crwdne329212:0

Out of range values will be clamped to 0 or 255.

**V2** only."""
    ...

class Button:
    """crwdns329216:0``button_a``crwdnd329216:0``button_b``crwdne329216:0 (crwdns329214:0crwdne329214:0)"""

    def is_pressed(self) -> bool:
        """crwdns329220:0crwdne329220:0 (crwdns329218:0crwdne329218:0)

:return: ``True`` if the specified button ``button`` is pressed, and ``False`` otherwise."""
        ...

    def was_pressed(self) -> bool:
        """crwdns329224:0crwdne329224:0 (crwdns329222:0crwdne329222:0)

Calling this method will clear the press state so
that the button must be pressed again before this method will return
``True`` again.

:return: ``True`` if the specified button ``button`` was pressed, and ``False`` otherwise"""
        ...

    def get_presses(self) -> int:
        """crwdns329228:0crwdne329228:0 (crwdns329226:0crwdne329226:0)

:return: The number of presses since the device started or the last time this method was called"""
        ...
button_a: Button
"""crwdns329232:0``Button``crwdne329232:0 (crwdns329230:0crwdne329230:0)"""
button_b: Button
"""crwdns329236:0``Button``crwdne329236:0 (crwdns329234:0crwdne329234:0)"""

class MicroBitDigitalPin:
    """crwdns329240:0crwdne329240:0 (crwdns329238:0crwdne329238:0)

Some pins support analog and touch features using the ``MicroBitAnalogDigitalPin`` and ``MicroBitTouchPin`` subclasses."""
    NO_PULL: int
    PULL_UP: int
    PULL_DOWN: int

    def read_digital(self) -> int:
        """crwdns329244:0crwdne329244:0 (crwdns329242:0crwdne329242:0)

Example: ``value = pin0.read_digital()``

:return: 1 if the pin is high, and 0 if it's low."""
        ...

    def write_digital(self, value: int) -> None:
        """crwdns329248:0crwdne329248:0 (crwdns329246:0crwdne329246:0)

Example: ``pin0.write_digital(1)``

:param value: (crwdns329250:0crwdne329250:0) crwdns329252:0crwdne329252:0"""
        ...

    def set_pull(self, value: int) -> None:
        """crwdns329256:0``PULL_UP``crwdnd329256:0``PULL_DOWN``crwdnd329256:0``NO_PULL``crwdne329256:0 (crwdns329254:0crwdne329254:0)

Example: ``pin0.set_pull(pin0.PULL_UP)``

:param value: (crwdns329258:0crwdne329258:0) crwdns329260:0``pin0.PULL_UP``crwdne329260:0"""
        ...

    def get_pull(self) -> int:
        """crwdns329264:0crwdne329264:0 (crwdns329262:0crwdne329262:0)

Example: ``pin0.get_pull()``

:return: ``NO_PULL``, ``PULL_DOWN``, or ``PULL_UP``

These are set using the ``set_pull()`` method or automatically configured
when a pin mode requires it."""
        ...

    def get_mode(self) -> str:
        """crwdns329268:0crwdne329268:0 (crwdns329266:0crwdne329266:0)

Example: ``pin0.get_mode()``

When a pin is used for a specific function, like
writing a digital value, or reading an analog value, the pin mode
changes.

:return: ``"unused"``, ``"analog"``, ``"read_digital"``, ``"write_digital"``, ``"display"``, ``"button"``, ``"music"``, ``"audio"``, ``"touch"``, ``"i2c"``, or ``"spi"``"""
        ...

    def write_analog(self, value: int) -> None:
        """crwdns329272:0``value``crwdne329272:0 (crwdns329270:0crwdne329270:0)

Example: ``pin0.write_analog(254)``

:param value: (crwdns329274:0crwdne329274:0) crwdns329276:0crwdne329276:0"""

    def set_analog_period(self, period: int) -> None:
        """crwdns329280:0``period``crwdne329280:0 (crwdns329278:0crwdne329278:0)

Example: ``pin0.set_analog_period(10)``

:param period: (crwdns329282:0crwdne329282:0) crwdns329284:0crwdne329284:0"""

    def set_analog_period_microseconds(self, period: int) -> None:
        """crwdns329288:0``period``crwdne329288:0 (crwdns329286:0crwdne329286:0)

Example: ``pin0.set_analog_period_microseconds(512)``

:param period: (crwdns329290:0crwdne329290:0) crwdns329292:0crwdne329292:0"""

class MicroBitAnalogDigitalPin(MicroBitDigitalPin):
    """crwdns329296:0crwdne329296:0 (crwdns329294:0crwdne329294:0)"""

    def read_analog(self) -> int:
        """crwdns329300:0crwdne329300:0 (crwdns329298:0crwdne329298:0)

Example: ``pin0.read_analog()``

:return: An integer between 0 (meaning 0V) and 1023 (meaning 3.3V)."""

class MicroBitTouchPin(MicroBitAnalogDigitalPin):
    """crwdns329304:0crwdne329304:0 (crwdns329302:0crwdne329302:0)"""
    CAPACITIVE: int
    RESISTIVE: int

    def is_touched(self) -> bool:
        """crwdns329308:0crwdne329308:0 (crwdns329306:0crwdne329306:0)

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
        """crwdns329312:0crwdne329312:0 (crwdns329310:0crwdne329310:0)

Example: ``pin0.set_touch_mode(pin0.CAPACITIVE)``

The default touch mode for the pins on the edge connector is
``resistive``. The default for the logo pin **V2** is ``capacitive``.

:param value: (crwdns329314:0crwdne329314:0) crwdns329316:0``CAPACITIVE``crwdnd329316:0``RESISTIVE``crwdne329316:0"""
        ...
pin0: MicroBitTouchPin
"""crwdns329320:0crwdne329320:0 (crwdns329318:0crwdne329318:0)"""
pin1: MicroBitTouchPin
"""crwdns329324:0crwdne329324:0 (crwdns329322:0crwdne329322:0)"""
pin2: MicroBitTouchPin
"""crwdns329328:0crwdne329328:0 (crwdns329326:0crwdne329326:0)"""
pin3: MicroBitAnalogDigitalPin
"""crwdns329332:0crwdne329332:0 (crwdns329330:0crwdne329330:0)"""
pin4: MicroBitAnalogDigitalPin
"""crwdns329336:0crwdne329336:0 (crwdns329334:0crwdne329334:0)"""
pin5: MicroBitDigitalPin
"""crwdns329340:0crwdne329340:0 (crwdns329338:0crwdne329338:0)"""
pin6: MicroBitDigitalPin
"""crwdns329344:0crwdne329344:0 (crwdns329342:0crwdne329342:0)"""
pin7: MicroBitDigitalPin
"""crwdns329348:0crwdne329348:0 (crwdns329346:0crwdne329346:0)"""
pin8: MicroBitDigitalPin
"""crwdns329352:0crwdne329352:0 (crwdns329350:0crwdne329350:0)"""
pin9: MicroBitDigitalPin
"""crwdns329356:0crwdne329356:0 (crwdns329354:0crwdne329354:0)"""
pin10: MicroBitAnalogDigitalPin
"""crwdns329360:0crwdne329360:0 (crwdns329358:0crwdne329358:0)"""
pin11: MicroBitDigitalPin
"""crwdns329364:0crwdne329364:0 (crwdns329362:0crwdne329362:0)"""
pin12: MicroBitDigitalPin
"""crwdns329368:0crwdne329368:0 (crwdns329366:0crwdne329366:0)"""
pin13: MicroBitDigitalPin
"""crwdns329372:0crwdne329372:0 (crwdns329370:0crwdne329370:0)"""
pin14: MicroBitDigitalPin
"""crwdns329376:0crwdne329376:0 (crwdns329374:0crwdne329374:0)"""
pin15: MicroBitDigitalPin
"""crwdns329380:0crwdne329380:0 (crwdns329378:0crwdne329378:0)"""
pin16: MicroBitDigitalPin
"""crwdns329384:0crwdne329384:0 (crwdns329382:0crwdne329382:0)"""
pin19: MicroBitDigitalPin
"""crwdns329388:0crwdne329388:0 (crwdns329386:0crwdne329386:0)"""
pin20: MicroBitDigitalPin
"""crwdns329392:0crwdne329392:0 (crwdns329390:0crwdne329390:0)"""
pin_logo: MicroBitTouchPin
"""crwdns329396:0crwdne329396:0 (crwdns329394:0crwdne329394:0)"""
pin_speaker: MicroBitAnalogDigitalPin
"""crwdns329400:0crwdne329400:0 (crwdns329398:0crwdne329398:0)

This API is intended only for use in Pulse-Width Modulation pin operations e.g. pin_speaker.write_analog(128).
"""

class Image:
    """crwdns329404:0crwdne329404:0 (crwdns329402:0crwdne329402:0)

Given an image object it's possible to display it via the ``display`` API::

    display.show(Image.HAPPY)"""
    HEART: Image
    """crwdns329408:0crwdne329408:0 (crwdns329406:0crwdne329406:0)"""
    HEART_SMALL: Image
    """crwdns329412:0crwdne329412:0 (crwdns329410:0crwdne329410:0)"""
    HAPPY: Image
    """crwdns329416:0crwdne329416:0 (crwdns329414:0crwdne329414:0)"""
    SMILE: Image
    """crwdns329420:0crwdne329420:0 (crwdns329418:0crwdne329418:0)"""
    SAD: Image
    """crwdns329424:0crwdne329424:0 (crwdns329422:0crwdne329422:0)"""
    CONFUSED: Image
    """crwdns329428:0crwdne329428:0 (crwdns329426:0crwdne329426:0)"""
    ANGRY: Image
    """crwdns329432:0crwdne329432:0 (crwdns329430:0crwdne329430:0)"""
    ASLEEP: Image
    """crwdns329436:0crwdne329436:0 (crwdns329434:0crwdne329434:0)"""
    SURPRISED: Image
    """crwdns329440:0crwdne329440:0 (crwdns329438:0crwdne329438:0)"""
    SILLY: Image
    """crwdns329444:0crwdne329444:0 (crwdns329442:0crwdne329442:0)"""
    FABULOUS: Image
    """crwdns329448:0crwdne329448:0 (crwdns329446:0crwdne329446:0)"""
    MEH: Image
    """crwdns329452:0crwdne329452:0 (crwdns329450:0crwdne329450:0)"""
    YES: Image
    """crwdns329456:0crwdne329456:0 (crwdns329454:0crwdne329454:0)"""
    NO: Image
    """crwdns329460:0crwdne329460:0 (crwdns329458:0crwdne329458:0)"""
    CLOCK12: Image
    """crwdns329464:0crwdne329464:0 (crwdns329462:0crwdne329462:0)"""
    CLOCK11: Image
    """crwdns329468:0crwdne329468:0 (crwdns329466:0crwdne329466:0)"""
    CLOCK10: Image
    """crwdns329472:0crwdne329472:0 (crwdns329470:0crwdne329470:0)"""
    CLOCK9: Image
    """crwdns329476:0crwdne329476:0 (crwdns329474:0crwdne329474:0)"""
    CLOCK8: Image
    """crwdns329480:0crwdne329480:0 (crwdns329478:0crwdne329478:0)"""
    CLOCK7: Image
    """crwdns329484:0crwdne329484:0 (crwdns329482:0crwdne329482:0)"""
    CLOCK6: Image
    """crwdns329488:0crwdne329488:0 (crwdns329486:0crwdne329486:0)"""
    CLOCK5: Image
    """crwdns329492:0crwdne329492:0 (crwdns329490:0crwdne329490:0)"""
    CLOCK4: Image
    """crwdns329496:0crwdne329496:0 (crwdns329494:0crwdne329494:0)"""
    CLOCK3: Image
    """crwdns329500:0crwdne329500:0 (crwdns329498:0crwdne329498:0)"""
    CLOCK2: Image
    """crwdns329504:0crwdne329504:0 (crwdns329502:0crwdne329502:0)"""
    CLOCK1: Image
    """crwdns329508:0crwdne329508:0 (crwdns329506:0crwdne329506:0)"""
    ARROW_N: Image
    """crwdns329512:0crwdne329512:0 (crwdns329510:0crwdne329510:0)"""
    ARROW_NE: Image
    """crwdns329516:0crwdne329516:0 (crwdns329514:0crwdne329514:0)"""
    ARROW_E: Image
    """crwdns329520:0crwdne329520:0 (crwdns329518:0crwdne329518:0)"""
    ARROW_SE: Image
    """crwdns329524:0crwdne329524:0 (crwdns329522:0crwdne329522:0)"""
    ARROW_S: Image
    """crwdns329528:0crwdne329528:0 (crwdns329526:0crwdne329526:0)"""
    ARROW_SW: Image
    """crwdns329532:0crwdne329532:0 (crwdns329530:0crwdne329530:0)"""
    ARROW_W: Image
    """crwdns329536:0crwdne329536:0 (crwdns329534:0crwdne329534:0)"""
    ARROW_NW: Image
    """crwdns329540:0crwdne329540:0 (crwdns329538:0crwdne329538:0)"""
    TRIANGLE: Image
    """crwdns329544:0crwdne329544:0 (crwdns329542:0crwdne329542:0)"""
    TRIANGLE_LEFT: Image
    """crwdns329548:0crwdne329548:0 (crwdns329546:0crwdne329546:0)"""
    CHESSBOARD: Image
    """crwdns329552:0crwdne329552:0 (crwdns329550:0crwdne329550:0)"""
    DIAMOND: Image
    """crwdns329556:0crwdne329556:0 (crwdns329554:0crwdne329554:0)"""
    DIAMOND_SMALL: Image
    """crwdns329560:0crwdne329560:0 (crwdns329558:0crwdne329558:0)"""
    SQUARE: Image
    """crwdns329564:0crwdne329564:0 (crwdns329562:0crwdne329562:0)"""
    SQUARE_SMALL: Image
    """crwdns329568:0crwdne329568:0 (crwdns329566:0crwdne329566:0)"""
    RABBIT: Image
    """crwdns329572:0crwdne329572:0 (crwdns329570:0crwdne329570:0)"""
    COW: Image
    """crwdns329576:0crwdne329576:0 (crwdns329574:0crwdne329574:0)"""
    MUSIC_CROTCHET: Image
    """crwdns329580:0crwdne329580:0 (crwdns329578:0crwdne329578:0)"""
    MUSIC_QUAVER: Image
    """crwdns329584:0crwdne329584:0 (crwdns329582:0crwdne329582:0)"""
    MUSIC_QUAVERS: Image
    """crwdns329588:0crwdne329588:0 (crwdns329586:0crwdne329586:0)"""
    PITCHFORK: Image
    """crwdns329592:0crwdne329592:0 (crwdns329590:0crwdne329590:0)"""
    XMAS: Image
    """crwdns329596:0crwdne329596:0 (crwdns329594:0crwdne329594:0)"""
    PACMAN: Image
    """crwdns329600:0crwdne329600:0 (crwdns329598:0crwdne329598:0)"""
    TARGET: Image
    """crwdns329604:0crwdne329604:0 (crwdns329602:0crwdne329602:0)"""
    TSHIRT: Image
    """crwdns329608:0crwdne329608:0 (crwdns329606:0crwdne329606:0)"""
    ROLLERSKATE: Image
    """crwdns329612:0crwdne329612:0 (crwdns329610:0crwdne329610:0)"""
    DUCK: Image
    """crwdns329616:0crwdne329616:0 (crwdns329614:0crwdne329614:0)"""
    HOUSE: Image
    """crwdns329620:0crwdne329620:0 (crwdns329618:0crwdne329618:0)"""
    TORTOISE: Image
    """crwdns329624:0crwdne329624:0 (crwdns329622:0crwdne329622:0)"""
    BUTTERFLY: Image
    """crwdns329628:0crwdne329628:0 (crwdns329626:0crwdne329626:0)"""
    STICKFIGURE: Image
    """crwdns329632:0crwdne329632:0 (crwdns329630:0crwdne329630:0)"""
    GHOST: Image
    """crwdns329636:0crwdne329636:0 (crwdns329634:0crwdne329634:0)"""
    SWORD: Image
    """crwdns329640:0crwdne329640:0 (crwdns329638:0crwdne329638:0)"""
    GIRAFFE: Image
    """crwdns329644:0crwdne329644:0 (crwdns329642:0crwdne329642:0)"""
    SKULL: Image
    """crwdns329648:0crwdne329648:0 (crwdns329646:0crwdne329646:0)"""
    UMBRELLA: Image
    """crwdns329652:0crwdne329652:0 (crwdns329650:0crwdne329650:0)"""
    SNAKE: Image
    """crwdns329656:0crwdne329656:0 (crwdns329654:0crwdne329654:0)"""
    SCISSORS: Image
    """crwdns335820:0crwdne335820:0 (crwdns335818:0crwdne335818:0)"""
    ALL_CLOCKS: List[Image]
    """crwdns329660:0crwdne329660:0 (crwdns329658:0crwdne329658:0)"""
    ALL_ARROWS: List[Image]
    """crwdns329664:0crwdne329664:0 (crwdns329662:0crwdne329662:0)"""

    @overload
    def __init__(self, string: str) -> None:
        """crwdns329668:0crwdne329668:0 (crwdns329666:0crwdne329666:0)

``string`` has to consist of digits 0-9 arranged into lines,
describing the image, for example::

    image = Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")

will create a 5×5 image of an X. The end of a line is indicated by a
colon. It's also possible to use newlines (\\n) insead of the colons.

:param string: (crwdns329670:0crwdne329670:0) crwdns329672:0crwdne329672:0"""
        ...

    @overload
    def __init__(self, width: int=5, height: int=5, buffer: ReadableBuffer=None) -> None:
        """crwdns329676:0``width``crwdnd329676:0``height``crwdne329676:0 (crwdns329674:0crwdne329674:0)

:param width: (crwdns329686:0crwdne329686:0) crwdns329688:0crwdne329688:0
:param height: (crwdns329682:0crwdne329682:0) crwdns329684:0crwdne329684:0
:param buffer: (crwdns329678:0crwdne329678:0) crwdns329680:0``width``crwdnd329680:0``height``crwdne329680:0

Examples::

    Image(2, 2, b'\x08\x08\x08\x08')
    Image(2, 2, bytearray([9,9,9,9]))

These create 2 x 2 pixel images at full brightness."""
        ...

    def width(self) -> int:
        """crwdns329692:0crwdne329692:0 (crwdns329690:0crwdne329690:0)

:return: The number of columns in the image"""
        ...

    def height(self) -> int:
        """crwdns329696:0crwdne329696:0 (crwdns329694:0crwdne329694:0)

:return: The number of rows in the image"""
        ...

    def set_pixel(self, x: int, y: int, value: int) -> None:
        """crwdns329700:0crwdne329700:0 (crwdns329698:0crwdne329698:0)

Example: ``my_image.set_pixel(0, 0, 9)``

:param x: (crwdns329706:0crwdne329706:0) crwdns329708:0crwdne329708:0
:param y: (crwdns329710:0crwdne329710:0) crwdns329712:0crwdne329712:0
:param value: (crwdns329702:0crwdne329702:0) crwdns329704:0crwdne329704:0

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def get_pixel(self, x: int, y: int) -> int:
        """crwdns329716:0crwdne329716:0 (crwdns329714:0crwdne329714:0)

Example: ``my_image.get_pixel(0, 0)``

:param x: (crwdns329718:0crwdne329718:0) crwdns329720:0crwdne329720:0
:param y: (crwdns329722:0crwdne329722:0) crwdns329724:0crwdne329724:0
:return: The brightness as an integer between 0 and 9."""
        ...

    def shift_left(self, n: int) -> Image:
        """crwdns329728:0crwdne329728:0 (crwdns329726:0crwdne329726:0)

Example: ``Image.HEART_SMALL.shift_left(1)``

:param n: (crwdns329730:0crwdne329730:0) crwdns329732:0crwdne329732:0
:return: The shifted image"""
        ...

    def shift_right(self, n: int) -> Image:
        """crwdns329736:0crwdne329736:0 (crwdns329734:0crwdne329734:0)

Example: ``Image.HEART_SMALL.shift_right(1)``

:param n: (crwdns329738:0crwdne329738:0) crwdns329740:0crwdne329740:0
:return: The shifted image"""
        ...

    def shift_up(self, n: int) -> Image:
        """crwdns329744:0crwdne329744:0 (crwdns329742:0crwdne329742:0)

Example: ``Image.HEART_SMALL.shift_up(1)``

:param n: (crwdns329746:0crwdne329746:0) crwdns329748:0crwdne329748:0
:return: The shifted image"""
        ...

    def shift_down(self, n: int) -> Image:
        """crwdns329752:0crwdne329752:0 (crwdns329750:0crwdne329750:0)

Example: ``Image.HEART_SMALL.shift_down(1)``

:param n: (crwdns329754:0crwdne329754:0) crwdns329756:0crwdne329756:0
:return: The shifted image"""
        ...

    def crop(self, x: int, y: int, w: int, h: int) -> Image:
        """crwdns329760:0crwdne329760:0 (crwdns329758:0crwdne329758:0)

Example: ``Image.HEART.crop(1, 1, 3, 3)``

:param x: (crwdns329770:0crwdne329770:0) crwdns329772:0crwdne329772:0
:param y: (crwdns329774:0crwdne329774:0) crwdns329776:0crwdne329776:0
:param w: (crwdns329766:0crwdne329766:0) crwdns329768:0crwdne329768:0
:param h: (crwdns329762:0crwdne329762:0) crwdns329764:0crwdne329764:0
:return: The new image"""
        ...

    def copy(self) -> Image:
        """crwdns329780:0crwdne329780:0 (crwdns329778:0crwdne329778:0)

Example: ``Image.HEART.copy()``

:return: The new image"""
        ...

    def invert(self) -> Image:
        """crwdns329784:0crwdne329784:0 (crwdns329782:0crwdne329782:0)

Example: ``Image.SMALL_HEART.invert()``

:return: The new image."""
        ...

    def fill(self, value: int) -> None:
        """crwdns329788:0crwdne329788:0 (crwdns329786:0crwdne329786:0)

Example: ``my_image.fill(5)``

:param value: (crwdns329790:0crwdne329790:0) crwdns329792:0crwdne329792:0

This method will raise an exception when called on any of the built-in
read-only images, like ``Image.HEART``."""
        ...

    def blit(self, src: Image, x: int, y: int, w: int, h: int, xdest: int=0, ydest: int=0) -> None:
        """crwdns329796:0crwdne329796:0 (crwdns329794:0crwdne329794:0)

Example: ``my_image.blit(Image.HEART, 1, 1, 3, 3, 1, 1)``

:param src: (crwdns329802:0crwdne329802:0) crwdns329804:0crwdne329804:0
:param x: (crwdns329810:0crwdne329810:0) crwdns329812:0crwdne329812:0
:param y: (crwdns329818:0crwdne329818:0) crwdns329820:0crwdne329820:0
:param w: (crwdns329806:0crwdne329806:0) crwdns329808:0crwdne329808:0
:param h: (crwdns329798:0crwdne329798:0) crwdns329800:0crwdne329800:0
:param xdest: (crwdns329814:0crwdne329814:0) crwdns329816:0crwdne329816:0
:param ydest: (crwdns329822:0crwdne329822:0) crwdns329824:0crwdne329824:0

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
        """crwdns329828:0crwdne329828:0 (crwdns329826:0crwdne329826:0)"""
        ...

    def __str__(self) -> str:
        """crwdns329832:0crwdne329832:0 (crwdns329830:0crwdne329830:0)"""
        ...

    def __add__(self, other: Image) -> Image:
        """crwdns329836:0crwdne329836:0 (crwdns329834:0crwdne329834:0)

Example: ``Image.HEART + Image.HAPPY``

:param other: (crwdns329838:0crwdne329838:0) crwdns329840:0crwdne329840:0"""
        ...

    def __sub__(self, other: Image) -> Image:
        """crwdns329844:0crwdne329844:0 (crwdns329842:0crwdne329842:0)

Example: ``Image.HEART - Image.HEART_SMALL``

:param other: (crwdns329846:0crwdne329846:0) crwdns329848:0crwdne329848:0"""
        ...

    def __mul__(self, n: float) -> Image:
        """crwdns329852:0``n``crwdne329852:0 (crwdns329850:0crwdne329850:0)

Example: ``Image.HEART * 0.5``

:param n: (crwdns329854:0crwdne329854:0) crwdns329856:0crwdne329856:0"""
        ...

    def __truediv__(self, n: float) -> Image:
        """crwdns329860:0``n``crwdne329860:0 (crwdns329858:0crwdne329858:0)

Example: ``Image.HEART / 2``

:param n: (crwdns329862:0crwdne329862:0) crwdns329864:0crwdne329864:0"""
        ...

class SoundEvent:
    LOUD: SoundEvent
    """crwdns334408:0``quiet``crwdnd334408:0``loud``crwdne334408:0 (crwdns329866:0crwdne329866:0)"""
    QUIET: SoundEvent
    """crwdns334410:0``loud``crwdnd334410:0``quiet``crwdne334410:0 (crwdns329870:0crwdne329870:0)"""

class Sound:
    """crwdns329876:0``audio.play(Sound.NAME)``crwdne329876:0 (crwdns329874:0crwdne329874:0)"""
    GIGGLE: Sound
    """crwdns329880:0crwdne329880:0 (crwdns329878:0crwdne329878:0)"""
    HAPPY: Sound
    """crwdns329884:0crwdne329884:0 (crwdns329882:0crwdne329882:0)"""
    HELLO: Sound
    """crwdns329888:0crwdne329888:0 (crwdns329886:0crwdne329886:0)"""
    MYSTERIOUS: Sound
    """crwdns329892:0crwdne329892:0 (crwdns329890:0crwdne329890:0)"""
    SAD: Sound
    """crwdns329896:0crwdne329896:0 (crwdns329894:0crwdne329894:0)"""
    SLIDE: Sound
    """crwdns329900:0crwdne329900:0 (crwdns329898:0crwdne329898:0)"""
    SOARING: Sound
    """crwdns329904:0crwdne329904:0 (crwdns329902:0crwdne329902:0)"""
    SPRING: Sound
    """crwdns329908:0crwdne329908:0 (crwdns329906:0crwdne329906:0)"""
    TWINKLE: Sound
    """crwdns329912:0crwdne329912:0 (crwdns329910:0crwdne329910:0)"""
    YAWN: Sound
    """crwdns329916:0crwdne329916:0 (crwdns329914:0crwdne329914:0)"""