"""Rassembler et désassembler des types de données primitives."""
from _typeshed import ReadableBuffer, WriteableBuffer
from typing import Any, Tuple, Union

def calcsize(fmt: str) -> int:
    """Récupère le nombre d'octets nécessaires pour stocker le ``fmt`` donné.

Example: ``struct.calcsize('hf')``

:param fmt: Une chaîne de mise en forme.
:return The number of bytes needed to store such a value."""
    ...

def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
    """Rassembler les valeurs selon une chaîne de mise en forme.

Example: ``struct.pack('hf', 1, 3.1415)``

:param fmt: La chaîne de mise en forme.
:param v1: La première valeur.
:param *vn: Les valeurs restantes.
:return A bytes object encoding the values."""
    ...

def pack_into(fmt: str, buffer: WriteableBuffer, offset: int, v1: Any, *vn: Any) -> None:
    """Rassembler les valeurs selon une chaîne de format. (Rassembler dans)

Example: ``struct.pack_info('hf', buffer, 1, 3.1415)``

:param fmt: La chaîne de format.
:param buffer: Le tampon cible dans lequel écrire.
:param offset: Le décalage dans le tampon. Peut être négatif pour compter à partir de la fin du tampon.
:param v1: La première valeur.
:param *vn: Les valeurs restantes."""
    ...

def unpack(fmt: str, data: ReadableBuffer) -> Tuple[Any, ...]:
    """Décompacter les données selon une chaîne de format.

Example: ``v1, v2 = struct.unpack('hf', buffer)``

:param fmt: La chaîne de format.
:param data: Les données.
:return: A tuple of the unpacked values."""
    ...

def unpack_from(fmt: str, buffer: ReadableBuffer, offset: int=0) -> Tuple:
    """Décompacter les données d'un tampon selon une chaîne de format.

Example: ``v1, v2 = struct.unpack_from('hf', buffer)``

:param fmt: La chaîne de format.
:param buffer: Le tampon source à partir duquel lire.
:param offset: Le décalage dans le tampon. Peut être négatif pour compter à partir de la fin du tampon.
:return: A tuple of the unpacked values."""
    ...