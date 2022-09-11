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

def set_labels(*args: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Définir l'en-tête du fichier journal

Example: ``log.set_labels('x', 'y', 'z', timestamp=log.MINUTES)``

Each call to this function with positional arguments will generate a new
header entry into the log file.

If the program starts and a log file already exists it will compare the
labels set up by this function call to the last headers declared in the
file. If the headers are different it will add a new header entry at the
end of the file.

:param *args: Un argument positionnel pour chaque en-tête du journal
:param timestamp: (horodatage) L'unité d'horodatage qui sera automatiquement ajoutée comme première colonne de chaque ligne.
Définir cet argument à ``None`` désactive l'horodatage. Passer les valeurs ``log.MILLISECONDS``, ``log.SECONDS``, , ``log.MINUTES``, ``log.HOURS`` ou ``log.DAYS`` définies par ce module. Une valeur invalide lèvera une exception."""
    ...

@overload
def add(log_data: Optional[dict[str, Union[str, int, float]]]) -> None:
    """Ajoute une ligne de données au journal en passant un dictionnaire d'en-têtes et de valeurs.

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

Dictionary keys not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header
entry to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row.

:param log_data: Les données à journaliser, sous la forme d'un dictionnaire ayant une clé pour chaque en-tête."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Ajoute une ligne de données au journal en utilisant des arguments nommés.

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

Keyword arguments not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header entry
to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Supprime le contenu du journal, y compris les en-têtes.

Example: ``log.delete()``

To add the log headers the ``set_labels`` function has to be called again
after this.

:param full: Sélectionne un moyen de suppression "complet" qui supprime les données sur le stockage flash. Si défini à ``False``, une méthode "rapide" est utilisée, elle consiste à invalider les données au lieu d'effectuer un effacement complet plus lent."""
    ...

def set_mirroring(serial: bool):
    """Effectue une copie de l'activité de journalisation des données vers la sortie série.

Example: ``log.set_mirroring(True)``

Mirroring is disabled by default.

:param serial: Passer ``True`` pour répliquer l'activité de journalisation des données sur la sortie série, ``False`` pour désactiver la réplication."""
    ...