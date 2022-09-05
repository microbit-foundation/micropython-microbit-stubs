"""Accéder au système de fichiers. (os)"""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Lister les fichiers. (listdir)

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Supprimer (effacer) un fichier. (remove)

Example: ``os.remove('data.txt')``

:param filename: (filename) Le fichier à effacer.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Retourne la taille d'un fichier. (size)

Example: ``os.size('data.txt')``

:param filename: (filename) Le fichier
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Résultat de ``os.uname()`` (uname result)"""
    sysname: str
    """Nom du système d'exploitation. (sysname)"""
    nodename: str
    """Nom de la machine sur le réseau (selon implémentation). (nodename)"""
    release: str
    """La release du système d'exploitation (release)"""
    version: str
    """Version du système d'exploitation (version)"""
    machine: str
    """Identifiant matériel. (machine)"""

def uname() -> uname_result:
    """Retourne les informations identifiant le système d'exploitation actuel. (uname)

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