"""Logáil sonraí chuig do micro:bit V2. (loga)"""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""Formáid stampa ama milleasoicindí. (milleasoicindí)"""
SECONDS = 10
"""Formáid stampa ama soicindí. (soicindí)"""
MINUTES = 600
"""Formáid stampa ama nóiméad. (nóiméad)"""
HOURS = 36000
"""Formáid stampa ama uaireanta. (uair an chloig)"""
DAYS = 864000
"""Formáid stampa ama na laethanta. (laethanta)"""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Socraigh ceanntásc an chomhaid logála. (lipéid a shocrú)

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: (*lipéid) Aon líon argóintí suímh, gach ceann ag freagairt d'iontráil sa cheanntásc loga.
:param timestamp: (stampa ama) Roghnaigh an t-aonad stampa ama a chuirfear leis go huathoibríoch mar an chéad cholún i ngach ró. Is féidir le luachanna stampa ama a bheith mar cheann de ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` nó ``None`` chun an stampa ama a dhíchumasú. Is é ``log.SECONDS`` an luach réamhshocraithe."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Cuir ró sonraí leis an loga trí fhoclóir ceanntásca agus luachanna a rith. (cuir leis)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: (foclóir sonraí) Na sonraí le logáil mar fhoclóir le heochair do gach ceanntásc."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Cuir ró sonraí leis an logáil ag baint úsáide as argóintí eochairfhocail. (suimigh)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Scrios inneachar an loga, lena n-áirítear ceanntásca. (scrios)

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: (iomlán) Roghnaíonn ``True`` scriosadh “lán” agus roghnaíonn ``False`` an modh scriosta “tapa”."""
    ...

def set_mirroring(serial: bool):
    """Cumraigh scáthánú na gníomhaíochta logála sonraí chuig an aschur sraitheach. (scáthánú socraithe)

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: (sraitheach) Cumasaíonn ``True`` sonraí a scáthánú leis an aschur sraitheach."""
    ...