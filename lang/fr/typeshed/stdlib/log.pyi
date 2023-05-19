"""Journalisez des données sur votre micro:bit V2."""
from typing import Literal, Mapping, Optional, Union, overload
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

:param *labels: Un nombre quelconque d'arguments positionnels, chacun correspondant à une entrée dans l'en-tête du journal.
:param timestamp: (horodatage) Sélectionnez l'unité d'horodatage qui sera automatiquement ajoutée comme première colonne de chaque ligne. Les valeurs d'horodatage peuvent être l'une des suivantes ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` ou ``None`` pour désactiver l'horodatage. La valeur par défaut est ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Ajoute une ligne de données au journal en passant un dictionnaire d'en-têtes et de valeurs.

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: Les données à enregistrer sous forme de dictionnaire avec une clé pour chaque en-tête."""
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

:param full: ``True`` sélectionne un effacement "complet" et ``False`` sélectionne la méthode d'effacement "rapide"."""
    ...

def set_mirroring(serial: bool):
    """Configurez la mise en miroir de l'activité d'enregistrement des données sur la sortie série.

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: ``True`` active la mise en miroir des données sur la sortie série."""
    ...