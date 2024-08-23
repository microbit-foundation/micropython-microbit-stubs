"""Zaloguj dane do swojego micro:bita V2."""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""Format znacznika czasu w milisekundach."""
SECONDS = 10
"""Format znacznika czasu w sekundach."""
MINUTES = 600
"""Format znacznika czasu w minutach."""
HOURS = 36000
"""Format znacznika czasu w godzinach."""
DAYS = 864000
"""Format znacznika czasu w dniach."""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Ustaw nagłówek pliku dziennika.

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: Dowolna liczba argumentów pozycyjnych, każdy odpowiadający wpisowi w nagłówku dziennika.
:param timestamp: Wybierz jednostkę znacznika czasu, która będzie automatycznie dodana jako pierwsza kolumna w każdym wierszu. Wartości znacznika czasu mogą być jedną z ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` lub ``None``, aby wyłączyć znacznik czasu. Wartością domyślną jest ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Dodaj wiersz danych do dziennika poprzez podanie słownika nagłówków i wartości.

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: Dane do logowania jako słownik z kluczem dla każdego nagłówka."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Dodaj wiersz danych do dziennika używając argumentów słów kluczowych. (dodaj)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Usuwa zawartość wpisu, w tym nagłówki.

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: ``True`` wybiera usunięcie "pełne" i ``False`` wybiera metodę "szybkiego" usunięcia."""
    ...

def set_mirroring(serial: bool):
    """Skonfiguruj lustrzane odbicie logowania danych do wyjścia szeregowego.

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: ``True`` umożliwia odbicie lustrzane danych na szeregowe wyjście."""
    ...