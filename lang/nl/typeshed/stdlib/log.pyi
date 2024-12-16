"""Log gegevens in op je micro:bit V2."""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""Milliseconden tijdstempel formaat. (milliseconden)"""
SECONDS = 10
"""Seconden tijdstempel formaat. (seconden)"""
MINUTES = 600
"""Minuten tijdstempel formaat. (minuten)"""
HOURS = 36000
"""Uren tijdstempel formaat. (uren)"""
DAYS = 864000
"""Dagen tijdstempel formaat. (dagen)"""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Stel de logbestandheader in. (kies labels)

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: Een willekeurig aantal positionele argumenten, elk corresponderend aan een vermelding in de log header.
:param timestamp: (tijdstempel) Selecteer de eenheid van de tijdsaanduiding die automatisch als eerste kolom in elke rij wordt toegevoegd. Tijdstempel waarden kunnen een van ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, , , ``log.HOURS``, ``log.DAYS`` of ``None`` om de tijdstempel uit te schakelen. De standaardwaarde is ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Voeg een gegevensrij toe aan de log door een woordenboek van koppen en waarden te passeren. (toevoegen)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: (gegevenswoordenboek) De gegevens die moeten worden geregistreerd als woordenboek met een sleutel voor elke header."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Voeg een gegevensrij toe aan het logboek met behulp van trefwoordargumenten. (toevoegen)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Verwijdert de inhoud van het log, inclusief headers. (verwijderen)

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: (volledig) ``True`` selecteert een "volledige" wissen en ``False`` selecteert de "snel" wis methode."""
    ...

def set_mirroring(serial: bool):
    """Configureer het spiegelen van de data logging activiteit naar de seriële uitgang. (stel spiegelen in)

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: (serieel) ``True`` maakt het spiegelen van gegevens naar de seriële uitvoer mogelijk."""
    ...