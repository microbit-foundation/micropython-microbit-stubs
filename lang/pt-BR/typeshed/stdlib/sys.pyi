"""Funções específicas do sistema (sistema)"""
from typing import Any, Dict, List, NoReturn, TextIO, Tuple

def exit(retval: object=...) -> NoReturn:
    """Termina o programa atual com um código de saída fornecido. (sair)

Example: ``sys.exit(1)``

This function raises a ``SystemExit`` exception. If an argument is given, its
value given as an argument to ``SystemExit``.

:param retval: (valor de retorno) O código de saída ou mensagem."""
    ...

def print_exception(exc: Exception) -> None:
    """Imprime uma exceção com um rastreamento. (imprimir exceção)

Example: ``sys.print_exception(e)``

:param exc: A exceção a ser impressa.

This is simplified version of a function which appears in the
``traceback`` module in CPython."""
argv: List[str]
"""Uma lista mutável de argumentos com os quais o programa atual foi iniciado."""
byteorder: str
"""A ordem dos bytes do sistema (``"little"`` ou ``"big"``). (ordem de bytes)"""

class _implementation:
    name: str
    version: Tuple[int, int, int]
implementation: _implementation
"""Objeto com informações sobre a implementação atual do Python. (implementação)

For MicroPython, it has following attributes:

- ``name`` - string "micropython"
- ``version`` - tuple (major, minor, micro), e.g. (1, 7, 0)

This object is the recommended way to distinguish MicroPython from other
Python implementations (note that it still may not exist in the very
minimal ports).

CPython mandates more attributes for this object, but the actual useful
bare minimum is implemented in MicroPython.
"""
maxsize: int
"""
Valor máximo que um tipo inteiro nativo pode conter na plataforma atual, ou o valor máximo representável pelo tipo inteiro do MicroPython, se for menor que o valor máximo da plataforma (esse é o caso para portas do MicroPython sem suporte para inteiros longos). (tamanho máximo)

This attribute is useful for detecting "bitness" of a platform (32-bit vs
64-bit, etc.). It's recommended to not compare this attribute to some
value directly, but instead count number of bits in it::

    bits = 0
    v = sys.maxsize
    while v:
        bits += 1
        v >>= 1
    if bits > 32:
        # 64-bit (or more) platform
        ...
    else:
        # 32-bit (or less) platform
        # Note that on 32-bit platform, value of bits may be less than 32
        # (e.g. 31) due to peculiarities described above, so use "> 16",
        # "> 32", "> 64" style of comparisons.
"""
modules: Dict[str, Any]
"""Dicionário de módulos carregados. (módulos) 

On some ports, it may not include builtin modules."""
path: List[str]
"""Uma lista mutável de diretórios para pesquisar módulos importados. (caminho)"""
platform: str
"""A plataforma em que o MicroPython está sendo executado. (plataforma) 

For OS/RTOS ports, this is usually an identifier of the OS, e.g. ``"linux"``.
For baremetal ports it is an identifier of a board, e.g. ``"pyboard"`` for 
the original MicroPython reference board. It thus can be used to
distinguish one board from another.

If you need to check whether your program runs on MicroPython (vs other
Python implementation), use ``sys.implementation`` instead.
"""
version: str
"""Versão da linguagem Python à qual esta implementação está em conformidade, como uma string. (versão)"""
version_info: Tuple[int, int, int]
"""Versão da linguagem Python à qual esta implementação está em conformidade, como uma tupla de inteiros. (informação de versão)

Only the first three version numbers (major, minor, micro) are supported and
they can be referenced only by index, not by name.
"""