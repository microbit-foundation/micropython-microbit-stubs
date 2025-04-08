"""Zeichne Daten auf deinem micro:bit V2 auf."""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""Zeitstempelformat: Millisekunden (millisekunden)"""
SECONDS = 10
"""Zeitstempelformat: Sekunden (sekunden)"""
MINUTES = 600
"""Zeitstempelformat: Minuten (minuten)"""
HOURS = 36000
"""Zeitstempelformat: Stunden (stunden)"""
DAYS = 864000
"""Zeitstempelformat: Tage (tage)"""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Spaltenüberschrift der Logdatei setzen (Beschriftungen festlegen)

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: (*Beschriftung) Eine beliebige Anzahl von Positionsargumenten, die jeweils einem Eintrag in der Kopfzeile des Logs entsprechen.
:param timestamp: (Zeitstempel) Wähle die Zeitstempel-Einheit, die automatisch als erste Spalte in jeder Zeile hinzugefügt wird. Der Zeitstempel kann einen der folgenden Werte annehmen: ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` oder ``None``, um den Zeitstempel zu deaktivieren. Der Standardwert ist ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Füge dem Protokoll eine Datenzeile hinzu, indem du ein Dictionary mit Kopfzeileneinträgen und Werten übergibst. (hinzufügen)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: (daten wörterbuch) Die zu protokollierenden Daten in Form eines Dictionarys mit einem Schlüssel für jeden Kopfzeileneintrag."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Füge dem Protokoll eine Datenzeile mit Schlüsselwörtern als Argumenten hinzu. (hinzufügen)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Löscht den Inhalt des Protokolls, einschließlich der Kopfzeilen. (löschen)

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: (vollständig) Mit ``True`` wird ein " vollständiges" Löschen und mit ``False`` die "schnelle" Löschmethode gewählt."""
    ...

def set_mirroring(serial: bool):
    """Richte die Spiegelung der Datenprotokollierung auf dem seriellen Ausgang ein. (spiegeln)

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: (seriell) ``True`` aktiviert die Spiegelung von Daten auf dem seriellen Ausgang."""
    ...