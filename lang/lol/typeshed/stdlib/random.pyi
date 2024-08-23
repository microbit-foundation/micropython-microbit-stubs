"""crwdns330812:0crwdne330812:0 (crwdns330810:0crwdne330810:0)"""
from typing import TypeVar, Sequence, Union, overload

def getrandbits(n: int) -> int:
    """crwdns330816:0``n``crwdne330816:0 (crwdns330814:0crwdne330814:0)

Example: ``random.getrandbits(1)``

:param n: (crwdns330818:0crwdne330818:0) crwdns330820:0crwdne330820:0"""
    ...

def seed(n: int) -> None:
    """crwdns330824:0crwdne330824:0 (crwdns330822:0crwdne330822:0)

Example: ``random.seed(0)``

:param n: (crwdns330826:0crwdne330826:0) crwdns330828:0crwdne330828:0

This will give you reproducibly deterministic randomness from a given starting
state (``n``)."""
    ...

def randint(a: int, b: int) -> int:
    """crwdns330832:0``a``crwdnd330832:0``b``crwdne330832:0 (crwdns330830:0crwdne330830:0)

Example: ``random.randint(0, 9)``

:param a: (crwdns330834:0crwdne330834:0) crwdns330836:0crwdne330836:0
:param b: (crwdns330838:0crwdne330838:0) crwdns330840:0crwdne330840:0

Alias for ``randrange(a, b + 1)``."""
    ...

@overload
def randrange(stop: int) -> int:
    """crwdns330844:0``stop``crwdne330844:0 (crwdns330842:0crwdne330842:0)

Example: ``random.randrange(10)``

:param stop: (crwdns330846:0crwdne330846:0) crwdns330848:0crwdne330848:0"""
    ...

@overload
def randrange(start: int, stop: int, step: int=1) -> int:
    """crwdns330852:0``range(start, stop, step)``crwdne330852:0 (crwdns330850:0crwdne330850:0)

Example: ``random.randrange(0, 10)``

:param start: (crwdns330854:0crwdne330854:0) crwdns330856:0crwdne330856:0
:param stop: (crwdns330862:0crwdne330862:0) crwdns330864:0crwdne330864:0
:param step: (crwdns330858:0crwdne330858:0) crwdns330860:0crwdne330860:0"""
    ...
_T = TypeVar('_T')

def choice(seq: Sequence[_T]) -> _T:
    """crwdns330868:0``seq``crwdne330868:0 (crwdns330866:0crwdne330866:0)

Example: ``random.choice([Image.HAPPY, Image.SAD])``

:param seq: (crwdns330870:0crwdne330870:0) crwdns330872:0crwdne330872:0

If ``seq`` is  empty, raises ``IndexError``."""
    ...

def random() -> float:
    """crwdns330876:0crwdne330876:0 (crwdns330874:0crwdne330874:0)

Example: ``random.random()``

:return: The random floating point number"""
    ...

def uniform(a: float, b: float) -> float:
    """crwdns330880:0``a``crwdnd330880:0``b``crwdne330880:0 (crwdns330878:0crwdne330878:0)

Example: ``random.uniform(0, 9)``

:param a: (crwdns330882:0crwdne330882:0) crwdns330884:0crwdne330884:0
:param b: (crwdns330886:0crwdne330886:0) crwdns330888:0crwdne330888:0"""
    ...