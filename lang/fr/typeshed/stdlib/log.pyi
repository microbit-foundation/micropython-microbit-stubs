"""Journalisez des données sur votre micro:bit V2."""
from typing import Literal, Optional, Union, overload
MILLISECONDS = 1
"""Format d'horodatage en millisecondes."""
SECONDS = 10
"""Format d'horodatage en secondes."""
MINUTES = 600
"""Format d'horodatage en minutes."""
HOURS = 36000
"""Format d'horodatage en heures."""
DAYS = 864000
"""Format d'horodatage en jours."""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Définir l'en-tête du fichier journal

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: Any number of positional arguments, each corresponding to an entry in the log header.
:param timestamp: (horodatage) Select the timestamp unit that will be automatically added as the first column in every row. Timestamp values can be one of ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` or ``None`` to disable the timestamp. The default value is ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[dict[str, Union[str, int, float]]]) -> None:
    """Ajoute une ligne de données au journal en passant un dictionnaire d'en-têtes et de valeurs.

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: The data to log as a dictionary with a key for each header."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Ajoute une ligne de données au journal en utilisant des arguments nommés.

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Supprime le contenu du journal, y compris les en-têtes.

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: ``True`` selects a “full” erase and ``False`` selects the “fast” erase method."""
    ...

def set_mirroring(serial: bool):
    """Configure mirroring of the data logging activity to the serial output.

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: ``True`` enables mirroring data to the serial output."""
    ...