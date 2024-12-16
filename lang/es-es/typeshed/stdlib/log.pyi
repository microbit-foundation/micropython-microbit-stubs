"""Registra datos en el micro:bit V2. (registrar)"""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""Formato de marca temporal en milisegundos. (milisegundos)"""
SECONDS = 10
"""Formato de marca temporal en segundos. (segundos)"""
MINUTES = 600
"""Formato de marca temporal en minutos. (minutos)"""
HOURS = 36000
"""Formato de marca temporal en horas. (horas)"""
DAYS = 864000
"""Formato de marca temporal en días. (días)"""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Configura la cabecera del archivo de registro. (configurar etiquetas)

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: (*Etiquetas) Cualquier número de argumentos posicionales, cada uno correspondiente a una entrada en el encabezado del registro.
:param timestamp: (marca de tiempo) Selecciona la unidad de marca de tiempo que se añadirá automáticamente como la primera columna de cada fila. Los valores de la marca de tiempo pueden ser ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` o ``None`` para desactivar la marca de tiempo. El valor por defecto es ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Añade una fila de datos al registro pasando un diccionario de cabeceras y valores. (añadir)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: (diccionario de datos) Los datos que se registrarán como un diccionario con una clave para cada cabecera."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Añade una fila de datos al registro usando argumentos de palabra clave. (añadir)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Elimina el contenido del registro, incluyendo las cabeceras. (eliminar)

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: (completo) ``True`` selecciona un borrador “completo” y ``False`` selecciona el método de borrado “rápido”."""
    ...

def set_mirroring(serial: bool):
    """Configura la duplicación de la actividad de registro de datos en la salida serie. (configurar replicación)

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: (serie) ``True`` habilita la reproducción de datos en la salida de serie."""
    ...