"""Acceder al sistema de archivos. (os)"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Lista los archivos. (listdir)

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Elimina un archivo. (remove)

Example: ``os.remove('data.txt')``

:param filename: (filename) El archivo a eliminar.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Devuelve el tamaño de un archivo. (tamaño)

Example: ``os.size('data.txt')``

:param filename: (filename) El archivo
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Resultado de ``os.uname()`` (uname result)"""
    sysname: str
    """Nombre del sistema operativo. (sysname)"""
    nodename: str
    """Nombre de la máquina en la red (definida por la implementación). (nodename)"""
    release: str
    """Versión de lanzamiento del sistema operativo. (release)"""
    version: str
    """Versión del sistema operativo. (version)"""
    machine: str
    """Identificador de hardware. (máquina)"""

def uname() -> uname_result:
    """Devuelve información que identifica el sistema operativo actual. (uname)

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