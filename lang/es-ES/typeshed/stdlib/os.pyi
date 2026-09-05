"""Acceder al sistema de archivos. (so)"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Lista los archivos.

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Elimina un archivo. (eliminar)

Example: ``os.remove('data.txt')``

:param filename: (nombre del archivo) El archivo a eliminar.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Devuelve el tamaño de un archivo. (tamaño)

Example: ``os.size('data.txt')``

:param filename: (nombre del archivo) El archivo
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Resultado de ``os.uname()`` (resultado de nombreu)"""
    sysname: str
    """Nombre del sistema operativo. (nombre del sistema)"""
    nodename: str
    """Nombre de la máquina en la red (definida por la implementación). (nombre del nodo)"""
    release: str
    """Versión de lanzamiento del sistema operativo. (lanzamiento)"""
    version: str
    """Versión del sistema operativo. (versión)"""
    machine: str
    """Identificador de hardware. (máquina)"""

def uname() -> uname_result:
    """Devuelve información que identifica el sistema operativo actual. (nombreu)

Example: ``os.uname()``

The return value is an object with five attributes:

- ``sysname`` - operating system name
- ``nodename`` - name of machine on network (implementation-defined)
- ``release`` - operating system release
- ``version`` - operating system version
- ``machine`` - hardware identifier

There is no underlying operating system in MicroPython. As a result the
information returned by the ``uname`` function is mostly useful for
versioning details."""
    ...