"""Taispeáin téacs, íomhánna agus beochan ar an taispeáint LED 5×5. (taispeáint)"""
from ..microbit import Image
from typing import Union, overload, Iterable

def get_pixel(x: int, y: int) -> int:
    """Faigh gile an LED ag colún ``x`` agus as a chéile ``y``. (faigh picteilín)

Example: ``display.get_pixel(0, 0)``

:param x: An colún taispeána (0..4)
:param y: An tsraith taispeána (0..4)
:return: A number between 0 (off) and 9 (bright)"""
    ...

def set_pixel(x: int, y: int, value: int) -> None:
    """Socraigh gile an LED ag colún ``x`` agus as a chéile ``y``. (socraigh picteilín)

Example: ``display.set_pixel(0, 0, 9)``

:param x: An colún taispeána (0..4)
:param y: An tsraith taispeána (0..4)
:param value: (luach) An ghile idir 0 (as) agus 9 (geal)"""
    ...

def clear() -> None:
    """Socraigh gile na soilse go léir go 0 (as). (soiléir)

Example: ``display.clear()``"""
    ...

def show(image: Union[str, float, int, Image, Iterable[Image]], delay: int=400, wait: bool=True, loop: bool=False, clear: bool=False) -> None:
    """Taispeáin íomhánna, litreacha nó digití ar an taispeáint LED. (taispeáin)

Example: ``display.show(Image.HEART)``

When ``image`` is an image or a list of images then each image is displayed in turn.
If ``image`` is a string or number, each letter or digit is displayed in turn.

:param image: (íomhá) Teaghrán, uimhir, íomhá nó liosta íomhánna le taispeáint.
:param delay: (moill) Taispeántar gach litir, digit nó íomhá le milleasoicindí ``delay`` eatarthu.
:param wait: (fan) Más ``wait`` é ``True``, cuirfear bac ar an bhfeidhm seo go dtí go mbeidh an bheochan críochnaithe, nó tarlóidh an bheochan sa chúlra.
:param loop: (lúb) Má tá ``loop`` ``True``, déanfaidh an beochan arís go deo.
:param clear: (soiléir) Más ionann ``clear`` agus ``True``, glanfar an taispeáint tar éis don seicheamh a bheith críochnaithe.

The ``wait``, ``loop`` and ``clear`` arguments must be specified using their keyword."""
    ...

def scroll(text: Union[str, float, int], delay: int=150, wait: bool=True, loop: bool=False, monospace: bool=False) -> None:
    """Scrollaigh uimhir nó téacs ar an taispeáint LED. (scrollaigh)

Example: ``display.scroll('micro:bit')``

:param text: (téacs) An teaghrán le scrollú. Más slánuimhir nó snámhphointe é ``text`` tiontaítear é ar dtús go teaghrán ag baint úsáide as ``str()``.
:param delay: (moill) Rialaíonn an paraiméadar ``delay`` cé chomh tapa is atá an téacs ag scrollú.
:param wait: (fan) Má tá ``wait`` ``True``, blocálfaidh an fheidhm seo go dtí go mbeidh an beochan críochnaithe, nó tarlóidh an beochan sa chúlra.
:param loop: (lúb) Má tá ``loop`` ``True``, déanfaidh an beochan arís go deo.
:param monospace: (monaspás) Más ``monospace`` é ``True``, tógfaidh na carachtair go léir suas le 5 cholún picteilín ar leithead, nó mura mbeidh go díreach 1 cholún bán picteilín idir gach carachtar agus iad ag scrollú.

The ``wait``, ``loop`` and ``monospace`` arguments must be specified
using their keyword."""
    ...

def on() -> None:
    """Cas ar an taispeáint LED. (ar)

Example: ``display.on()``"""
    ...

def off() -> None:
    """Múch an taispeáint LED (ceadaíonn an taispeáint a dhíchumasú duit na bioráin GPIO a athúsáid chun críocha eile). (as)

Example: ``display.off()``"""
    ...

def is_on() -> bool:
    """Seiceáil an bhfuil an taispeáint LED cumasaithe. (atá ar)

Example: ``display.is_on()``

:return: ``True`` if the display is on, otherwise returns ``False``."""
    ...

def read_light_level() -> int:
    """Léigh leibhéal an tsolais. (léigh leibhéal an tsolais)

Example: ``display.read_light_level()``

Uses the display's LEDs in reverse-bias mode to sense the amount of light
falling on the display.

:return: An integer between 0 and 255 representing the light level, with larger meaning more light."""
    ...