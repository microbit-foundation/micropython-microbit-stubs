"""Registra datos en el micro:bit V2. (registrar)"""
from typing import Literal, Optional, Union, overload
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

def set_labels(*args: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Configura la cabecera del archivo de registro. (configurar etiquetas)

Example: ``log.set_labels('x', 'y', 'z', timestamp=log.MINUTES)``

Each call to this function with positional arguments will generate a new
header entry into the log file.

If the program starts and a log file already exists it will compare the
labels set up by this function call to the last headers declared in the
file. If the headers are different it will add a new header entry at the
end of the file.

:param *args: Un argumento posicional para cada cabecera de registro.
:param timestamp: (marca de tiempo) La unidad de marca temporal que se añadirá automáticamente como la primera columna en cada fila.
Establecer este argumento a ``None`` desactiva la marca temporal. Se le pueden pasar los valores ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS`` o ``log.DAYS`` definidos en este módulo. Un valor no válido lanzará una excepción."""
    ...

@overload
def add(log_data: Optional[dict[str, Union[str, int, float]]]) -> None:
    """Añade una fila de datos al registro pasando un diccionario de cabeceras y valores. (añadir)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

Dictionary keys not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header
entry to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row.

:param log_data: (registrar datos) Los datos a registrar como un diccionario con una clave para cada cabecera."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Añade una fila de datos al registro usando argumentos de palabra clave. (añadir)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

Keyword arguments not already specified via the ``set_labels`` function,
or by a previous call to this function, will trigger a new header entry
to be added to the log with the extra label.

Labels previously specified and not present in this function call will be
skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Elimina el contenido del registro, incluyendo las cabeceras. (eliminar)

Example: ``log.delete()``

To add the log headers the ``set_labels`` function has to be called again
after this.

:param full: (completo) Selecciona un formato de borrado "completo" que elimina los datos del almacenamiento flash.
Si se pone a ``False`` (falso), usa un método "rápido" que invalida los datos en lugar de realizar un borrado completo más lento."""
    ...

def set_mirroring(serial: bool):
    """Replica la actividad del registro de datos en la salida serie. (configurar replicación)

Example: ``log.set_mirroring(True)``

Mirroring is disabled by default.

:param serial: (serie) Si se le pasa ``True`` (verdadero), replicará la actividad del registro de datos en la salida serie; si se le pasa ``False`` (falso), se desactivará la replicación."""
    ...