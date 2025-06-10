"""Cuir an micro:bit ag caint, ag canadh agus ag déanamh fuaimeanna eile cosúil le cainte. (óráid)"""
from typing import Optional
from .microbit import MicroBitDigitalPin, pin0

def translate(words: str) -> str:
    """Aistrigh focail Bhéarla go fóinéimí. (aistrigh)

Example: ``speech.translate('hello world')``

:param words: (focail) Teaghrán focal Béarla.
:return: A string containing a best guess at the appropriate phonemes to pronounce.
The output is generated from this `text to phoneme translation table <https://github.com/s-macke/SAM/wiki/Text-to-phoneme-translation-table>`_.

This function should be used to generate a first approximation of phonemes
that can be further hand-edited to improve accuracy, inflection and
emphasis.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def pronounce(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Fóinéimí a fhuaimniú. (fuaimniú)

Example: ``speech.pronounce(' /HEHLOW WERLD')``

:param phonemes: (fóinéimí) An teaghrán fóinéimí a fhuaimniú
:param pitch: (airde) Uimhir a sheasann do pháirc an ghutha
:param speed: (luas) Uimhir a léiríonn luas an ghutha
:param mouth: (béal) Uimhir a sheasann do bhéal an ghutha
:param throat: (scornach) Uimhir a sheasann do scornach an ghutha
:param pin: (biorán) Is féidir argóint roghnach chun an bioráin aschuir a shonrú a úsáid chun mainneachtain ``pin0``a shárú.
Mura dteastaíonn uainn aon fhuaim a sheinm as na bioráin is féidir ``pin=None``a úsáid. micro:bit V2 amháin.

Override the optional pitch, speed, mouth and throat settings to change the
timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def say(words: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Abair focail Bhéarla. (abair)

Example: ``speech.say('hello world')``

:param words: (focail) An teaghrán focal le rá.
:param pitch: (airde) Uimhir a léiríonn airde an ghutha
:param speed: (luas) Uimhir a léiríonn luas an ghlór
:param mouth: (béal) Uimhir a sheasann do bhéal an ghutha
:param throat: (scornach) Uimhir a sheasann do scornach an ghutha
:param pin: (biorán) Is féidir argóint roghnach a úsáid chun an biorán aschuir a shonrú chun an réamhshocrú ``pin0`` a shárú.
Mura dteastaíonn uainn go seinnfí aon fhuaim as na bioráin is féidir ``pin=None`` a úsáid. micro:bit V2 amháin.

The result is semi-accurate for English. Override the optional pitch, speed,
mouth and throat settings to change the timbre (quality) of the voice.

This is a short-hand equivalent of:
``speech.pronounce(speech.translate(words))``

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...

def sing(phonemes: str, pitch: int=64, speed: int=72, mouth: int=128, throat: int=128, pin: MicroBitDigitalPin=pin0) -> None:
    """Can fóinéimí. (canadh)

Example: ``speech.sing(' /HEHLOW WERLD')``

:param phonemes: (fóinéimí) An teaghrán focal le canadh.
:param pitch: (airde) Uimhir a léiríonn airde an ghutha
:param speed: (luas) Uimhir a léiríonn luas an ghlór
:param mouth: (béal) Uimhir a sheasann do bhéal an ghutha
:param throat: (scornach) Uimhir a sheasann do scornach an ghutha
:param pin: (biorán) Is féidir argóint roghnach chun an bioráin aschuir a shonrú a úsáid chun mainneachtain ``pin0``a shárú.
Mura dteastaíonn uainn aon fhuaim a sheinm as na bioráin is féidir ``pin=None``a úsáid. micro:bit V2 amháin.

Override the optional pitch, speed, mouth and throat settings to change
the timbre (quality) of the voice.

See `the online documentation <https://microbit-micropython.readthedocs.io/en/v2-docs/speech.html>`_ for detailed information."""
    ...