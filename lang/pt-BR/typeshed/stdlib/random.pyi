"""Gerar números aleatórios. (aleatório)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """Gera um inteiro com ``n`` bits aleatórios.

Example: ``random.getrandbits(1)``

:param n: Um valor entre 1-30 (inclusive)."""
    ...

def seed(n: int) -> None:
    """Inicializa o gerador de números aleatórios. (semente)

Example: ``random.seed(0)``

:param n: A semente inteira

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """Escolhe um inteiro aleatório entre ``a`` e ``b`` inclusive.

Example: ``random.randint(0, 9)``

:param a: Valor inicial para o intervalo (inclusivo)
:param b: Valor final para o intervalo (inclusivo)

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """Escolhe um inteiro selecionado aleatoriamente entre zero e até (mas não incluindo) ``stop``.

Example: ``random.randrange(10)``

:param stop: (parar) Valor final para o intervalo (exclusivo)"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """Escolhe um elemento selecionado aleatoriamente de ``range(start, stop, step)``.

Example: ``random.randrange(0, 10)``

:param start: (iniciar) O início do intervalo (inclusivo)
:param stop: (parar) O fim do intervalo (exclusivo)
:param step: (passo) O passo."""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """Escolhe um elemento aleatório da sequência não vazia ``seq``. (escolha)

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: (sequência) Uma sequência.

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """Gerar um número de ponto flutuante aleatório no intervalo [0.0, 1.0). (aleatório)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """Retorna um número de ponto flutuante aleatório entre ``a`` e ``b``, inclusive. (uniforme)

Example: ``random.uniform(0, 9)``

:param a: Valor inicial para o intervalo (inclusive)
:param b: Valor final para o intervalo (inclusive)"""
    ...