import sys
from typing import Dict, Generic, Tuple, TypeVar

if sys.version_info >= (3, 10):
    from typing import (
        Callable,
        ItemsView,
        Iterable,
        Iterator,
        KeysView,
        Mapping,
        MutableMapping,
        MutableSequence,
        Reversible,
        Sequence,
        ValuesView,
    )
else:
    from _collections_abc import *

_S = TypeVar("_S")
_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class _OrderedDictKeysView(KeysView[_KT], Reversible[_KT]):
    def __reversed__(self) -> Iterator[_KT]: ...

class _OrderedDictItemsView(ItemsView[_KT, _VT], Reversible[Tuple[_KT, _VT]]):
    def __reversed__(self) -> Iterator[Tuple[_KT, _VT]]: ...

class _OrderedDictValuesView(ValuesView[_VT], Reversible[_VT]):
    def __reversed__(self) -> Iterator[_VT]: ...

class OrderedDict(Dict[_KT, _VT], Reversible[_KT], Generic[_KT, _VT]):
    def popitem(self, last: bool = ...) -> Tuple[_KT, _VT]: ...
    def move_to_end(self, key: _KT, last: bool = ...) -> None: ...
    def copy(self: _S) -> _S: ...
    def __reversed__(self) -> Iterator[_KT]: ...
    def keys(self) -> _OrderedDictKeysView[_KT]: ...
    def items(self) -> _OrderedDictItemsView[_KT, _VT]: ...
    def values(self) -> _OrderedDictValuesView[_VT]: ...