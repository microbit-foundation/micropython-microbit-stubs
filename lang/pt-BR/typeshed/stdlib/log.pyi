"""Registre os dados em seu micro:bit V2."""
from typing import Literal, Mapping, Optional, Union, overload
MILLISECONDS = 1
"""Formato de timestamp de milissegundos. (milissegundos)"""
SECONDS = 10
"""Formato timestamp segundo. (segundos)"""
MINUTES = 600
"""Formato timestamp dos minutos (minutos)"""
HOURS = 36000
"""Formato timestamp das horas. (horas)"""
DAYS = 864000
"""Formato timestamp dias. (Dias)"""

def set_labels(*labels: str, timestamp: Optional[Literal[1, 10, 36000, 864000]]=SECONDS) -> None:
    """Configurar o cabeçalho do arquivo de log. (definir etiquetas)

Example: ``log.set_labels('X', 'Y', 'Z', timestamp=log.MINUTES)``

Ideally this function should be called a single time, before any data is
logged, to configure the data table header once.

If a log file already exists when the program starts, or if this function
is called multiple times, it will check the labels already defined in the
log file. If this function call contains any new labels not already
present, it will generate a new header row with the additional columns.

By default the first column contains a timestamp for each row. The time
unit can be selected via the timestamp argument.

:param *labels: (*rótulos) Qualquer número de argumentos posicionais, cada um correspondente a uma entrada no cabeçalho do registro.
:param timestamp: (registro de data e hora) Selecione a unidade timestamp que será automaticamente adicionada como a primeira coluna de cada linha. Os valores do Timestamp podem ser um dos ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``, ``log.DAYS`` ou ``None`` para desativar o timestamp. O valor padrão é ``log.SECONDS``."""
    ...

@overload
def add(data_dictionary: Optional[Mapping[str, Union[str, int, float]]]) -> None:
    """Adicionar uma linha de dados para o log passando um dicionário de cabeçalhos e valores. (adicionar)

Example: ``log.add({ 'temp': temperature() })``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row.

:param data_dictionary: (dicionário de dados) Os dados a serem registrados como um dicionário com uma chave para cada cabeçalho."""
    ...

@overload
def add(**kwargs: Union[str, int, float]) -> None:
    """Adicionar uma linha de dados ao log usando argumentos de palavra-chave. (adicionar)

Example: ``log.add(temp=temperature())``

Each call to this function adds a row to the log.

New labels not previously specified via the set_labels function, or by a
previous call to this function, will trigger a new header entry to be added
to the log with the extra labels.

Labels previously specified and not present in a call to this function will
be skipped with an empty value in the log row."""
    ...

def delete(full=False):
    """Exclui o conteúdo do log, incluindo cabeçalhos. (Excluir)

Example: ``log.delete()``

To add the log headers again the ``set_labels`` function should to be called after this function.

There are two erase modes; “full” completely removes the data from the physical storage,
and “fast” invalidates the data without removing it.

:param full: (cheio) ``True`` seleciona uma limpeza "completa" e ``False`` seleciona o método de limpeza "rápida"."""
    ...

def set_mirroring(serial: bool):
    """Configure o espelhamento da atividade de registro de dados para a saída serial. (defina espelhamento)

Example: ``log.set_mirroring(True)``

Serial mirroring is disabled by default. When enabled, it will print to serial each row logged into the log file.

:param serial: (série) ``True`` permite espelhar dados para a saída serial."""
    ...