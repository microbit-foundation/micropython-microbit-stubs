"""Cruthaigh agus seinn séiseanna. (ceol)"""
from typing import Optional, Tuple, Union, List
from .microbit import MicroBitDigitalPin, pin0
DADADADUM: Tuple[str, ...]
"""Fonn: oscailt 5ú Siansa Beethoven i C mion."""
ENTERTAINER: Tuple[str, ...]
"""Fonn: an blúire oscailte de chlasaic Ragtime Scott Joplin "The Entertainer". (siamsóir)"""
PRELUDE: Tuple[str, ...]
"""Fonn: oscailt an chéad Réamhrá i C Major de 48 Réamhráite agus Fugues J.S.Bach. (réamhrá)"""
ODE: Tuple[str, ...]
"""Fonn: an téama "Ode to Joy" ó 9ú Siansa Beethoven in D minor."""
NYAN: Tuple[str, ...]
"""Fonn: téama Nyan Cat (http://www.nyan.cat/).

The composer is unknown. This is fair use for educational porpoises (as they say in New York)."""
RINGTONE: Tuple[str, ...]
"""Fonn: rud a fhuaimníonn cosúil le clingthon fón póca. (clingthon)

To be used to indicate an incoming message.
"""
FUNK: Tuple[str, ...]
"""Fonn: líne dord spraíúil do ghníomhairí rúnda agus do mháistir-intinn choiriúla. (func)"""
BLUES: Tuple[str, ...]
"""Fonn: a boogie-woogie 12-bar blues ag siúl Bass."""
BIRTHDAY: Tuple[str, ...]
"""Fonn: "Breithlá sona duit..." (lá breithe)

For copyright status see: http://www.bbc.co.uk/news/world-us-canada-34332853
"""
WEDDING: Tuple[str, ...]
"""Fonn: an curfá bridal ó cheoldráma Wagner "Lohengrin". (pósadh)"""
FUNERAL: Tuple[str, ...]
"""Fonn : an “máirseáil sochraide” ar a dtugtar freisin Sonáid Phianó Uimh. 2 i B♭ beag, Op. 35 le Frédéric Chopin. (sochraid)"""
PUNCHLINE: Tuple[str, ...]
"""Fonn: tá blúire spraoi a léiríonn magadh déanta."""
PYTHON: Tuple[str, ...]
"""Fonn: Máirseáil John Philip Sousa “Liberty Bell” ar a dtugtar téama “Monty Python’s Flying Circus” (ar a dtugtar an teanga ríomhchlárúcháin Python ina diaidh)."""
BADDY: Tuple[str, ...]
"""Fonn: bealach isteach ré an scannáin chiúin de drochdhuine. (drochdhuine)"""
CHASE: Tuple[str, ...]
"""Fonn: radharc ruaig ré scannán ciúin. (ruaig)"""
BA_DING: Tuple[str, ...]
"""Fonn: comhartha gearr chun a chur in iúl gur tharla rud éigin."""
WAWAWAWAA: Tuple[str, ...]
"""Fonn: trombón an-bhrónach."""
JUMP_UP: Tuple[str, ...]
"""Fonn: le húsáid i gcluiche, rud a léiríonn gluaiseacht aníos. (léim suas)"""
JUMP_DOWN: Tuple[str, ...]
"""Séis: le húsáid i gcluiche, rud a léiríonn gluaiseacht anuas. (léim síos)"""
POWER_UP: Tuple[str, ...]
"""Fonn: fonnfóir chun éacht a dhíghlasáil a léiriú. (cumhacht suas)"""
POWER_DOWN: Tuple[str, ...]
"""Fonn: faitíos brónach chun éacht a cailleadh a léiriú. (cumhacht síos)"""

def set_tempo(ticks: int=4, bpm: int=120) -> None:
    """Socraigh an luas garbh le haghaidh athsheinm. (socraigh tempo)

Example: ``music.set_tempo(bpm=120)``

:param ticks: (sceartáin) Líon na sceartán ar buille iad.
:param bpm: Slánuimhir a chinneann cé mhéad buille in aghaidh an nóiméid.

Suggested default values allow the following useful behaviour:

- music.set_tempo() – reset the tempo to default of ticks = 4, bpm = 120
- music.set_tempo(ticks=8) – change the “definition” of a beat
- music.set_tempo(bpm=180) – just change the tempo

To work out the length of a tick in milliseconds is very simple arithmetic:
60000/bpm/ticks_per_beat. For the default values that’s
60000/120/4 = 125 milliseconds or 1 beat = 500 milliseconds."""
    ...

def get_tempo() -> Tuple[int, int]:
    """Faigheann an luas reatha mar tupla slánuimhreacha: ``(ticks, bpm)``. (faigh tempo)

Example: ``ticks, beats = music.get_tempo()``

:return: The temp as a tuple with two integer values, the ticks then the beats per minute."""
    ...

def play(music: Union[str, List[str], Tuple[str, ...]], pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True, loop: bool=False) -> None:
    """Seinneann sé ceol. (seinn)

Example: ``music.play(music.NYAN)``

:param music: (ceol) ceol a shonraítear in 'nodaireacht speisialta <https://microbit-micropython.readthedocs.io/en/v2-docs/music.html#musical-notation>'_
:param pin: (biorán) an bioráin aschuir le húsáid le cainteoir seachtrach (réamhshocraithe ``pin0``), ``None`` gan aon fhuaim.
:param wait: (fan) Má tá ``wait`` socraithe go ``True``, tá an fheidhm seo ag blocáil.
:param loop: (lúb) Má tá ``loop`` socraithe go ``True``, athrá ar an tiún go dtí go dtugtar ``stop`` nó go gcuirtear isteach ar an nglao blocála.

Many built-in melodies are defined in this module."""
    ...

def pitch(frequency: int, duration: int=-1, pin: Optional[MicroBitDigitalPin]=pin0, wait: bool=True) -> None:
    """Seinn nóta. (páirc)

Example: ``music.pitch(185, 1000)``

:param frequency: (minicíocht) Minicíocht slánuimhir
:param duration: (fad) Fad milleasoicind. Má tá fuaim dhiúltach ansin leanúnach go dtí an chéad ghlao eile nó glao ar ``stop``.
:param pin: (biorán) Bioráin aschuir roghnach (réamhshocraithe ``pin0``).
:param wait: (fan) Má tá ``wait`` socraithe go ``True``, tá an fheidhm seo ag blocáil.

For example, if the frequency is set to 440 and the length to
1000 then we hear a standard concert A for one second.

You can only play one pitch on one pin at any one time."""
    ...

def stop(pin: Optional[MicroBitDigitalPin]=pin0) -> None:
    """Stopann sé gach athsheinm ceoil ar an gcainteoir tógtha isteach agus aon fhuaim aschur bioráin. (stad)

Example: ``music.stop()``

:param pin: (pionna) Is féidir argóint roghnach a chur ar fáil chun biorán a shonrú, m.sh. ``music.stop(pin1)``."""

def reset() -> None:
    """Athshocraigh sceartáin, bpm, fad agus ochtach chuig a luachanna réamhshocraithe. (athshocrú)

Example: ``music.reset()``

Values:
- ``ticks = 4``
- ``bpm = 120``
- ``duration = 4``
- ``octave = 4``"""
    ...