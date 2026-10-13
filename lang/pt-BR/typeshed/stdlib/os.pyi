"""Acessar o sistema de arquivos."""
from typing import Tuple
from typing import List

def listdir() -> List[str]:
    """Listar arquivos. (listar diretório)

Example: ``os.listdir()``

:return: A list of the names of all the files contained within the local
persistent on-device file system."""
    ...

def remove(filename: str) -> None:
    """Remover (excluir) um arquivo. (remover)

Example: ``os.remove('data.txt')``

:param filename: (nome do arquivo) O arquivo a ser excluído.

If the file does not exist an ``OSError`` exception will occur."""
    ...

def size(filename: str) -> int:
    """Retorna o tamanho de um arquivo. (tamanho)

Example: ``os.size('data.txt')``

:param filename: (nome do arquivo) O arquivo
:return: The size in bytes.

If the file does not exist an ``OSError`` exception will occur."""

class uname_result(Tuple[str, str, str, str, str]):
    """Resultado de ``os.uname()`` (resultado do uname)"""
    sysname: str
    """Nome do sistema operacional."""
    nodename: str
    """Nome da máquina na rede (definido pela implementação)."""
    release: str
    """Versão do sistema operacional. (lançamento)"""
    version: str
    """Versão do sistema operacional. (versão)"""
    machine: str
    """Identificador de hardware. (máquina)"""

def uname() -> uname_result:
    """Retorna informações que identificam o sistema operacional atual.

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