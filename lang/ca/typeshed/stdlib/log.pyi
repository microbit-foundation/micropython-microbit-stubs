"""Registre dades en la micro:bit V2 (registre)"""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""Format de marca de temps de mil·lisegons. (mil·lisegons)"""
SECONDS = 10
"""Format de marca de temps de segons. (segons)"""
MINUTES = 600
"""Format de marca de temps de minuts. (minuts)"""
HOURS = 36000
"""Format de marca de temps d'hores. (hores)"""
DAYS = 864000
"""Format de marca de temps de dies. (dies)"""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Defineix la capçalera del fitxer de registre. (Defineix l'etiqueta)

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: Qualsevol nombre d'arguments posicionals, corresponent cadascun a una entrada en la capçalera del registre.
:param timestamp: (marca horària) Selecciona la unitat de la marca del temps que serà automaticament afegida com a primera columna de cada fila. Els valors de la marca del temps pot ser un de  ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` o ``None``  per desactivar la marca del temps. El valor per defecte es ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Afegeix una fila de dades al registre passant un diccionari de capçaleres i valors. (afegeix)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: (diccionari de dades) Les dades a ser registrades com un diccionari amb una clau per cada capçalera."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Afegeix una fila de dades al registre fent servir arguments de paraula clau. (afegeix)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Suprimeix el contingut del registre, incloses les capçaleres. (suprimeix)

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: (ple) ``True`` selecciona un esborrat "total"  ``False`` selecciona un mètode d'esborrat "ràpid"."""
    ...

def set_mirroring(serial: bool):
    """Configura la duplicació de l'activitat de registre de dades a la sortida en sèrie. (estableix mirall)

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: ``True`` permet la duplicació de les dades a la sortida sèrie."""
    ...